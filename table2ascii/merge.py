from enum import Enum


class Merge(Enum):
    """Enum for merging table cells

    Using :attr:`Merge.LEFT` in a table cell will merge the cell it is used in
    with the cell to its left.

    In the case that the contents of the merged cell are longer than the
    contents of the unmerged cells in the rows above and below, the merged
    cell will be wrapped onto multiple lines.

    Example::

        from table2ascii import table2ascii, Merge, PresetStyle

        table2ascii(
            body=[
                ["A", "B", "C", "D"],
                ["E", "Long cell contents", Merge.LEFT, Merge.LEFT],
            ],
            style=PresetStyle.double_box,
        )

        \"\"\"
        ╔═══╦═══╦═══╦═══╗
        ║ A ║ B ║ C ║ D ║
        ╠═══╬═══╩═══╩═══╣
        ║ E ║ Long cell ║
        ║   ║ contents  ║
        ╚═══╩═══════════╝
        \"\"\"
    """

    LEFT = 0

    def __str__(self):
        return ""
