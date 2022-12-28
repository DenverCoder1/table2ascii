"""
table2ascii - Library for converting 2D Python lists to fancy ASCII/Unicode tables
"""
import sys

from .alignment import Alignment
from .merge import Merge
from .preset_style import PresetStyle
from .table_style import TableStyle
from .table_to_ascii import table2ascii

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

__all__ = [
    "Alignment",
    "Merge",
    "PresetStyle",
    "TableStyle",
    "table2ascii",
]
