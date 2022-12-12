from enum import Enum


class Merge(Enum):
    """Enum for types of cell merging in a table

    Example::

    from table2ascii import table2ascii
    from table2ascii.merge import Merge

    output = table2ascii(
        body=[
            ["A", "B", "C", "D"],
            ["E", "Long cell", Merge.LEFT, Merge.LEFT],
        ],
    )

    print(output)

    ╔═══════════════╗
    ║ A   B   C   D ║
    ║ E   Long cell ║
    ╚═══════════════╝
    """

    LEFT = 0

    def __repr__(self):
        return f"Merge.{self.name}"

    def __str__(self):
        return ""
