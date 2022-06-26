from dataclasses import dataclass
from typing import List, Optional

from .alignment import Alignment
from .table_style import TableStyle


@dataclass
class Options:
    """Class for storing options that the user sets"""

    first_col_heading: bool
    last_col_heading: bool
    column_widths: Optional[List[Optional[int]]]
    alignments: Optional[List[Alignment]]
    style: TableStyle
