from enum import Enum


class Alignment(Enum):
    """
    Enum for text alignment types within a table cell

    Example::

        from table2ascii import Alignment

        output = table2ascii(
            ...
            alignments=[Alignment.LEFT, Alignment.RIGHT, Alignment.CENTER, Alignment.CENTER]
        )
    """

    LEFT = 0
    CENTER = 1
    RIGHT = 2
