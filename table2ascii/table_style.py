from dataclasses import dataclass


@dataclass
class TableStyle:
    """Class for storing information about a table style

    Parts of the table labeled alphabetically:

    .. code-block::

        ABBBBBCBBBBBDBBBBBDBBBBBDBBBBBE
        F     G     H     H     H     F
        IJJJJJKJJJJJLJJJJJLJJJJJLJJJJJM
        F     G     H     H     H     F
        NOOOOOPOOOOOQOOOOOQOOOOOQOOOOOR
        F     G     H     H     H     F
        IJJJJJKJJJJJLJJJJJLJJJJJLJJJJJM
        F     G     H     H     H     F
        SBBBBBTBBBBBUBBBBBUBBBBBUBBBBBV

    How the theme is displayed with double thickness for
    heading rows and columns and thin for normal rows and columns:

    .. code-block::

        ╔═════╦═════╤═════╤═════╤═════╗
        ║  #  ║  G  │  H  │  R  │  S  ║
        ╠═════╬═════╪═════╪═════╪═════╣
        ║  1  ║ 30  │ 40  │ 35  │ 30  ║
        ╟─────╫─────┼─────┼─────┼─────╢
        ║  2  ║ 30  │ 40  │ 35  │ 30  ║
        ╠═════╬═════╪═════╪═════╪═════╣
        ║ SUM ║ 130 │ 140 │ 135 │ 130 ║
        ╚═════╩═════╧═════╧═════╧═════╝

    In addition to the parts above, W-Z are used for merged cells as follows:

    .. code-block::

        +-----+-----+---+---+-----+
        |   Merge   | # | G |  S  |
        +====[Y]====+==[Z]==+=====+
        |  1  | 100 |  Long | 150 |
        +----[X]----+--[W]--+-----+
        |   Bonus   | 5 | 5 | 150 |
        +====[Y]====+==[Z]==+=====+
        | SUM | 100 |  200  | 300 |
        +-----+-----+-------+-----+

    """

    # parts of the table
    top_left_corner: str  # A
    top_and_bottom_edge: str  # B
    heading_col_top_tee: str  # C
    top_tee: str  # D
    top_right_corner: str  # E
    left_and_right_edge: str  # F
    heading_col_sep: str  # G
    col_sep: str  # H
    heading_row_left_tee: str  # I
    heading_row_sep: str  # J
    heading_col_heading_row_cross: str  # K
    heading_row_cross: str  # L
    heading_row_right_tee: str  # M
    row_left_tee: str  # N
    row_sep: str  # O
    heading_col_row_cross: str  # P
    col_row_cross: str  # Q
    row_right_tee: str  # R
    bottom_left_corner: str  # S
    heading_col_bottom_tee: str  # T
    bottom_tee: str  # U
    bottom_right_corner: str  # V
    col_row_top_tee: str  # W
    col_row_bottom_tee: str  # X
    heading_row_top_tee: str  # Y
    heading_row_bottom_tee: str  # Z

    @classmethod
    def from_string(cls, string: str) -> "TableStyle":
        """Create a TableStyle from a string

        Args:
            string: The string to create the TableStyle from

        Returns:
            A TableStyle object

        Example::

            TableStyle.from_string("╔═╦╤╗║║│╠═╬╪╣╟─╫┼╢╚╩╧╝┬┴╤╧")

        Raises:
            ValueError: If the string is too long
        """
        num_params = len(cls.__dataclass_fields__)
        # if the string is too long, raise an error
        if len(string) > num_params:
            raise ValueError(
                f"Too many characters in string. Expected {num_params} but got {len(string)}."
            )
        # if the string is too short, pad it with spaces
        elif len(string) < num_params:
            string += " " * (num_params - len(string))
        return cls(*string)

    def set(self, **kwargs) -> "TableStyle":
        """Set attributes of the TableStyle

        Args:
            kwargs: The attributes to set

        Returns:
            A TableStyle object with the attributes set

        Example::

            TableStyle().set(top_left_corner="╔", top_and_bottom_edge="═")
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self
