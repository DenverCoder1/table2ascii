from __future__ import annotations

from math import ceil, floor

from wcwidth import wcswidth

from .alignment import Alignment
from .annotations import SupportsStr
from .options import Options
from .preset_style import PresetStyle
from .table_style import TableStyle


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(
        self,
        header: list[SupportsStr] | None,
        body: list[list[SupportsStr]] | None,
        footer: list[SupportsStr] | None,
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
        self.__header = header
        self.__body = body
        self.__footer = footer
        self.__style = options.style
        self.__first_col_heading = options.first_col_heading
        self.__last_col_heading = options.last_col_heading
        self.__cell_padding = options.cell_padding
        self.__use_wcwidth = options.use_wcwidth

        # calculate number of columns
        self.__columns = self.__count_columns()

        # check if footer has a different number of columns
        if footer and len(footer) != self.__columns:
            raise ValueError("Footer must have the same number of columns as the other rows")
        # check if any rows in body have a different number of columns
        if body and any(len(row) != self.__columns for row in body):
            raise ValueError(
                "All rows in body must have the same number of columns as the other rows"
            )

        # calculate or use given column widths
        self.__column_widths = self.__calculate_column_widths(options.column_widths)

        self.__alignments = options.alignments or [Alignment.CENTER] * self.__columns

        # check if alignments specified have a different number of columns
        if options.alignments and len(options.alignments) != self.__columns:
            raise ValueError("Length of `alignments` list must equal the number of columns")

        # check if the cell padding is valid
        if self.__cell_padding < 0:
            raise ValueError("Cell padding must be greater than or equal to 0")

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

    def __auto_column_widths(self) -> list[int]:
        """Get the minimum number of characters needed for the values in each column in the table
        with 1 space of padding on each side.

        Returns:
            The minimum number of characters needed for each column
        """

        def widest_line(value: SupportsStr) -> int:
            """Returns the width of the longest line in a multi-line string"""
            text = str(value)
            return max(self.__str_width(line) for line in text.splitlines()) if len(text) else 0

        column_widths = []
        # get the width necessary for each column
        for i in range(self.__columns):
            # number of characters in column of i of header, each body row, and footer
            header_size = widest_line(self.__header[i]) if self.__header else 0
            body_size = max(widest_line(row[i]) for row in self.__body) if self.__body else 0
            footer_size = widest_line(self.__footer[i]) if self.__footer else 0
            # get the max and add 2 for padding each side with a space depending on cell padding
            column_widths.append(max(header_size, body_size, footer_size) + self.__cell_padding * 2)
        return column_widths

    def __calculate_column_widths(self, user_column_widths: list[int | None] | None) -> list[int]:
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
                raise ValueError("Length of `column_widths` list must equal the number of columns")
            # check that each column is at least as large as the minimum size
            for i in range(len(user_column_widths)):
                option = user_column_widths[i]
                minimum = column_widths[i]
                if option is None:
                    option = minimum
                elif option < minimum:
                    raise ValueError(
                        f"The value at index {i} of `column_widths` is {option} which is less than the minimum {minimum}."
                    )
                column_widths[i] = option
        return column_widths

    def __pad(self, cell_value: SupportsStr, width: int, alignment: Alignment) -> str:
        """Pad a string of text to a given width with specified alignment

        Args:
            cell_value: The text in the cell to pad
            width: The width in characters to pad to
            alignment: The alignment to use

        Returns:
            The padded text
        """
        text = str(cell_value)
        padding = " " * self.__cell_padding
        padded_text = f"{padding}{text}{padding}"
        text_width = self.__str_width(padded_text)
        if alignment == Alignment.LEFT:
            # pad with spaces on the end
            return padded_text + (" " * (width - text_width))
        if alignment == Alignment.CENTER:
            # pad with spaces, half on each side
            before = " " * floor((width - text_width) / 2)
            after = " " * ceil((width - text_width) / 2)
            return before + padded_text + after
        if alignment == Alignment.RIGHT:
            # pad with spaces at the beginning
            return (" " * (width - text_width)) + padded_text
        raise ValueError(f"The value '{alignment}' is not valid for alignment.")

    def __row_to_ascii(
        self,
        left_edge: str,
        heading_col_sep: str,
        column_separator: str,
        right_edge: str,
        filler: str | list[SupportsStr],
    ) -> str:
        """Assembles a line of text in the ascii table

        Returns:
            The line in the ascii table
        """
        output = ""
        # find the maximum number of lines a single cell in the column has (minimum of 1)
        num_lines = max(len(str(cell).splitlines()) for cell in filler) or 1
        # repeat for each line of text in the cell
        for line_index in range(num_lines):
            output += self.__line_in_row_to_ascii(
                line_index,
                left_edge,
                heading_col_sep,
                column_separator,
                right_edge,
                filler,
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
        filler: str | list[SupportsStr],
    ) -> str:
        """Assembles a line of text in the ascii table

        Returns:
            The line in the ascii table
        """
        output = left_edge
        # add columns
        for col_index in range(self.__columns):
            output += self.__line_in_cell_column_to_ascii(
                line_index,
                col_index,
                heading_col_sep,
                column_separator,
                right_edge,
                filler,
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
        filler: str | list[SupportsStr],
    ) -> str:
        """Assembles a column of text in the ascii table

        Returns:
            The column in the ascii table
        """
        output = ""
        # content between separators
        col_content = ""
        # if filler is a separator character, repeat it for the full width of the column
        if isinstance(filler, str):
            col_content = filler * self.__column_widths[col_index]
        # otherwise, use the text from the corresponding column in the filler list
        else:
            # get the text of the current line in the cell
            # if there are fewer lines in the current cell than others, empty string is used
            col_lines = str(filler[col_index]).splitlines()
            if line_index < len(col_lines):
                col_content = col_lines[line_index]
            # pad the text to the width of the column using the alignment
            col_content = self.__pad(
                col_content,
                self.__column_widths[col_index],
                self.__alignments[col_index],
            )
        output += col_content
        # column separator
        sep = column_separator
        if col_index == 0 and self.__first_col_heading:
            # use column heading if first column option is specified
            sep = heading_col_sep
        elif col_index == self.__columns - 2 and self.__last_col_heading:
            # use column heading if last column option is specified
            sep = heading_col_sep
        elif col_index == self.__columns - 1:
            # replace last separator with symbol for edge of the row
            sep = right_edge
        return output + sep

    def __top_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table

        Returns:
            The top edge of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.top_left_corner,
            heading_col_sep=self.__style.heading_col_top_tee,
            column_separator=self.__style.top_tee,
            right_edge=self.__style.top_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __bottom_edge_to_ascii(self) -> str:
        """Assembles the bottom edge of the ascii table

        Returns:
            The bottom edge of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.bottom_left_corner,
            heading_col_sep=self.__style.heading_col_bottom_tee,
            column_separator=self.__style.bottom_tee,
            right_edge=self.__style.bottom_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __heading_row_to_ascii(self, row: list[SupportsStr]) -> str:
        """Assembles the header or footer row line of the ascii table

        Returns:
            The header or footer row line of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.left_and_right_edge,
            heading_col_sep=self.__style.heading_col_sep,
            column_separator=self.__style.col_sep,
            right_edge=self.__style.left_and_right_edge,
            filler=row,
        )

    def __heading_sep_to_ascii(self) -> str:
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
        )

    def __body_to_ascii(self, body: list[list[SupportsStr]]) -> str:
        """Assembles the body of the ascii table

        Returns:
            The body of the ascii table
        """
        separation_row = self.__row_to_ascii(
            left_edge=self.__style.row_left_tee,
            heading_col_sep=self.__style.heading_col_row_cross,
            column_separator=self.__style.col_row_cross,
            right_edge=self.__style.row_right_tee,
            filler=self.__style.row_sep,
        )
        return separation_row.join(
            self.__row_to_ascii(
                left_edge=self.__style.left_and_right_edge,
                heading_col_sep=self.__style.heading_col_sep,
                column_separator=self.__style.col_sep,
                right_edge=self.__style.left_and_right_edge,
                filler=row,
            )
            for row in body
        )

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

    def to_ascii(self) -> str:
        """Generates a formatted ASCII table

        Returns:
            The generated ASCII table
        """
        # top row of table
        table = self.__top_edge_to_ascii()
        # add table header
        if self.__header:
            table += self.__heading_row_to_ascii(self.__header)
            table += self.__heading_sep_to_ascii()
        # add table body
        if self.__body:
            table += self.__body_to_ascii(self.__body)
        # add table footer
        if self.__footer:
            table += self.__heading_sep_to_ascii()
            table += self.__heading_row_to_ascii(self.__footer)
        # bottom row of table
        table += self.__bottom_edge_to_ascii()
        # reurn ascii table
        return table.strip("\n")


