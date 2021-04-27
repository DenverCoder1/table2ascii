from typing import List
from math import floor, ceil

# constants
ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2


class TableToAscii:
    """Class used to convert a 2D Python table to ASCII text"""

    def __init__(self, header_row: List, body: List[List], footer_row: List):
        self.__header_row = header_row
        self.__body = body
        self.__footer_row = footer_row
        self.__cell_width = 5  # ! TODO: Remove
        self.__cell_widths = [5, 5, 5, 5, 5]  # TODO: make this automatic
        """
        ╔═════╦═══════════════════════╗
        ║  #  ║  G     H     R     S  ║
        ╟─────╫───────────────────────╢
        ║  1  ║  30    40    35    30 ║
        ║  2  ║  30    40    35    30 ║
        ╟─────╫───────────────────────╢
        ║ SUM ║ 130   140   135   130 ║
        ╚═════╩═══════════════════════╝

        0111112111113111113111113111114
        5     6     7     7     7     5
        899999a99999b99999b99999b99999c
        5     6     7     7     7     5
        5     6     7     7     7     5
        deeeeefeeeeegeeeeegeeeeegeeeeeh
        5     6     7     7     7     5
        i11111j11111k11111k11111k11111l
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
        if alignment == ALIGN_LEFT:
            return f" {text} " + (" " * (width - len(text) - 2))
        if alignment == ALIGN_CENTER:
            before = " " * floor((width - len(text) - 2) / 2)
            after = " " * ceil((width - len(text) - 2) / 2)
            return before + f" {text} " + after
        if alignment == ALIGN_RIGHT:
            return (" " * (width - len(text) - 2)) + f" {text} "
        raise ValueError(f"The value '{alignment}' is not valid for alignment.")

    def __top_edge_to_ascii(self) -> str:
        """Assembles the top edge of the ascii table"""
        # top-left corner of the table
        output: str = self.parts["top_left_corner"]
        # top edge above the first column
        output += self.parts["top_and_bottom_edge"] * self.__cell_widths[0]
        # tee separating first column from the rest of the table
        output += self.parts["first_col_top_tee"]
        # add remaining columns
        for i in range(len(self.__header_row) - 1):
            output += self.parts["top_and_bottom_edge"] * self.__cell_widths[i]
            output += self.parts["top_tee"]
        # replace last top tee with top-right corner
        output = output[0:-1] + self.parts["top_right_corner"]
        return output

    def __header_row_to_ascii(self) -> str:
        """Assembles the header row line of the ascii table"""
        # add left edge of table
        output: str = self.parts["left_and_right_edge"]
        # add first column contents and padding
        output += self.__pad(str(self.__header_row[0]), self.__cell_widths[0])
        # separate first column from the rest of the table
        output += self.parts["first_col_sep"]
        # add the rest of the headers
        output += self.parts["middle_edge"].join(
            self.__pad(str(val), self.__cell_widths[i + 1])
            for i, val in enumerate(self.__header_row[1:])
        )
        # add right edge of the table
        output += self.parts["left_and_right_edge"]
        return output

    def __header_sep_to_ascii(self) -> str:
        """Assembles the seperator below the header of the ascii table"""
        # add left edge tee
        output: str = self.parts["header_left_tee"]
        # top edge above the first column
        output += self.parts["header_row_sep"] * self.__cell_widths[0]
        # tee separating first column from the rest of the table
        output += self.parts["first_col_header_cross"]
        # add remaining columns
        for i in range(len(self.__header_row) - 1):
            output += self.parts["header_row_sep"] * self.__cell_widths[i]
            output += self.parts["header_row_cross"]
        # replace last top tee with top-right corner
        output = output[0:-1] + self.parts["right_tee"]
        return output

    def to_ascii(self) -> str:
        cols = len(self.__header_row)
        # create table header
        table = [
            self.__top_edge_to_ascii(),
            self.__header_row_to_ascii(),
            self.__header_sep_to_ascii(),
        ]
        # add table body
        for p in self.__body:
            # add table row
            table += [
                # ║
                self.parts["left_and_right_edge"]
                +
                #  1  ║
                f"  {p[0]}  "
                + self.parts["first_col_sep"]
                #  40    40    40    40
                + self.parts["middle_edge"].join(
                    f"{p[i].rjust(4)} " for i in range(1, cols)
                )
                # ║
                + self.parts["left_and_right_edge"]
            ]
        # footer row
        table += [
            # ╟
            self.parts["footer_left_tee"]
            # ─────╫
            + (
                self.parts["footer_row_sep"] * self.__cell_width
                + self.parts["first_col_footer_cross"]
            )
            # ───────────────────────
            + (
                (
                    self.parts["footer_row_sep"] * self.__cell_width
                    + self.parts["footer_row_cross"]
                )
                * (cols - 1)
            )[0:-1]
            # ╢
            + self.parts["right_tee"],
            # ║
            self.parts["left_and_right_edge"]
            #  SUM ║
            + f"{self.__footer_row[0].rjust(4)} " + self.parts["first_col_sep"]
            #  120 ║ 120 ║ 120 ║ 120 ║
            + self.parts["middle_edge"].join(
                f"{self.__footer_row[i].rjust(4)} " for i in range(1, cols)
            )
            # ║
            + self.parts["left_and_right_edge"],
            # ╚
            self.parts["bottom_left_corner"]
            # ═════╩
            + self.parts["top_and_bottom_edge"] * self.__cell_width
            + self.parts["first_col_bottom_tee"]
            # ════════════════════════
            + (
                (
                    self.parts["top_and_bottom_edge"] * self.__cell_width
                    + self.parts["bottom_tee"]
                )
                * (cols - 1)
            )[0:-1]
            # ╗
            + self.parts["bottom_right_corner"],
        ]
        return "\n".join(table)


def table2ascii(header_row: List, body: List[List], footer_row: List) -> str:
    """Convert a 2D Python table to ASCII text
    #TODO: add param documentation
    """
    return TableToAscii(header_row, body, footer_row).to_ascii()
