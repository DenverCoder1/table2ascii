from enum import Enum


class Merge(Enum):
    """Enum for merging table cells

    Using :attr:`Merge.LEFT` in a table cell will merge the cell it is used in
    with the cell to its left.

    In the case that the contents of the merged cell are longer than the
    combined widths of the unmerged cells in the rows above and below,
    the merged cell will be wrapped onto multiple lines. The ``column_widths``
    option can be used to control the widths of the unmerged cells.

    Example::

        from table2ascii import Merge, PresetStyle, table2ascii

        table2ascii(
            header=["Name", "Price", "Category", "Stock"],
            body=[["Milk", "$2.99", "N/A", Merge.LEFT]],
            footer=["Description", "Milk is a nutritious beverage", Merge.LEFT, Merge.LEFT],
            style=PresetStyle.double_box,
        )

        \"\"\"
        ╔═════════════╦═══════╦══════════╦═══════╗
        ║    Name     ║ Price ║ Category ║ Stock ║
        ╠═════════════╬═══════╬══════════╩═══════╣
        ║    Milk     ║ $2.99 ║       N/A        ║
        ╠═════════════╬═══════╩══════════════════╣
        ║ Description ║   Milk is a nutritious   ║
        ║             ║         beverage         ║
        ╚═════════════╩══════════════════════════╝
        \"\"\"

    .. versionadded:: 1.0.0
    """

    LEFT = 0

    def __str__(self) -> str:
        return ""
