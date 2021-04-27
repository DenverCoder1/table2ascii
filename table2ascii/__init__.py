from typing import List, Optional, Union
from math import floor, ceil

# constants
ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(
        self,
        header_row: Optional[List],
        body: Optional[List[List]],
        footer_row: Optional[List],
    ):
        """Validate arguments and initialize fields"""
        # check if columns in header are different from footer
        if header_row and footer_row and len(header_row) != len(footer_row):
            raise ValueError("Header row and footer row must have the same length")
        # check if columns in header are different from body
        if header_row and body and len(body) > 0 and len(header_row) != len(body[0]):
            raise ValueError("Header row and body rows must have the same length")
        # check if any rows in body have a different number of columns
        if body and len(body) and list(filter(lambda x: len(x) != len(body[0]), body)):
            raise ValueError("All rows in body must have the same length")

        # initialize fields
        self.__header_row = header_row
        self.__body = body
        self.__footer_row = footer_row
        self.__columns = self.__count_columns()
        self.__cell_widths = [5, 5, 5, 5, 5]  # TODO: make this automatic

        """
        ╔═════╦═══════════════════════╗   ABBBBBCBBBBBDBBBBBDBBBBBDBBBBBE
        ║  #  ║  G     H     R     S  ║   F     G     H     H     H     F
        ╟─────╫───────────────────────╢   IJJJJJKJJJJJLJJJJJLJJJJJLJJJJJM
        ║  1  ║  30    40    35    30 ║   F     G     H     H     H     F
        ║  2  ║  30    40    35    30 ║   F     G     H     H     H     F
        ╟─────╫───────────────────────╢   NOOOOOPOOOOOQOOOOOQOOOOOQOOOOOR
        ║ SUM ║ 130   140   135   130 ║   F     G     H     H     H     F
        ╚═════╩═══════════════════════╝   SBBBBBTBBBBBUBBBBBUBBBBBUBBBBBV
        """
        self.__parts = {
            "top_left_corner": "╔",  # A
            "top_and_bottom_edge": "═",  # B
            "first_col_top_tee": "╦",  # C
            "top_tee": "═",  # D
            "top_right_corner": "╗",  # E
            "left_and_right_edge": "║",  # F
            "first_col_sep": "║",  # G
            "middle_edge": " ",  # H
            "header_left_tee": "╟",  # I
            "header_row_sep": "─",  # J
            "first_col_header_cross": "╫",  # K
            "header_row_cross": "─",  # L
            "header_right_tee": "╢",  # M
            "footer_left_tee": "╟",  # N
            "footer_row_sep": "─",  # O
            "first_col_footer_cross": "╫",  # P
            "footer_row_cross": "─",  # Q
            "footer_right_tee": "╢",  # R
            "bottom_left_corner": "╚",  # S
            "first_col_bottom_tee": "╩",  # T
            "bottom_tee": "═",  # U
            "bottom_right_corner": "╝",  # V
        }

    def __count_columns(self):
        if self.__header_row:
            return len(self.__header_row)
        if self.__footer_row:
            return len(self.__footer_row)
        if self.__body and len(self.__body) > 0:
            return len(self.__body[0])
        return 0

    def __pad(self, text: str, width: int, alignment: int = ALIGN_CENTER):
        """Pad a string of text to a given width with specified alignment"""
        if alignment == ALIGN_LEFT:
            return f" {text} " + (" " * (width - len(text) - 2))
        if alignment == ALIGN_CENTER:
            before = " " * ceil((width - len(text) - 2) / 2)
            after = " " * floor((width - len(text) - 2) / 2)
            return before + f" {text} " + after
        if alignment == ALIGN_RIGHT:
            return (" " * (width - len(text) - 2)) + f" {text} "
        raise ValueError(f"The value '{alignment}' is not valid for alignment.")

    def __row_to_ascii(
        self,
        left: str,
        first_col_sep: str,
        col_sep: str,
        right: str,
        filler: Union[str, List],
    ) -> str:
        """Assembles a row of the ascii table"""
        # left edge of the row
        output: str = left
        # content across the first column
        output += (
            # edge or row separator if filler is specified
            filler * self.__cell_widths[0]
            if isinstance(filler, str)
            # otherwise, first column content
            else self.__pad(str(filler[0]), self.__cell_widths[0])
        )
        # separation of first column from the rest of the table
        output += first_col_sep
        # add remaining columns
        for i in range(1, self.__columns):
            # content between separators
            output += (
                # edge or row separator if filler is specified
                filler * self.__cell_widths[i]
                if isinstance(filler, str)
                # otherwise, column content
                else self.__pad(str(filler[i]), self.__cell_widths[i])
            )
            # add a separator
            output += col_sep
        # replace last seperator with symbol for edge of the row
        output = output[0:-1] + right
        return output + "\n"

    def __top_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["top_left_corner"],
            first_col_sep=self.__parts["first_col_top_tee"],
            col_sep=self.__parts["top_tee"],
            right=self.__parts["top_right_corner"],
            filler=self.__parts["top_and_bottom_edge"],
        )

    def __bottom_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["bottom_left_corner"],
            first_col_sep=self.__parts["first_col_bottom_tee"],
            col_sep=self.__parts["bottom_tee"],
            right=self.__parts["bottom_right_corner"],
            filler=self.__parts["top_and_bottom_edge"],
        )

    def __header_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["left_and_right_edge"],
            first_col_sep=self.__parts["first_col_sep"],
            col_sep=self.__parts["middle_edge"],
            right=self.__parts["left_and_right_edge"],
            filler=self.__header_row,
        )

    def __footer_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["left_and_right_edge"],
            first_col_sep=self.__parts["first_col_sep"],
            col_sep=self.__parts["middle_edge"],
            right=self.__parts["left_and_right_edge"],
            filler=self.__footer_row,
        )

    def __header_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["header_left_tee"],
            first_col_sep=self.__parts["first_col_header_cross"],
            col_sep=self.__parts["header_row_cross"],
            right=self.__parts["header_right_tee"],
            filler=self.__parts["header_row_sep"],
        )

    def __footer_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left=self.__parts["footer_left_tee"],
            first_col_sep=self.__parts["first_col_footer_cross"],
            col_sep=self.__parts["footer_row_cross"],
            right=self.__parts["footer_right_tee"],
            filler=self.__parts["footer_row_sep"],
        )

    def __body_to_ascii(self) -> str:
        output: str = ""
        for row in self.__body:
            output += self.__row_to_ascii(
                left=self.__parts["left_and_right_edge"],
                first_col_sep=self.__parts["first_col_sep"],
                col_sep=self.__parts["middle_edge"],
                right=self.__parts["left_and_right_edge"],
                filler=row,
            )
        return output

    def to_ascii(self) -> str:
        # top row of table
        table = self.__top_edge_to_ascii()
        # add table header
        if self.__header_row:
            table += self.__header_row_to_ascii()
            table += self.__header_sep_to_ascii()
        # add table body
        if self.__body:
            table += self.__body_to_ascii()
        # add table footer
        if self.__footer_row:
            table += self.__footer_sep_to_ascii()
            table += self.__footer_row_to_ascii()
        # bottom row of table
        table += self.__bottom_edge_to_ascii()
        # reurn ascii table
        return table


def table2ascii(
    header_row: Optional[List] = None,
    body: Optional[List[List]] = None,
    footer_row: Optional[List] = None,
) -> str:
    """Convert a 2D Python table to ASCII text
    #TODO: add param documentation
    """
    return TableToAscii(header_row, body, footer_row).to_ascii()
