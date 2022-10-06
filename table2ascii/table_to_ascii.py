from math import ceil, floor
from typing import Callable, List, Optional, Union

from .alignment import Alignment
from .annotations import SupportsStr
from .options import Options
from .preset_style import PresetStyle
from .table_style import TableStyle


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(
        self,
        header: Optional[List[SupportsStr]],
        body: Optional[List[List[SupportsStr]]],
        footer: Optional[List[SupportsStr]],
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
        self.__header = header
        self.__body = body
        self.__footer = footer
        self.__style = options.style
        self.__first_col_heading = options.first_col_heading
        self.__last_col_heading = options.last_col_heading

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
        self.__column_widths = self.__auto_column_widths()
        if options.column_widths:
            # check that the right number of columns were specified
            if len(options.column_widths) != self.__columns:
                raise ValueError("Length of `column_widths` list must equal the number of columns")
            # check that each column is at least as large as the minimum size
            for i in range(len(options.column_widths)):
                option = options.column_widths[i]
                minimum = self.__column_widths[i]
                if option is None:
                    option = minimum
                elif option < minimum:
                    raise ValueError(
                        f"The value at index {i} of `column_widths` is {option} which is less than the minimum {minimum}."
                    )
                self.__column_widths[i] = option

        self.__alignments = options.alignments or [Alignment.CENTER] * self.__columns

        # check if alignments specified have a different number of columns
        if options.alignments and len(options.alignments) != self.__columns:
            raise ValueError("Length of `alignments` list must equal the number of columns")

    def __count_columns(self) -> int:
        """
        Get the number of columns in the table based on the
        provided header, footer, and body lists.

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

    def __auto_column_widths(self) -> List[int]:
        """
        Get the minimum number of characters needed for the values in
        each column in the table with 1 space of padding on each side.

        Returns:
            The minimum number of characters needed for each column
        """

        def widest_line(text: str) -> int:
            """Returns the width of the longest line in a multi-line string"""
            return max(len(line) for line in text.splitlines()) if len(text) else 0

        column_widths = []
        # get the width necessary for each column
        for i in range(self.__columns):
            # col_widest returns the width of the widest line in the ith cell of a given list
            col_widest: Callable[[List[SupportsStr], int], int] = lambda row, i=i: widest_line(
                str(row[i])
            )
            # number of characters in column of i of header, each body row, and footer
            header_size = col_widest(self.__header) if self.__header else 0
            body_size = map(col_widest, self.__body) if self.__body else [0]
            footer_size = col_widest(self.__footer) if self.__footer else 0
            # get the max and add 2 for padding each side with a space
            column_widths.append(max(header_size, *body_size, footer_size) + 2)
        return column_widths

    def __pad(self, cell_value: SupportsStr, width: int, alignment: Alignment) -> str:
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
        if alignment == Alignment.LEFT:
            # pad with spaces on the end
            return f" {text} " + (" " * (width - len(text) - 2))
        if alignment == Alignment.CENTER:
            # pad with spaces, half on each side
            before = " " * floor((width - len(text) - 2) / 2)
            after = " " * ceil((width - len(text) - 2) / 2)
            return before + f" {text} " + after
        if alignment == Alignment.RIGHT:
            # pad with spaces at the beginning
            return (" " * (width - len(text) - 2)) + f" {text} "
        raise ValueError(f"The value '{alignment}' is not valid for alignment.")

    def __row_to_ascii(
        self,
        left_edge: str,
        heading_col_sep: str,
        column_seperator: str,
        right_edge: str,
        filler: Union[str, List],
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
            for col_index in range(self.__columns):
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
                # column seperator
                sep = column_seperator
                if col_index == 0 and self.__first_col_heading:
                    # use column heading if first column option is specified
                    sep = heading_col_sep
                elif col_index == self.__columns - 2 and self.__last_col_heading:
                    # use column heading if last column option is specified
                    sep = heading_col_sep
                elif col_index == self.__columns - 1:
                    # replace last seperator with symbol for edge of the row
                    sep = right_edge
                output += sep
            output += "\n"
            # don't use separation row if it's only space
            if isinstance(filler, str) and output.strip() == "":
                output = ""
        return output

    def __top_edge_to_ascii(self) -> str:
        """
        Assembles the top edge of the ascii table

        Returns:
            The top edge of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.top_left_corner,
            heading_col_sep=self.__style.heading_col_top_tee,
            column_seperator=self.__style.top_tee,
            right_edge=self.__style.top_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __bottom_edge_to_ascii(self) -> str:
        """
        Assembles the bottom edge of the ascii table

        Returns:
            The bottom edge of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.bottom_left_corner,
            heading_col_sep=self.__style.heading_col_bottom_tee,
            column_seperator=self.__style.bottom_tee,
            right_edge=self.__style.bottom_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __heading_row_to_ascii(self, row: List) -> str:
        """
        Assembles the header or footer row line of the ascii table

        Returns:
            The header or footer row line of the ascii table
        """
        return self.__row_to_ascii(
            left_edge=self.__style.left_and_right_edge,
            heading_col_sep=self.__style.heading_col_sep,
            column_seperator=self.__style.col_sep,
            right_edge=self.__style.left_and_right_edge,
            filler=row,
        )

    def __heading_sep_to_ascii(self) -> str:
        """
        Assembles the seperator below the header or above footer of the ascii table

        Returns:
            The seperator line
        """
        return self.__row_to_ascii(
            left_edge=self.__style.heading_row_left_tee,
            heading_col_sep=self.__style.heading_col_heading_row_cross,
            column_seperator=self.__style.heading_row_cross,
            right_edge=self.__style.heading_row_right_tee,
            filler=self.__style.heading_row_sep,
        )

    def __body_to_ascii(self, body: List[List[SupportsStr]]) -> str:
        """
        Assembles the body of the ascii table

        Returns:
            The body of the ascii table
        """
        separation_row = self.__row_to_ascii(
            left_edge=self.__style.row_left_tee,
            heading_col_sep=self.__style.heading_col_row_cross,
            column_seperator=self.__style.col_row_cross,
            right_edge=self.__style.row_right_tee,
            filler=self.__style.row_sep,
        )
        return separation_row.join(
            self.__row_to_ascii(
                left_edge=self.__style.left_and_right_edge,
                heading_col_sep=self.__style.heading_col_sep,
                column_seperator=self.__style.col_sep,
                right_edge=self.__style.left_and_right_edge,
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
    header: Optional[List[SupportsStr]] = None,
    body: Optional[List[List[SupportsStr]]] = None,
    footer: Optional[List[SupportsStr]] = None,
    *,
    first_col_heading: bool = False,
    last_col_heading: bool = False,
    column_widths: Optional[List[Optional[int]]] = None,
    alignments: Optional[List[Alignment]] = None,
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
            style=style,
        ),
    ).to_ascii()
