from dataclasses import dataclass


@dataclass
class Style:
    """Class for storing information about a table style

    **Parts of the table labeled alphabetically**

    ```text
    ABBBBBCBBBBBDBBBBBDBBBBBDBBBBBE
    F     G     H     H     H     F
    IJJJJJKJJJJJLJJJJJLJJJJJLJJJJJM
    F     G     H     H     H     F
    F     G     H     H     H     F
    NOOOOOPOOOOOQOOOOOQOOOOOQOOOOOR
    F     G     H     H     H     F
    SBBBBBTBBBBBUBBBBBUBBBBBUBBBBBV
    ```

    **How the default theme is displayed**

    ```text
    ╔═════╦═══════════════════════╗
    ║  #  ║  G     H     R     S  ║
    ╟─────╫───────────────────────╢
    ║  1  ║  30    40    35    30 ║
    ║  2  ║  30    40    35    30 ║
    ╟─────╫───────────────────────╢
    ║ SUM ║ 130   140   135   130 ║
    ╚═════╩═══════════════════════╝
    ```
    """

    top_left_corner: str  # A
    top_and_bottom_edge: str  # B
    heading_col_top_tee: str  # C
    top_tee: str  # D
    top_right_corner: str  # E
    left_and_right_edge: str  # F
    heading_col_sep: str  # G
    middle_edge: str  # H
    header_left_tee: str  # I
    header_row_sep: str  # J
    heading_col_header_cross: str  # K
    header_row_cross: str  # L
    header_right_tee: str  # M
    footer_left_tee: str  # N
    footer_row_sep: str  # O
    heading_col_footer_cross: str  # P
    footer_row_cross: str  # Q
    footer_right_tee: str  # R
    bottom_left_corner: str  # S
    heading_col_bottom_tee: str  # T
    bottom_tee: str  # U
    bottom_right_corner: str  # V
