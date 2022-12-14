from enum import IntEnum


class Alignment(IntEnum):
    """Enum for text alignment types within a table cell

    Example::

        from table2ascii import Alignment, table2ascii

        table2ascii(
            header=["Product", "Category", "Price", "In Stock"],
            body=[
                ["Milk", "Dairy", "$2.99", "Yes"],
                ["Cheese", "Dairy", "$10.99", "No"],
                ["Apples", "Produce", "$0.99", "Yes"],
            ],
            alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT, Alignment.LEFT],
        )

        \"\"\"
        ╔════════════════════════════════════════╗
        ║ Product   Category    Price   In Stock ║
        ╟────────────────────────────────────────╢
        ║ Milk       Dairy      $2.99   Yes      ║
        ║ Cheese     Dairy     $10.99   No       ║
        ║ Apples    Produce     $0.99   Yes      ║
        ╚════════════════════════════════════════╝
        \"\"\"
    """

    LEFT = 0
    CENTER = 1
    RIGHT = 2