def table2ascii(
    header: list[SupportsStr] | None = None,
    body: list[list[SupportsStr]] | None = None,
    footer: list[SupportsStr] | None = None,
    *,
    first_col_heading: bool = False,
    last_col_heading: bool = False,
    column_widths: list[int | None] | None = None,
    alignments: list[Alignment] | None = None,
    cell_padding: int = 1,
    style: TableStyle = PresetStyle.double_thin_compact,
    use_wcwidth: bool = True,
) -> str:
    """Convert a 2D Python table to ASCII text

    Args:
        header: List of column values in the table's header row. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a header row.
        body: 2-dimensional list of values in the table's body. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a body.
        footer: List of column values in the table's footer row. All values should be :class:`str`
            or support :class:`str` conversion. If not specified, the table will not have a footer row.
        first_col_heading: Whether to add a header column separator after the first column.
            Defaults to :py:obj:`False`.
        last_col_heading: Whether to add a header column separator before the last column.
            Defaults to :py:obj:`False`.
        column_widths: List of widths in characters for each column. Any value of :py:obj:`None`
            indicates that the column width should be determined automatically. If :py:obj:`None`
            is passed instead of a :class:`list`, all columns will be automatically sized.
            Defaults to :py:obj:`None`.
        alignments: List of alignments for each column
            (ex. ``[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]``). If not specified or set to
            :py:obj:`None`, all columns will be center-aligned. Defaults to :py:obj:`None`.
        cell_padding: The minimum number of spaces to add between the cell content and the column
            separator. If set to ``0``, the cell content will be flush against the column separator.
            Defaults to ``1``.
        style: Table style to use for styling (preset styles can be imported).
            Defaults to :ref:`PresetStyle.double_thin_compact <PresetStyle.double_thin_compact>`.
        use_wcwidth: Whether to use :func:`wcwidth.wcswidth` to determine the width of each cell instead of
            :func:`len`. The :func:`~wcwidth.wcswidth` function takes into account double-width characters
            (East Asian Wide and East Asian Fullwidth) and zero-width characters (combining characters,
            zero-width space, etc.), whereas :func:`len` determines the width solely based on the number of
            characters in the string. Defaults to :py:obj:`True`.

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
            cell_padding=cell_padding,
            style=style,
            use_wcwidth=use_wcwidth,
        ),
    ).to_ascii()
