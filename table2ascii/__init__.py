"""
table2ascii - Library for converting 2D Python lists to fancy ASCII/Unicode tables
"""
import importlib.metadata

from .alignment import Alignment
from .merge import Merge
from .preset_style import PresetStyle
from .table_style import TableStyle
from .table_to_ascii import table2ascii

__version__ = importlib.metadata.version(__name__)

__all__ = [
    "Alignment",
    "Merge",
    "PresetStyle",
    "TableStyle",
    "table2ascii",
]
