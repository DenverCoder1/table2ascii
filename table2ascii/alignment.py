from enum import IntEnum


class Alignment(IntEnum):
    """Enum for text alignment types within a table cell

    A list of alignment types can be used to align each column individually::

        from table2ascii import Alignment, table2ascii

        table2ascii(
            header=["Product", "Category", "Price", "Rating"],
            body=[
                ["Milk", "Dairy", "$2.99", "6.28318"],
                ["Cheese", "Dairy", "$10.99", "8.2"],
                ["Apples", "Produce", "$0.99", "10.00"],
            ],
            # Align the first column to the left, the second to the center,
            # the third to the right, and the fourth to the decimal point
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

    A single alignment type can be used to align all columns::

        table2ascii(
            header=["First Name", "Last Name", "Age"],
            body=[
                ["John", "Smith", 30],
                ["Jane", "Doe", 28],
            ],
            alignments=Alignment.LEFT,  # Align all columns to the left
            number_alignments=Alignment.RIGHT,  # Align all numeric values to the right
        )

        \"\"\"
        ╔══════════════════════════════╗
        ║ First Name   Last Name   Age ║
        ╟──────────────────────────────╢
        ║ John         Smith        30 ║
        ║ Jane         Doe          28 ║
        ╚══════════════════════════════╝
        \"\"\"

    .. note::

        If :attr:`DECIMAL` is used in the ``number_alignments`` argument to :func:`table2ascii`,
        all non-numeric values will be aligned according to the ``alignments`` argument.
        If the :attr:`DECIMAL` alignment type is used in the ``alignments`` argument,
        all non-numeric values will be aligned to the center.
        Numeric values include integers, floats, and strings containing only :meth:`decimal <str.isdecimal>`
        characters and at most one decimal point.

    .. versionchanged:: 1.1.0

        Added :attr:`DECIMAL` alignment -- align decimal numbers such that
        the decimal point is aligned with the decimal point of all other numbers
        in the same column.
    """

    LEFT = 0
    CENTER = 1
    RIGHT = 2
    DECIMAL = 3
