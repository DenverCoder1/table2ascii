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
        """
        self.parts = {
            "top_left_corner": "╔",
            "top_right_corner": "╗",
            "top_edge": "═",
            "first_col_top_tee": "╦",
            "top_tee": "═",
            "left_edge": "║",
            "header_row_sep": "─",
            "footer_row_sep": "─",
            "first_col_sep": "║",
            "left_tee": "╟",
            "middle_edge": " ",
            "header_row_cross": "─",
            "footer_row_cross": "─",
            "first_col_cross": "╫",
            "right_edge": "║",
            "right_tee": "╢",
            "bottom_left_corner": "╚",
            "bottom_right_corner": "╝",
            "bottom_edge": "═",
            "first_col_bottom_tee": "╩",
            "bottom_tee": "═",
        }

    def to_ascii(self) -> str:
        cols = len(self.header_row)
        # create table header
        table = [
            # ╔
            self.parts["top_left_corner"]
            # ═════╦
            + self.parts["top_edge"] * self.cell_width + self.parts["first_col_top_tee"]
            #
            + (
                (self.parts["top_edge"] * self.cell_width + self.parts["top_tee"])
                * (cols - 1)
            )[0:-1]
            # ╗
            + self.parts["top_right_corner"],
            # ║
            self.parts["left_edge"]
            #  #  ║
            + f"  {self.header_row[0]}  " + self.parts["first_col_sep"]
            #    G     H     R     S
            + self.parts["middle_edge"].join(
                "  " + val + "  " for val in self.header_row[1:]
            )
            # ║
            + self.parts["right_edge"],
            # ╟
            self.parts["left_tee"]
            # ─────╫
            + (
                self.parts["header_row_sep"] * self.cell_width
                + self.parts["first_col_cross"]
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
                self.parts["left_edge"]
                +
                #  1  ║
                f"  {p[0]}  "
                + self.parts["first_col_sep"]
                #  40    40    40    40
                + self.parts["middle_edge"].join(
                    f"{p[i].rjust(4)} " for i in range(1, cols)
                )
                # ║
                + self.parts["right_edge"]
            ]
        # footer row
        table += [
            # ╟
            self.parts["left_tee"]
            # ─────╫
            + (
                self.parts["footer_row_sep"] * self.cell_width
                + self.parts["first_col_cross"]
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
            self.parts["left_edge"]
            #  SUM ║
            + f"{self.footer_row[0].rjust(4)} " + self.parts["first_col_sep"]
            #  120 ║ 120 ║ 120 ║ 120 ║
            + self.parts["middle_edge"].join(
                f"{self.footer_row[i].rjust(4)} " for i in range(1, cols)
            )
            # ║
            + self.parts["right_edge"],
            # ╚
            self.parts["bottom_left_corner"]
            # ═════╩
            + self.parts["bottom_edge"] * self.cell_width
            + self.parts["first_col_bottom_tee"]
            # ════════════════════════
            + (
                (self.parts["bottom_edge"] * self.cell_width + self.parts["bottom_tee"])
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
