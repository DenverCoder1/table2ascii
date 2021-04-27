from typing import List, Union
from math import floor, ceil

# constants
ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(self, header_row: List, body: List[List], footer_row: List):
        """Validate arguments and initialize fields"""
        # check that values are valid
        if len(header_row) != len(footer_row):
            raise ValueError("header row and footer row must have the same length")
        if len(header_row) != len(body[0]):
            raise ValueError("header row and body rows must have the same length")
        for row in body[1:]:
            if len(body[0]) != len(row):
                raise ValueError("all rows in body must have the same length")

        # initialize fields
        self.__header_row = header_row
        self.__body = body
        self.__footer_row = footer_row
        self.__cell_widths = [5, 5, 5, 5, 5]  # TODO: make this automatic

        """
        ╔═════╦═══════════════════════╗   0111112111113111113111113111114
        ║  #  ║  G     H     R     S  ║   5     6     7     7     7     5
        ╟─────╫───────────────────────╢   899999a99999b99999b99999b99999c
        ║  1  ║  30    40    35    30 ║   5     6     7     7     7     5
        ║  2  ║  30    40    35    30 ║   5     6     7     7     7     5
        ╟─────╫───────────────────────╢   deeeeefeeeeegeeeeegeeeeegeeeeeh
        ║ SUM ║ 130   140   135   130 ║   5     6     7     7     7     5
        ╚═════╩═══════════════════════╝   i11111j11111k11111k11111k11111l
        """
        self.parts = {
            "top_left_corner": "╔",  # 0
            "top_and_bottom_edge": "═",  # 1
            "first_col_top_tee": "╦",  # 2
            "top_tee": "═",  # 3
            "top_right_corner": "╗",  # 4
            "left_and_right_edge": "║",  # 5
            "first_col_sep": "║",  # 6
            "middle_edge": " ",  # 7
            "header_left_tee": "╟",  # 8
            "header_row_sep": "─",  # 9
            "first_col_header_cross": "╫",  # a
            "header_row_cross": "─",  # b
            "right_tee": "╢",  # c
            "footer_left_tee": "╟",  # d
            "footer_row_sep": "─",  # e
            "first_col_footer_cross": "╫",  # f
            "footer_row_cross": "─",  # g
            "bottom_left_corner": "╚",  # i
            "first_col_bottom_tee": "╩",  # j
            "bottom_tee": "═",  # k
            "bottom_right_corner": "╝",  # l
        }

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
        for i in range(1, len(self.__header_row)):
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
            left=self.parts["top_left_corner"],
            first_col_sep=self.parts["first_col_top_tee"],
            col_sep=self.parts["top_tee"],
            right=self.parts["top_right_corner"],
            filler=self.parts["top_and_bottom_edge"],
        )

    def __bottom_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        return self.__row_to_ascii(
            left=self.parts["bottom_left_corner"],
            first_col_sep=self.parts["first_col_bottom_tee"],
            col_sep=self.parts["bottom_tee"],
            right=self.parts["bottom_right_corner"],
            filler=self.parts["top_and_bottom_edge"],
        )

    def __header_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left=self.parts["left_and_right_edge"],
            first_col_sep=self.parts["first_col_sep"],
            col_sep=self.parts["middle_edge"],
            right=self.parts["left_and_right_edge"],
            filler=self.__header_row,
        )

    def __footer_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        return self.__row_to_ascii(
            left=self.parts["left_and_right_edge"],
            first_col_sep=self.parts["first_col_sep"],
            col_sep=self.parts["middle_edge"],
            right=self.parts["left_and_right_edge"],
            filler=self.__footer_row,
        )

    def __header_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left=self.parts["header_left_tee"],
            first_col_sep=self.parts["first_col_header_cross"],
            col_sep=self.parts["header_row_cross"],
            right=self.parts["right_tee"],
            filler=self.parts["header_row_sep"],
        )

    def __footer_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        return self.__row_to_ascii(
            left=self.parts["footer_left_tee"],
            first_col_sep=self.parts["first_col_footer_cross"],
            col_sep=self.parts["footer_row_cross"],
            right=self.parts["right_tee"],
            filler=self.parts["header_row_sep"],
        )

    def __body_to_ascii(self) -> str:
        output: str = ""
        for row in self.__body:
            output += self.__row_to_ascii(
                left=self.parts["left_and_right_edge"],
                first_col_sep=self.parts["first_col_sep"],
                col_sep=self.parts["middle_edge"],
                right=self.parts["left_and_right_edge"],
                filler=row,
            )
        return output

    def to_ascii(self) -> str:
        # add table header
        table: str = self.__top_edge_to_ascii()
        table += self.__header_row_to_ascii()
        table += self.__header_sep_to_ascii()
        # add table body
        table += self.__body_to_ascii()
        # add table footer
        table += self.__footer_sep_to_ascii()
        table += self.__footer_row_to_ascii()
        table += self.__bottom_edge_to_ascii()
        return table


def table2ascii(header_row: List, body: List[List], footer_row: List) -> str:
    """Convert a 2D Python table to ASCII text
    #TODO: add param documentation
    """
    return TableToAscii(header_row, body, footer_row).to_ascii()
