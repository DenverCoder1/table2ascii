from typing import List


class TableToAscii:
    def __init__(
        self,
        header_row: List[str],
        body: List[List[str]],
        footer_row: List[str],
    ):
        self.header_row = header_row
        self.body = body
        self.footer_row = footer_row
        self.cell_width = 5
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
            "top_left_corner": "╔",        # 0
            "top_bottom_edge": "═",        # 1
            "first_col_top_tee": "╦",      # 2
            "top_tee": "═",                # 3
            "top_right_corner": "╗",       # 4
            "left_right_edge": "║",        # 5
            "first_col_sep": "║",          # 6
            "middle_edge": " ",            # 7
            "header_left_tee": "╟",        # 8
            "header_row_sep": "─",         # 9
            "first_col_header_cross": "╫", # a
            "header_row_cross": "─",       # b
            "right_tee": "╢",              # c
            "footer_left_tee": "╟",        # d
            "footer_row_sep": "─",         # e
            "first_col_footer_cross": "╫", # f
            "footer_row_cross": "─",       # g
            "bottom_left_corner": "╚",     # i
            "first_col_bottom_tee": "╩",   # j
            "bottom_tee": "═",             # k
            "bottom_right_corner": "╝",  #   l  
        }

    def to_ascii(self) -> str:
        cols = len(self.header_row)
        # create table header
        table = [
            # ╔
            self.parts["top_left_corner"]
            # ═════╦
            + self.parts["top_bottom_edge"] * self.cell_width + self.parts["first_col_top_tee"]
            #
            + (
                (self.parts["top_bottom_edge"] * self.cell_width + self.parts["top_tee"])
                * (cols - 1)
            )[0:-1]
            # ╗
            + self.parts["top_right_corner"],
            # ║
            self.parts["left_right_edge"]
            #  #  ║
            + f"  {self.header_row[0]}  " + self.parts["first_col_sep"]
            #    G     H     R     S
            + self.parts["middle_edge"].join(
                "  " + val + "  " for val in self.header_row[1:]
            )
            # ║
            + self.parts["left_right_edge"],
            # ╟
            self.parts["header_left_tee"]
            # ─────╫
            + (
                self.parts["header_row_sep"] * self.cell_width
                + self.parts["first_col_header_cross"]
            )
            # ───────────────────────
            + (
                (
                    self.parts["header_row_sep"] * self.cell_width
                    + self.parts["header_row_cross"]
                )
                * (cols - 1)
            )[0:-1]
            # ╢
            + self.parts["right_tee"],
        ]
        # add table body
        for p in self.body:
            # add table row
            table += [
                # ║
                self.parts["left_right_edge"]
                +
                #  1  ║
                f"  {p[0]}  "
                + self.parts["first_col_sep"]
                #  40    40    40    40
                + self.parts["middle_edge"].join(
                    f"{p[i].rjust(4)} " for i in range(1, cols)
                )
                # ║
                + self.parts["left_right_edge"]
            ]
        # footer row
        table += [
            # ╟
            self.parts["footer_left_tee"]
            # ─────╫
            + (
                self.parts["footer_row_sep"] * self.cell_width
                + self.parts["first_col_footer_cross"]
            )
            # ───────────────────────
            + (
                (
                    self.parts["footer_row_sep"] * self.cell_width
                    + self.parts["footer_row_cross"]
                )
                * (cols - 1)
            )[0:-1]
            # ╢
            + self.parts["right_tee"],
            # ║
            self.parts["left_right_edge"]
            #  SUM ║
            + f"{self.footer_row[0].rjust(4)} " + self.parts["first_col_sep"]
            #  120 ║ 120 ║ 120 ║ 120 ║
            + self.parts["middle_edge"].join(
                f"{self.footer_row[i].rjust(4)} " for i in range(1, cols)
            )
            # ║
            + self.parts["left_right_edge"],
            # ╚
            self.parts["bottom_left_corner"]
            # ═════╩
            + self.parts["top_bottom_edge"] * self.cell_width
            + self.parts["first_col_bottom_tee"]
            # ════════════════════════
            + (
                (self.parts["top_bottom_edge"] * self.cell_width + self.parts["bottom_tee"])
                * (cols - 1)
            )[0:-1]
            # ╗
            + self.parts["bottom_right_corner"],
        ]
        return "\n".join(table)


def table2ascii(
    header_row: List[str], body: List[List[str]], footer_row: List[str]
) -> str:
    """Convert a 2D Python table to ASCII text
    #TODO: add param documentation
    """
    return TableToAscii(header_row, body, footer_row).to_ascii()
