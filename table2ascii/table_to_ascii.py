from __future__ import annotations

import textwrap
from math import ceil, floor
from collections.abc import Sequence

from wcwidth import wcswidth

from .alignment import Alignment
from .annotations import SupportsStr
from .exceptions import (
    AlignmentCountMismatchError,
    BodyColumnCountMismatchError,
    ColumnWidthTooSmallError,
    ColumnWidthsCountMismatchError,
    FooterColumnCountMismatchError,
    InvalidAlignmentError,
    InvalidCellPaddingError,
    InvalidColumnWidthError,
    NoHeaderBodyOrFooterError,
)
from .merge import Merge
from .options import Options
from .preset_style import PresetStyle
from .table_style import TableStyle


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(
        self,
        header: Sequence[SupportsStr] | None,
        body: Sequence[Sequence[SupportsStr]] | None,
        footer: Sequence[SupportsStr] | None,
        options: Options,
    ):
        """Validate arguments and initialize fields

        Args:
            header: The values in the header of the table
            body: The rows of values in the body of the table
            footer: The values in the footer of the table
            options: The options for the table
        """
        # initialize fields
        self.__header = list(header) if header else None
        self.__body = list([list(row) for row in body]) if body else None
        self.__footer = list(footer) if footer else None
        self.__style = options.style
        self.__first_col_heading = options.first_col_heading
        self.__last_col_heading = options.last_col_heading
        self.__cell_padding = options.cell_padding
        self.__use_wcwidth = options.use_wcwidth

        # calculate number of columns
        self.__columns = self.__count_columns()

        # check if footer has a different number of columns
        if footer and len(footer) != self.__columns:
            raise FooterColumnCountMismatchError(footer, self.__columns)
        # check if any rows in body have a different number of columns
        if body and any(len(row) != self.__columns for row in body):
            raise BodyColumnCountMismatchError(body, self.__columns)

        # check that at least one of header, body, or footer is not None
        if not header and not body and not footer:
            raise NoHeaderBodyOrFooterError()

        self.__alignments = self.__determine_alignments(
            options.alignments, default=Alignment.CENTER
        )
        self.__number_alignments = self.__determine_alignments(
            options.number_alignments, default=self.__alignments
        )

        # keep track of the number widths and positions of the decimal points for decimal alignment
        decimal_widths, decimal_positions = self.__calculate_decimal_widths_and_positions()
        self.__decimal_widths: list[int] = decimal_widths
        self.__decimal_positions: list[int] = decimal_positions

        # calculate or use given column widths
        self.__column_widths = self.__calculate_column_widths(options.column_widths)

        # check if the cell padding is valid
        if self.__cell_padding < 0:
            raise InvalidCellPaddingError(self.__cell_padding)

        # if any row starts with Merge.LEFT, replace it with an empty string
        self.__fix_rows_beginning_with_merge()

    def __count_columns(self) -> int:
        """Get the number of columns in the table based on the provided header, footer, and body lists.

        Returns:
            The number of columns in the table
        """
        if self.__header:
            return len(self.__header)
        if self.__footer:
            return len(self.__footer)
        if self.__body and len(self.__body) > 0:
            return len(self.__body[0])
        return 0

    def __determine_alignments(
        self,
        user_alignments: Sequence[Alignment] | Alignment | None,
        *,
        default: Sequence[Alignment] | Alignment,
    ) -> list[Alignment]:
        """Determine the alignments for each column based on the user provided alignments option.

        Args:
            user_alignments: The alignments specified by the user
            default: The default alignments to use if user_alignments is None

        Returns:
            The alignments for each column in the table
        """
        alignments = user_alignments if user_alignments is not None else default

        # if alignments is a single Alignment, convert it to a list of that Alignment
        if isinstance(alignments, Alignment):
            alignments = [alignments] * self.__columns

        # check if alignments specified have a different number of columns
        if len(alignments) != self.__columns:
            raise AlignmentCountMismatchError(alignments, self.__columns)

        return list(alignments)

    def __widest_line(self, value: SupportsStr) -> int:
        """Returns the width of the longest line in a multi-line string"""
        text = str(value)
        return max(self.__str_width(line) for line in text.splitlines()) if len(text) else 0

    def __auto_column_widths(self) -> list[int]:
        """Get the minimum number of characters needed for the values in each column in the table
        with 1 space of padding on each side.

        Returns:
            The minimum number of characters needed for each column
        """

        def get_column_width(row: Sequence[SupportsStr], column: int) -> int:
            """Get the width of a cell in a column"""
            value = row[column]
            next_value = row[column + 1] if column < self.__columns - 1 else None
            if value is Merge.LEFT or next_value is Merge.LEFT:
                return 0
            return self.__widest_line(value)

        column_widths = []
        # get the width necessary for each column
        for i in range(self.__columns):
            # number of characters in column of i of header, each body row, and footer
            header_size = get_column_width(self.__header, i) if self.__header else 0
            body_size = max(get_column_width(row, i) for row in self.__body) if self.__body else 0
            footer_size = get_column_width(self.__footer, i) if self.__footer else 0
            min_text_width = max(header_size, body_size, footer_size, self.__decimal_widths[i])
            # get the max and add 2 for padding each side with a space depending on cell padding
            column_widths.append(min_text_width + self.__cell_padding * 2)
        return column_widths

    def __calculate_decimal_widths_and_positions(self) -> tuple[list[int], list[int]]:
        """Calculate the positions of the decimal points for decimal alignment.

        Returns:
            A tuple of the widths of the decimal numbers in each column
            and the positions of the decimal points in each column
        """
        decimal_widths: list[int] = [0] * self.__columns
        decimal_positions: list[int] = [0] * self.__columns
        for i in range(self.__columns):
            # skip if the column is not decimal aligned
            if self.__number_alignments[i] != Alignment.DECIMAL:
                continue
            # list all values in the i-th column of header, body, and footer
            values = [str(self.__header[i])] if self.__header else []
            values += [str(row[i]) for row in self.__body] if self.__body else []
            values += [str(self.__footer[i])] if self.__footer else []
            # filter out values that are not numbers and split at the decimal point
            split_values = [
                self.__split_decimal(value) for value in values if self.__is_number(value)
            ]
            # skip if there are no decimal values
            if len(split_values) == 0:
                continue
            # get the max number of digits before and after the decimal point
            max_before_decimal = max(self.__str_width(parts[0]) for parts in split_values)
            max_after_decimal = max(self.__str_width(parts[1]) for parts in split_values)
            # add 1 for the decimal point if there are any decimal point values
            has_decimal = any(self.__is_number(value) and "." in value for value in values)
            # store the total width of the decimal numbers in the column
            decimal_widths[i] = max_before_decimal + max_after_decimal + int(has_decimal)
            # store the max digits before the decimal point for decimal alignment
            decimal_positions[i] = max_before_decimal
        return decimal_widths, decimal_positions

    def __calculate_column_widths(
        self, user_column_widths: Sequence[int | None] | None
    ) -> list[int]:
        """Calculate the width of each column in the table based on the cell values and provided column widths.

        Args:
            user_column_widths: The user specified column widths

        Returns:
            The width of each column in the table
        """
        column_widths = self.__auto_column_widths()
        if user_column_widths:
            # check that the right number of columns were specified
            if len(user_column_widths) != self.__columns:
                raise ColumnWidthsCountMismatchError(user_column_widths, self.__columns)
            # check that each column is at least as large as the minimum size
            for i in range(len(user_column_widths)):
                option = user_column_widths[i]
                minimum = column_widths[i]
                if option is None:
                    option = minimum
                elif option < 0:
                    raise InvalidColumnWidthError(i, option)
                elif option < minimum:
                    raise ColumnWidthTooSmallError(i, option, minimum)
                column_widths[i] = option
        return column_widths

    def __fix_rows_beginning_with_merge(self) -> None:
        """Fix rows that begin with Merge.LEFT by replacing the cell with an empty string."""
        if self.__body:
            for row_index, row in enumerate(self.__body):
                if row and row[0] == Merge.LEFT:
                    self.__body[row_index][0] = ""
        if self.__header and self.__header[0] == Merge.LEFT:
            self.__header[0] = ""
        if self.__footer and self.__footer[0] == Merge.LEFT:
            self.__footer[0] = ""

    def __pad(self, cell_value: SupportsStr, width: int, col_index: int) -> str:
        """Pad a string of text to a given width with specified alignment

        Args:
            cell_value: The text in the cell to pad
            width: The width in characters to pad to
            col_index: The index of the column

        Returns:
            The padded text
        """
        alignment = self.__alignments[col_index]
        text = str(cell_value)
        # set alignment for numeric values
        if self.__is_number(text):
            # if the number alignment is decimal, pad such that the decimal point
            # is aligned to the column's decimal position and use the default alignment
            if self.__number_alignments[col_index] == Alignment.DECIMAL:
                decimal_position = self.__decimal_positions[col_index]
                decimal_max_width = self.__decimal_widths[col_index]
                text_before_decimal = self.__split_decimal(text)[0]
                before = " " * (decimal_position - self.__str_width(text_before_decimal))
                after = " " * (decimal_max_width - self.__str_width(text) - len(before))
                text = f"{before}{text}{after}"
            # otherwise use the number alignment as the alignment for the cell
            else:
                alignment = self.__number_alignments[col_index]
        # add minimum cell padding around the text
        padding = " " * self.__cell_padding
        padded_text = f"{padding}{text}{padding}"
        text_width = self.__str_width(padded_text)
        # pad the text based on the alignment
        if alignment == Alignment.LEFT:
            # pad with spaces on the end
            return padded_text + (" " * (width - text_width))
        elif alignment in (Alignment.CENTER, Alignment.DECIMAL):
            # pad with spaces, half on each side
            before = " " * floor((width - text_width) / 2)
            after = " " * ceil((width - text_width) / 2)
            return before + padded_text + after
        elif alignment == Alignment.RIGHT:
            # pad with spaces at the beginning
            return (" " * (width - text_width)) + padded_text
        raise InvalidAlignmentError(alignment)

    def __wrap_long_lines_in_merged_cells(
        self, row: Sequence[SupportsStr], column_separator: str
    ) -> list[SupportsStr]:
        """Wrap long lines in merged cells to the width of the merged cell

        Args:
            row: The row to wrap cells in
            column_separator: The column separator between cells

        Returns:
            The row with long lines wrapped
        """
        wrapped_row: list[SupportsStr] = []
        for col_index, cell in enumerate(row):
            if cell is Merge.LEFT:
                wrapped_row.append(cell)
                continue
            merged_width = self.__column_widths[col_index]
            # if the columns to the right are Merge.LEFT, add their width to the padding
            for other_col_index in range(col_index + 1, self.__columns):
                if row[other_col_index] is not Merge.LEFT:
                    break
                merged_width += self.__column_widths[other_col_index] + len(column_separator)
            cell = str(cell)
            # if the text is too wide, wrap it
            inner_cell_width = merged_width - self.__cell_padding * 2
            if self.__widest_line(cell) > inner_cell_width:
                cell = textwrap.fill(cell, inner_cell_width)
            # add the wrapped cell to the row
            wrapped_row.append(cell)
        return wrapped_row

    def __row_to_ascii(
        self,
        left_edge: str,
        heading_col_sep: str,
        column_separator: str,
        right_edge: str,
        filler: str | Sequence[SupportsStr],
        previous_content_row: Sequence[SupportsStr] | None = None,
        next_content_row: Sequence[SupportsStr] | None = None,
        top_tee: str | None = None,
        bottom_tee: str | None = None,
        heading_col_top_tee: str | None = None,
        heading_col_bottom_tee: str | None = None,
    ) -> str:
        """Assembles a line of text in the ascii table

        Returns:
            The line in the ascii table
        """
        output = ""
        # wrap long lines in merged cells
        if isinstance(filler, list):
            filler = self.__wrap_long_lines_in_merged_cells(filler, column_separator)
        # find the maximum number of lines a single cell in the column has (minimum of 1)
        num_lines = max(len(str(cell).splitlines()) for cell in filler) or 1
        # repeat for each line of text in the cell
        for line_index in range(num_lines):
            output += self.__line_in_row_to_ascii(
                line_index=line_index,
                left_edge=left_edge,
                heading_col_sep=heading_col_sep,
                column_separator=column_separator,
                right_edge=right_edge,
                filler=filler,
                previous_content_row=previous_content_row,
                next_content_row=next_content_row,
                top_tee=top_tee,
                bottom_tee=bottom_tee,
                heading_col_top_tee=heading_col_top_tee,
                heading_col_bottom_tee=heading_col_bottom_tee,
            )
        # don't use separation row if it's only space
        if isinstance(filler, str) and output.strip() == "":
            output = ""
        return output

    def __line_in_row_to_ascii(
        self,
        line_index: int,
        left_edge: str,
        heading_col_sep: str,
        column_separator: str,
        right_edge: str,
        filler: str | Sequence[SupportsStr],
        previous_content_row: Sequence[SupportsStr] | None = None,
        next_content_row: Sequence[SupportsStr] | None = None,
        top_tee: str | None = None,
        bottom_tee: str | None = None,
        heading_col_top_tee: str | None = None,
        heading_col_bottom_tee: str | None = None,
    ) -> str:
        """Assembles a line of text in the ascii table

        Returns:
            The line in the ascii table
        """
        output = left_edge
        # add columns
        for col_index in range(self.__columns):
            output += self.__line_in_cell_column_to_ascii(
                line_index=line_index,
                col_index=col_index,
                heading_col_sep=heading_col_sep,
                column_separator=column_separator,
                right_edge=right_edge,
                filler=filler,
                previous_content_row=previous_content_row,
                next_content_row=next_content_row,
                top_tee=top_tee,
                bottom_tee=bottom_tee,
                heading_col_top_tee=heading_col_top_tee,
                heading_col_bottom_tee=heading_col_bottom_tee,
            )
        output += "\n"
        return output

    def __line_in_cell_column_to_ascii(
        self,
        line_index: int,
        col_index: int,
        heading_col_sep: str,
        column_separator: str,
        right_edge: str,
        filler: str | Sequence[SupportsStr],
        previous_content_row: Sequence[SupportsStr] | None = None,
        next_content_row: Sequence[SupportsStr] | None = None,
        top_tee: str | None = None,
        bottom_tee: str | None = None,
        heading_col_top_tee: str | None = None,
        heading_col_bottom_tee: str | None = None,
    ) -> str:
        """Assembles a column of text in the ascii table

        Returns:
            The column in the ascii table
        """
        output = ""
        col_content = (
            # if filler is a separator character, repeat it for the full width of the column
            filler * self.__column_widths[col_index]
            if isinstance(filler, str)
            # otherwise, use the text from the corresponding column in the filler list
            else self.__get_padded_cell_line_content(
                line_index=line_index,
                col_index=col_index,
                column_separator=column_separator,
                filler=filler,
            )
        )
        output += col_content
        # check for merged cells
        next_value = prev_row_next_value = next_row_next_value = None
        if col_index < self.__columns - 1:
            next_value = filler[col_index + 1] if isinstance(filler, list) else None
            prev_row_next_value = (
                previous_content_row[col_index + 1] if previous_content_row else None
            )
            next_row_next_value = next_content_row[col_index + 1] if next_content_row else None
        # column separator
        sep = column_separator
        # handle separators between rows when previous or next row is a merged cell
        if top_tee and prev_row_next_value is Merge.LEFT:
            sep = top_tee
        if bottom_tee and next_row_next_value is Merge.LEFT:
            sep = bottom_tee
        if (
            isinstance(filler, str)
            and prev_row_next_value in (Merge.LEFT, None)
            and next_row_next_value in (Merge.LEFT, None)
        ):
            sep = filler
        # use column heading if first or last column option is specified
        if (col_index == 0 and self.__first_col_heading) or (
            col_index == self.__columns - 2 and self.__last_col_heading
        ):
            sep = heading_col_sep
            # handle separators between rows when previous or next row is a merged cell
            if heading_col_top_tee and prev_row_next_value is Merge.LEFT:
                sep = heading_col_top_tee
            if heading_col_bottom_tee and next_row_next_value is Merge.LEFT:
                sep = heading_col_bottom_tee
        # replace last separator with symbol for edge of the row
        elif col_index == self.__columns - 1:
            sep = right_edge
        # if this is cell contents and the next column is Merge.LEFT, don't add a separator
        if next_value is Merge.LEFT:
            sep = ""
        return output + sep

    def __get_padded_cell_line_content(
        self, line_index: int, col_index: int, column_separator: str, filler: Sequence[SupportsStr]
    ) -> str:
        # If this is a merge cell, merge with the previous column
        if filler[col_index] is Merge.LEFT:
            return ""
        # get the text of the current line in the cell
        # if there are fewer lines in the current cell than others, empty string is used
        col_lines = str(filler[col_index]).splitlines()
        col_content = col_lines[line_index] if line_index < len(col_lines) else ""
        pad_width = self.__column_widths[col_index]
        # if the columns to the right are Merge.LEFT, add their width to the padding
        for other_col_index in range(col_index + 1, self.__columns):
            if filler[other_col_index] is not Merge.LEFT:
                break
            pad_width += self.__column_widths[other_col_index] + len(column_separator)
        # pad the text to the width of the column using the alignment
        return self.__pad(
            cell_value=col_content,
            width=pad_width,
            col_index=col_index,
        )

    def __top_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table

        Returns:
            The top edge of the ascii table
        """
        first_row = self.__body[0] if self.__body else None
        first_row = self.__header if self.__header else first_row
        return self.__row_to_ascii(
            left_edge=self.__style.top_left_corner,
            heading_col_sep=self.__style.heading_col_top_tee,
            column_separator=self.__style.top_tee,
            right_edge=self.__style.top_right_corner,
            filler=self.__style.top_and_bottom_edge,
            next_content_row=first_row,
            top_tee=self.__style.col_row_top_tee,
            bottom_tee=self.__style.top_and_bottom_edge,
            heading_col_top_tee=self.__style.heading_col_top_tee,
            heading_col_bottom_tee=self.__style.top_and_bottom_edge,
        )

    def __bottom_edge_to_ascii(self) -> str:
        """Assembles the bottom edge of the ascii table

        Returns:
            The bottom edge of the ascii table
        """
        last_row = self.__body[-1] if self.__body else None
        last_row = self.__footer if self.__footer else last_row
        return self.__row_to_ascii(
            left_edge=self.__style.bottom_left_corner,
            heading_col_sep=self.__style.heading_col_bottom_tee,
            column_separator=self.__style.bottom_tee,
            right_edge=self.__style.bottom_right_corner,
            filler=self.__style.top_and_bottom_edge,
            previous_content_row=last_row,
            top_tee=self.__style.top_and_bottom_edge,
            bottom_tee=self.__style.col_row_bottom_tee,
            heading_col_top_tee=self.__style.top_and_bottom_edge,
            heading_col_bottom_tee=self.__style.heading_col_bottom_tee,
        )

    def __content_row_to_ascii(self, row: Sequence[SupportsStr]) -> str:
        """Assembles a row of cell values into a single line of the ascii table

        Returns:
            The row of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.left_and_right_edge,
            heading_col_sep=self.__style.heading_col_sep,
            column_separator=self.__style.col_sep,
            right_edge=self.__style.left_and_right_edge,
            filler=row,
        )

    def __heading_sep_to_ascii(
        self,
        previous_content_row: Sequence[SupportsStr] | None = None,
        next_content_row: Sequence[SupportsStr] | None = None,
    ) -> str:
        """Assembles the separator below the header or above footer of the ascii table

        Returns:
            The separator line
        """
        return self.__row_to_ascii(
            left_edge=self.__style.heading_row_left_tee,
            heading_col_sep=self.__style.heading_col_heading_row_cross,
            column_separator=self.__style.heading_row_cross,
            right_edge=self.__style.heading_row_right_tee,
            filler=self.__style.heading_row_sep,
            previous_content_row=previous_content_row,
            next_content_row=next_content_row,
            top_tee=self.__style.heading_row_top_tee,
            bottom_tee=self.__style.heading_row_bottom_tee,
            heading_col_top_tee=self.__style.heading_col_heading_row_top_tee,
            heading_col_bottom_tee=self.__style.heading_col_heading_row_bottom_tee,
        )

    def __body_to_ascii(self, body: Sequence[Sequence[SupportsStr]]) -> str:
        """Assembles the body of the ascii table

        Returns:
            The body of the ascii table
        """
        # first content row
        output = self.__content_row_to_ascii(body[0]) if len(body) else ""
        for row_index, row in enumerate(body[1:], 1):
            # separator between rows
            output += self.__row_to_ascii(
                left_edge=self.__style.row_left_tee,
                heading_col_sep=self.__style.heading_col_row_cross,
                column_separator=self.__style.col_row_cross,
                right_edge=self.__style.row_right_tee,
                filler=self.__style.row_sep,
                previous_content_row=body[row_index - 1],
                next_content_row=row,
                top_tee=self.__style.col_row_top_tee,
                bottom_tee=self.__style.col_row_bottom_tee,
                heading_col_top_tee=self.__style.heading_col_body_row_top_tee,
                heading_col_bottom_tee=self.__style.heading_col_body_row_bottom_tee,
            )
            # content row
            output += self.__content_row_to_ascii(row)
        return output

    def __str_width(self, text: str) -> int:
        """
        Returns the width of the string in characters for the purposes of monospace
        formatting. This is usually the same as the length of the string, but can be
        different for double-width characters (East Asian Wide and East Asian Fullwidth)
        or zero-width characters (combining characters, zero-width space, etc.)

        Args:
            text: The text to measure

        Returns:
            The width of the string in characters
        """
        width = wcswidth(text) if self.__use_wcwidth else -1
        # if use_wcwidth is False or wcswidth fails, fall back to len
        return width if width >= 0 else len(text)

    @staticmethod
    def __is_number(text: str) -> bool:
        """Returns True if the string is a number, with or without a decimal point"""
        return text.replace(".", "", 1).isdecimal()

    @staticmethod
    def __split_decimal(text: str) -> tuple[str, str]:
        """Splits a string into a tuple of the integer and decimal parts"""
        if "." in text:
            before, after = text.split(".", 1)
            return before, after
        return text, ""

    def to_ascii(self) -> str:
        """Generates a formatted ASCII table

        Returns:
            The generated ASCII table
        """
        # top row of table
        table = self.__top_edge_to_ascii()
        # add table header
        if self.__header:
            table += self.__content_row_to_ascii(self.__header)
            table += self.__heading_sep_to_ascii(
                previous_content_row=self.__header,
                next_content_row=self.__body[0] if self.__body else None,
            )
        # add table body
        if self.__body:
            table += self.__body_to_ascii(self.__body)
        # add table footer
        if self.__footer:
            table += self.__heading_sep_to_ascii(
                previous_content_row=self.__body[-1] if self.__body else None,
                next_content_row=self.__footer,
            )
            table += self.__content_row_to_ascii(self.__footer)
        # bottom row of table
        table += self.__bottom_edge_to_ascii()
        # reurn ascii table
        return table.strip("\n")


