"""
table2ascii - Library for converting 2D Python lists to fancy ASCII/Unicode tables
"""
import sys

from .alignment import Alignment
from .merge import Merge
from .preset_style import PresetStyle
from .table_style import TableStyle
from .table_to_ascii import table2ascii

try:
    from importlib import metadata
except ImportError:  # Python < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

__all__ = [
    "Alignment",
    "Merge",
    "PresetStyle",
    "TableStyle",
    "table2ascii",
]
