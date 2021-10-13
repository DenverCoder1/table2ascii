from dataclasses import dataclass
from typing import List, Optional

from .alignment import Alignment
from .preset_style import PresetStyle
from .table_style import TableStyle


@dataclass
class Options:
    """Class for storing options that the user sets"""

    first_col_heading: bool = False
    last_col_heading: bool = False
    column_widths: Optional[List[int]] = None
    alignments: Optional[List[Alignment]] = None
    style: TableStyle = PresetStyle.double_thin_compact