def table2ascii(
    header: Sequence[SupportsStr] | None = None,
    body: Sequence[Sequence[SupportsStr]] | None = None,
    footer: Sequence[SupportsStr] | None = None,
    *,
    first_col_heading: bool = False,
    last_col_heading: bool = False,
    column_widths: Sequence[int | None] | None = None,
    alignments: Sequence[Alignment] | Alignment | None = None,
    number_alignments: Sequence[Alignment] | Alignment | None = None,
    cell_padding: int = 1,
    style: TableStyle = PresetStyle.double_thin_compact,
    use_wcwidth: bool = True,
) -> str:
    """Convert a 2D Python table to ASCII text

    Args:
        header (:data:`Optional <typing.Optional>`\ [:class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]]):
            List of column values in the table's header row. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a header row.
        body (:data:`Optional <typing.Optional>`\ [:class:`Sequence <collections.abc.Sequence>`\ [:class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]]]):
            2-dimensional list of values in the table's body. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a body.
        footer (:data:`Optional <typing.Optional>`\ [:class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]]):
            List of column values in the table's footer row. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a footer row.
        first_col_heading: Whether to add a header column separator after the first column.
            Defaults to :py:obj:`False`.
        last_col_heading: Whether to add a header column separator before the last column.
            Defaults to :py:obj:`False`.
        column_widths (:data:`Optional <typing.Optional>`\ [:class:`Sequence <collections.abc.Sequence>`\ [:data:`Optional <typing.Optional>`\ [:class:`int`]]]):
            List of widths in characters for each column. Any value of :py:obj:`None`
            indicates that the column width should be determined automatically. If :py:obj:`None`
            is passed instead of a :class:`~collections.abc.Sequence`, all columns will be automatically
            sized. Defaults to :py:obj:`None`.
        alignments: List of alignments for each column
            (ex. [:attr:`Alignment.LEFT`, :attr:`Alignment.CENTER`, :attr:`Alignment.RIGHT`, :attr:`Alignment.DECIMAL`])
            or a single alignment to apply to all columns (ex. :attr:`Alignment.LEFT`).
            If not specified or set to :py:obj:`None`, all columns will be center-aligned.
            Defaults to :py:obj:`None`.

            .. versionchanged:: 1.1.0
                ``alignments`` can now also be specified as a single :class:`Alignment` value to apply to all columns.
        number_alignments: List of alignments for numeric values in each column or a single alignment
            to apply to all columns. This argument can be used to override the alignment of numbers and
            is ignored for non-numeric values. Numeric values include integers, floats, and strings containing only
            :meth:`decimal <str.isdecimal>` characters and at most one decimal point.
            If not specified or set to :py:obj:`None`, numbers will be aligned based on the ``alignments`` argument.
            Defaults to :py:obj:`None`.

            .. versionadded:: 1.1.0
        cell_padding: The minimum number of spaces to add between the cell content and the column
            separator. If set to ``0``, the cell content will be flush against the column separator.
            Defaults to ``1``.
        style: Table style to use for styling (preset styles can be imported).
            Defaults to :ref:`PresetStyle.double_thin_compact`.
        use_wcwidth: Whether to use :func:`wcwidth.wcswidth` to determine the width of each cell instead of
            :func:`len`. The :func:`~wcwidth.wcswidth` function takes into account double-width characters
            (East Asian Wide and East Asian Fullwidth) and zero-width characters (combining characters,
            zero-width space, etc.), whereas :func:`len` determines the width solely based on the number of
            characters in the string. Defaults to :py:obj:`True`.

            .. versionadded:: 1.0.0

    Returns:
        The generated ASCII table
    """
    return TableToAscii(
        header,
        body,
        footer,
        Options(
            first_col_heading=first_col_heading,
            last_col_heading=last_col_heading,
            column_widths=column_widths,
            alignments=alignments,
            number_alignments=number_alignments,
            cell_padding=cell_padding,
            style=style,
            use_wcwidth=use_wcwidth,
        ),
    ).to_ascii()
