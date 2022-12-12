from __future__ import annotations

from dataclasses import dataclass

from .alignment import Alignment
from .table_style import TableStyle


@dataclass
class Options:
    """Class for storing options that the user sets

    .. versionchanged:: 1.0.0

        Added ``use_wcwidth`` option
    """

    first_col_heading: bool
    last_col_heading: bool
    column_widths: list[int | None] | None
    alignments: list[Alignment] | None
    cell_padding: int
    style: TableStyle
    use_wcwidth: bool
