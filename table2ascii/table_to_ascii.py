from math import ceil, floor
from typing import List, Union

from .alignment import Alignment
from .options import Options


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(self, options: Options):
        """Validate arguments and initialize fields"""
        # initialize fields
        self.__header = options.header
        self.__body = options.body
        self.__footer = options.footer
        self.__style = options.style
        self.__first_col_heading = options.first_col_heading
        self.__last_col_heading = options.last_col_heading

        # calculate number of columns
        self.__columns = self.__count_columns()

        # check if footer has a different number of columns
        if options.footer and len(options.footer) != self.__columns:
            raise ValueError(
                "Footer must have the same number of columns as the other rows"
            )
        # check if any rows in body have a different number of columns
        if options.body and any(len(row) != self.__columns for row in options.body):
            raise ValueError(
                "All rows in body must have the same number of columns as the other rows"
            )

        # calculate or use given column widths
        self.__column_widths = options.column_widths or self.__auto_column_widths()

        # check if column widths specified have a different number of columns
        if options.column_widths and len(options.column_widths) != self.__columns:
            raise ValueError(
                "Length of `column_widths` list must equal the number of columns"
            )
        # check if column widths are not all at least 2
        if options.column_widths and min(options.column_widths) < 2:
            raise ValueError(
                "All values in `column_widths` must be greater than or equal to 2"
            )

        self.__alignments = options.alignments or [Alignment.CENTER] * self.__columns

        # check if alignments specified have a different number of columns
        if options.alignments and len(options.alignments) != self.__columns:
            raise ValueError(
                "Length of `alignments` list must equal the number of columns"
            )

    def __count_columns(self) -> int:
        """Get the number of columns in the table
        based on the provided header, footer, and body lists.
        """
        if self.__header:
            return len(self.__header)
        if self.__footer:
            return len(self.__footer)
        if self.__body and len(self.__body) > 0:
            return len(self.__body[0])
        return 0

    def __auto_column_widths(self) -> List[int]:
        """Get the minimum number of characters needed for the values
        in each column in the table with 1 space of padding on each side.
        """
        column_widths = []
        for i in range(self.__columns):
            # number of characters in column of i of header, each body row, and footer
            header_size = len(self.__header[i]) if self.__header else 0
            body_size = (
                map(lambda row, i=i: len(row[i]), self.__body) if self.__body else [0]
            )
            footer_size = len(self.__footer[i]) if self.__footer else 0
            # get the max and add 2 for padding each side with a space
            column_widths.append(max(header_size, *body_size, footer_size) + 2)
        return column_widths

    def __pad(self, text: str, width: int, alignment: Alignment):
        """Pad a string of text to a given width with specified alignment"""
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
        """Assembles a row of the ascii table"""
        # left edge of the row
        output = left_edge
        # add columns
        for i in range(self.__columns):
            # content between separators
            output += (
                # edge or row separator if filler is a specific character
                filler * self.__column_widths[i]
                if isinstance(filler, str)
                # otherwise, use the column content
                else self.__pad(
                    str(filler[i]), self.__column_widths[i], self.__alignments[i]
                )
            )
            # column seperator
            sep = column_seperator
            if i == 0 and self.__first_col_heading:
                # use column heading if first column option is specified
                sep = heading_col_sep
            elif i == self.__columns - 2 and self.__last_col_heading:
                # use column heading if last column option is specified
                sep = heading_col_sep
            elif i == self.__columns - 1:
                # replace last seperator with symbol for edge of the row
                sep = right_edge
            output += sep
        return output + "\n"

    def __top_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.top_left_corner,
            heading_col_sep=self.__style.heading_col_top_tee,
            column_seperator=self.__style.top_tee,
            right_edge=self.__style.top_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __bottom_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.bottom_left_corner,
            heading_col_sep=self.__style.heading_col_bottom_tee,
            column_seperator=self.__style.bottom_tee,
            right_edge=self.__style.bottom_right_corner,
            filler=self.__style.top_and_bottom_edge,
        )

    def __header_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.left_and_right_edge,
            heading_col_sep=self.__style.heading_col_sep,
            column_seperator=self.__style.middle_edge,
            right_edge=self.__style.left_and_right_edge,
            filler=self.__header,
        )

    def __footer_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.left_and_right_edge,
            heading_col_sep=self.__style.heading_col_sep,
            column_seperator=self.__style.middle_edge,
            right_edge=self.__style.left_and_right_edge,
            filler=self.__footer,
        )

    def __header_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.header_left_tee,
            heading_col_sep=self.__style.heading_col_header_cross,
            column_seperator=self.__style.header_row_cross,
            right_edge=self.__style.header_right_tee,
            filler=self.__style.header_row_sep,
        )

    def __footer_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left_edge=self.__style.footer_left_tee,
            heading_col_sep=self.__style.heading_col_footer_cross,
            column_seperator=self.__style.footer_row_cross,
            right_edge=self.__style.footer_right_tee,
            filler=self.__style.footer_row_sep,
        )

    def __body_to_ascii(self) -> str:
        return "".join(
            self.__row_to_ascii(
                left_edge=self.__style.left_and_right_edge,
                heading_col_sep=self.__style.heading_col_sep,
                column_seperator=self.__style.middle_edge,
                right_edge=self.__style.left_and_right_edge,
                filler=row,
            )
            for row in self.__body
        )

    def to_ascii(self) -> str:
        # top row of table
        table = self.__top_edge_to_ascii()
        # add table header
        if self.__header:
            table += self.__header_row_to_ascii()
            table += self.__header_sep_to_ascii()
        # add table body
        if self.__body:
            table += self.__body_to_ascii()
        # add table footer
        if self.__footer:
            table += self.__footer_sep_to_ascii()
            table += self.__footer_row_to_ascii()
        # bottom row of table
        table += self.__bottom_edge_to_ascii()
        # reurn ascii table
        return table


def table2ascii(**options) -> str:
    """Convert a 2D Python table to ASCII text

    ### Arguments
    :param header: :class:`Optional[List]` List of column values in the table's header row
    :param body: :class:`Optional[List[List]]` 2-dimensional list of values in the table's body
    :param footer: :class:`Optional[List]` List of column values in the table's footer row
    :param column_widths: :class:`Optional[List[int]]` List of widths in characters for each column (defaults to auto-sizing)
    :param alignments: :class:`Optional[List[Alignment]]` List of alignments (ex. `[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]`)
    :param first_col_heading: :class:`Optional[bool]` Whether to add a header column separator after the first column
    :param last_col_heading: :class:`Optional[bool]` Whether to add a header column separator before the last column
    """
    return TableToAscii(Options(**options)).to_ascii()
