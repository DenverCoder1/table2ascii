from dataclasses import dataclass
import warnings

from .exceptions import TableStyleTooShortWarning, TableStyleTooLongError


@dataclass
class TableStyle:
    """Class for storing information about a table style

    Parts of the table labeled alphabetically from A to V:

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

    How the theme is displayed using :ref:`PresetStyle.double_thin_box`
    as an example:

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

    In addition to the parts above, W-Z and the four fields that follow
    (labeled 0-3) are used for top and bottom edges of merged cells as shown:

    .. code-block::

        ╔══════════════╤══════╤══════╗
        ║    Header    │      │      ║
        ╠══════[2]═════╪═════[Z]═════╣
        ║       ║      │             ║
        ╟──────[1]─────┼─────────────╢
        ║              │             ║
        ╟──────[0]─────┼─────[W]─────╢
        ║       ║      │      │      ║
        ╟───────╫──────┼─────[X]─────╢
        ║       ║      │             ║
        ╠══════[3]═════╪═════[Y]═════╣
        ║    Footer    │      │      ║
        ╚══════════════╧══════╧══════╝

        [W] = ┬ [X] = ┴ [Y] = ╤ [Z] = ╧
        [0] = ╥ [1] = ╨ [2] = ╦ [3] = ╩

    .. versionchanged:: 1.0.0

        Added fields for edges of merged cells:

        ``col_row_top_tee``, ``col_row_bottom_tee``, ``heading_row_top_tee``,
        ``heading_row_bottom_tee``, ``heading_col_body_row_top_tee``,
        ``heading_col_body_row_bottom_tee``, ``heading_col_heading_row_top_tee``,
        ``heading_col_heading_row_bottom_tee``
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
    heading_col_body_row_top_tee: str  # 0
    heading_col_body_row_bottom_tee: str  # 1
    heading_col_heading_row_top_tee: str  # 2
    heading_col_heading_row_bottom_tee: str  # 3

    @classmethod
    def from_string(cls, string: str) -> "TableStyle":
        """Create a TableStyle from a string

        .. versionchanged:: 1.0.0

            The string will be padded on the right with spaces if it is too short
            and :class:`~table2ascii.exceptions.TableStyleTooLongError` will be
            raised if it is too long.

        Args:
            string: The string to create the TableStyle from

        Returns:
            A TableStyle object

        Example::

            TableStyle.from_string("╔═╦╤╗║║│╠═╬╪╣╟─╫┼╢╚╩╧╝┬┴╤╧╥╨╦╩")

        Raises:
            TableStyleTooLongError: If the string is too long
        """
        num_params = len(cls.__dataclass_fields__)
        # if the string is too long, raise an error
        if len(string) > num_params:
            raise TableStyleTooLongError(string, num_params)
        # if the string is too short, show a warning and pad it with spaces
        elif len(string) < num_params:
            warnings.warn(TableStyleTooShortWarning(string, num_params), stacklevel=2)
            string += " " * (num_params - len(string))
        return cls(*string)

    def set(self, **kwargs: str) -> "TableStyle":
        """Set attributes of the TableStyle

        Args:
            kwargs: The attributes to set

        Returns:
            A TableStyle object with the attributes set

        Example::

            TableStyle.from_string("~" * 30).set(left_and_right_edge="", col_sep="")
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self
