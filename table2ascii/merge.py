from enum import Enum


class Merge(Enum):
    """Enum for types of cell merging in a table

    Example::

    output = table2ascii(
        body=[
            ["a", "b", "c", "d"],
            ["e", "Long cell value", Merge.LEFT, Merge.LEFT],
        ],
    )

    print(output)

    ╔═════════════════════╗
    ║ a    b        c   d ║
    ║ e   Long cell value ║
    ╚═════════════════════╝
    """

    LEFT = 0

    def __repr__(self):
        return f"Merge.{self.name}"

    def __str__(self):
        return ""
