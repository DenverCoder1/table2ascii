from enum import IntEnum


class Alignment(IntEnum):
    """Enum for text alignment types within a table cell

    Example::

        from table2ascii import Alignment, table2ascii

        table2ascii(
            header=["Product", "Category", "Price", "Rating"],
            body=[
                ["Milk", "Dairy", "$2.99", "6.28318"],
                ["Cheese", "Dairy", "$10.99", "8.2"],
                ["Apples", "Produce", "$0.99", "10.00"],
            ],
            alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT, Alignment.DECIMAL],
        )

        \"\"\"
        ╔════════════════════════════════════════╗
        ║ Product   Category    Price    Rating  ║
        ╟────────────────────────────────────────╢
        ║ Milk       Dairy      $2.99    6.28318 ║
        ║ Cheese     Dairy     $10.99    8.2     ║
        ║ Apples    Produce     $0.99   10.00    ║
        ╚════════════════════════════════════════╝
        \"\"\"

    .. note::

        If the :attr:`DECIMAL` alignment type is used, any cell values that are
        not valid decimal numbers will be aligned to the center. Decimal numbers
        include integers, floats, and strings containing only
        :meth:`decimal <str.isdecimal>` characters and at most one decimal point.

    .. versionchanged:: 1.1.0

        Added :attr:`DECIMAL` alignment -- align decimal numbers such that
        the decimal point is aligned with the decimal point of all other numbers
        in the same column.
    """

    LEFT = 0
    CENTER = 1
    RIGHT = 2
    DECIMAL = 3
