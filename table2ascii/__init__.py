"""
table2ascii - Library for converting 2D Python lists to fancy ASCII/Unicode tables
"""

from .alignment import Alignment
from .preset_style import PresetStyle
from .table_style import TableStyle
from .table_to_ascii import table2ascii

__version__ = "0.4.0"

__all__ = [
    "table2ascii",
    "Alignment",
    "TableStyle",
    "PresetStyle",
]
