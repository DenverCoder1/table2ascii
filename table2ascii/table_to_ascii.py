from __future__ import annotations

from math import ceil, floor

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
        """
        Validate arguments and initialize fields

        Args:
            header: The values in the header of the table
            body: The rows of values in the body of the table
            footer: The values in the footer of the table
            options: The options for the table
        """
        # initialize fields
        self._header = header
        self._body = body
        self._footer = footer
        self._style = options.style
        self._first_col_heading = options.first_col_heading
        self._last_col_heading = options.last_col_heading
        self._cell_padding = options.cell_padding

        # check if footer has a different number of columns
        if footer and len(footer) != self.column_count:
            raise ValueError("Footer must have the same number of columns as the other rows")
        # check if any rows in body have a different number of columns
        if body and any(len(row) != self.column_count for row in body):
            raise ValueError(
                "All rows in body must have the same number of columns as the other rows"
            )

        # calculate or use given column widths
        self._column_widths = self.auto_column_widths()
        if options.column_widths:
            # check that the right number of columns were specified
            if len(options.column_widths) != self.column_count:
                raise ValueError("Length of `column_widths` list must equal the number of columns")
            # check that each column is at least as large as the minimum size
            for i in range(len(options.column_widths)):
                option = options.column_widths[i]
                minimum = self._column_widths[i]
                if option is None:
                    option = minimum
                elif option < minimum:
                    raise ValueError(
                        f"The value at index {i} of `column_widths` is {option} which is less than the minimum {minimum}."
                    )
                self._column_widths[i] = option

        self._alignments = options.alignments or [Alignment.CENTER] * self.column_count

        # check if alignments specified have a different number of columns
        if options.alignments and len(options.alignments) != self.column_count:
            raise ValueError("Length of `alignments` list must equal the number of columns")

        # check if the cell padding is valid
        if self._cell_padding < 0:
            raise ValueError("Cell padding must be greater than or equal to 0")

    @property
    def column_count(self) -> int:
        """
        Get the number of columns in the table based on the
        provided header, footer, and body lists.

        Returns:
            The number of columns in the table
        """
        if self._header:
            return len(self._header)
        if self._footer:
            return len(self._footer)
        if self._body and len(self._body) > 0:
            return len(self._body[0])
        return 0

    @property
    def column_widths(self) -> list[int]:
        """
        Get the column widths of the table

        Returns:
            The column widths of the table
        """
        return self._column_widths

    @property
    def alignments(self) -> list[Alignment]:
        """
        Get the alignments of the table

        Returns:
            The alignments of the table
        """
        return self._alignments

    def auto_column_widths(self) -> list[int]:
        """
        Get the minimum number of characters needed for the values in
        each column in the table with 1 space of padding on each side.

        Returns:
            The minimum number of characters needed for each column
        """

        def widest_line(value: SupportsStr) -> int:
            """Returns the width of the longest line in a multi-line string"""
            text = str(value)
            return max(len(line) for line in text.splitlines()) if len(text) else 0

        column_widths: list[int] = []
        # get the width necessary for each column
        for i in range(self.column_count):
            # number of characters in column of i of header, each body row, and footer
            header_size = widest_line(self._header[i]) if self._header else 0
            body_size = max(widest_line(row[i]) for row in self._body) if self._body else 0
            footer_size = widest_line(self._footer[i]) if self._footer else 0
            # get the max and add 2 for padding each side with a space depending on cell padding
            column_widths.append(max(header_size, body_size, footer_size) + self._cell_padding * 2)
        return column_widths

    def pad(self, cell_value: SupportsStr, *, width: int, alignment: Alignment) -> str:
        """
        Pad a string of text to a given width with specified alignment

        Args:
            cell_value: The text in the cell to pad
            width: The width in characters to pad to
            alignment: The alignment to use

        Returns:
            The padded text
        """
        text = str(cell_value)
        padding = " " * self._cell_padding
        padded_text = f"{padding}{text}{padding}"
        if alignment == Alignment.LEFT:
            # pad with spaces on the end
            return padded_text + (" " * (width - len(padded_text)))
        if alignment == Alignment.CENTER:
            # pad with spaces, half on each side
            before = " " * floor((width - len(padded_text)) / 2)
            after = " " * ceil((width - len(padded_text)) / 2)
            return before + padded_text + after
        if alignment == Alignment.RIGHT:
            # pad with spaces at the beginning
            return (" " * (width - len(padded_text))) + padded_text
        raise ValueError(f"The value '{alignment}' is not valid for alignment.")

    def row_to_ascii(
        self,
        *,
        left_edge: str,
        heading_col_sep: str,
        column_separator: str,
        right_edge: str,
        filler: str | list[SupportsStr],
    ) -> str:
        """
        Assembles a line of text in the ascii table

        Returns:
            The line in the ascii table
        """
        output = ""
        # find the maximum number of lines a single cell in the column has (minimum of 1)
        num_lines = max(len(str(cell).splitlines()) for cell in filler) or 1
        # repeat for each line of text in the cell
        for line_index in range(num_lines):
            # left edge of the row
            output += left_edge
            # add columns
            for col_index in range(self.column_count):
                # content between separators
                col_content = ""
                # if filler is a separator character, repeat it for the full width of the column
                if isinstance(filler, str):
                    col_content = filler * self._column_widths[col_index]
                # otherwise, use the text from the corresponding column in the filler list
                else:
                    # get the text of the current line in the cell
                    # if there are fewer lines in the current cell than others, empty string is used
                    col_lines = str(filler[col_index]).splitlines()
                    if line_index < len(col_lines):
                        col_content = col_lines[line_index]
                    # pad the text to the width of the column using the alignment
                    col_content = self.pad(
                        col_content,
                        width=self._column_widths[col_index],
                        alignment=self._alignments[col_index],
                    )
                output += col_content
                # column separator
                sep = column_separator
                if col_index == 0 and self._first_col_heading:
                    # use column heading if first column option is specified
                    sep = heading_col_sep
                elif col_index == self.column_count - 2 and self._last_col_heading:
                    # use column heading if last column option is specified
                    sep = heading_col_sep
                elif col_index == self.column_count - 1:
                    # replace last separator with symbol for edge of the row
                    sep = right_edge
                output += sep
            output += "\n"
            # don't use separation row if it's only space
            if isinstance(filler, str) and output.strip() == "":
                output = ""
        return output

    def top_edge_to_ascii(self) -> str:
        """
        Assembles the top edge of the ascii table

        Returns:
            The top edge of the ascii table
        """
        return self.row_to_ascii(
            left_edge=self._style.top_left_corner,
            heading_col_sep=self._style.heading_col_top_tee,
            column_separator=self._style.top_tee,
            right_edge=self._style.top_right_corner,
            filler=self._style.top_and_bottom_edge,
        )

    def bottom_edge_to_ascii(self) -> str:
        """
        Assembles the bottom edge of the ascii table

        Returns:
            The bottom edge of the ascii table
        """
        return self.row_to_ascii(
            left_edge=self._style.bottom_left_corner,
            heading_col_sep=self._style.heading_col_bottom_tee,
            column_separator=self._style.bottom_tee,
            right_edge=self._style.bottom_right_corner,
            filler=self._style.top_and_bottom_edge,
        )

    def heading_row_to_ascii(self, row: list[SupportsStr]) -> str:
        """
        Assembles the header or footer row line of the ascii table

        Returns:
            The header or footer row line of the ascii table
        """
        return self.row_to_ascii(
            left_edge=self._style.left_and_right_edge,
            heading_col_sep=self._style.heading_col_sep,
            column_separator=self._style.col_sep,
            right_edge=self._style.left_and_right_edge,
            filler=row,
        )

    def heading_sep_to_ascii(self) -> str:
        """
        Assembles the separator below the header or above footer of the ascii table

        Returns:
            The separator line
        """
        return self.row_to_ascii(
            left_edge=self._style.heading_row_left_tee,
            heading_col_sep=self._style.heading_col_heading_row_cross,
            column_separator=self._style.heading_row_cross,
            right_edge=self._style.heading_row_right_tee,
            filler=self._style.heading_row_sep,
        )

    def body_to_ascii(self, body: list[list[SupportsStr]]) -> str:
        """
        Assembles the body of the ascii table

        Returns:
            The body of the ascii table
        """
        separation_row = self.row_to_ascii(
            left_edge=self._style.row_left_tee,
            heading_col_sep=self._style.heading_col_row_cross,
            column_separator=self._style.col_row_cross,
            right_edge=self._style.row_right_tee,
            filler=self._style.row_sep,
        )
        return separation_row.join(
            self.row_to_ascii(
                left_edge=self._style.left_and_right_edge,
                heading_col_sep=self._style.heading_col_sep,
                column_separator=self._style.col_sep,
                right_edge=self._style.left_and_right_edge,
                filler=row,
            )
            for row in body
        )

    def to_ascii(self) -> str:
        """
        Generates a formatted ASCII table

        Returns:
            The generated ASCII table
        """
        # top row of table
        table = self.top_edge_to_ascii()
        # add table header
        if self._header:
            table += self.heading_row_to_ascii(self._header)
            table += self.heading_sep_to_ascii()
        # add table body
        if self._body:
            table += self.body_to_ascii(self._body)
        # add table footer
        if self._footer:
            table += self.heading_sep_to_ascii()
            table += self.heading_row_to_ascii(self._footer)
        # bottom row of table
        table += self.bottom_edge_to_ascii()
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
) -> str:
    """
    Convert a 2D Python table to ASCII text

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
            is passed instead of a :py:obj:`~typing.List`, all columns will be automatically sized.
            Defaults to :py:obj:`None`.
        alignments: List of alignments for each column
            (ex. ``[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]``). If not specified or set to
            :py:obj:`None`, all columns will be center-aligned. Defaults to :py:obj:`None`.
        cell_padding: The minimum number of spaces to add between the cell content and the column
            separator. If set to ``0``, the cell content will be flush against the column separator.
            Defaults to ``1``.
        style: Table style to use for styling (preset styles can be imported).
            Defaults to :ref:`PresetStyle.double_thin_compact <PresetStyle.double_thin_compact>`.

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
        ),
    ).to_ascii()
