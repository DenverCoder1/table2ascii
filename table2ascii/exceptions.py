from __future__ import annotations
from typing import Any

from .alignment import Alignment

from .annotations import SupportsStr


class Table2AsciiError(Exception):
    """Base class for all table2ascii exceptions"""

    def _message(self):
        """Return the error message"""
        raise NotImplementedError


class TableOptionError(Table2AsciiError, ValueError):
    """Base class for exceptions raised when an invalid option
    is passed when creating an ascii table

    This class is a subclass of :class:`Table2AsciiError` and :class:`ValueError`.
    """


class ColumnCountMismatchError(TableOptionError):
    """Base class for exceptions raised when a parameter has an
    invalid number of columns

    This class is a subclass of :class:`TableOptionError`.
    """

    expected_columns: int


class FooterColumnCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of columns in the footer
    does not match the number of columns in the header

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        footer (list[SupportsStr]): The footer that caused the error
        expected_columns (int): The number of columns that were expected
    """

    def __init__(self, footer: list[SupportsStr], expected_columns: int):
        self.footer = footer
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self):
        return (
            f"Footer column count mismatch: {len(self.footer)} columns "
            f"found, expected {self.expected_columns}."
        )


class BodyColumnCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of columns in the body
    does not match the number of columns in the footer or header

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        body (list[list[SupportsStr]]): The body that caused the error
        expected_columns (int): The number of columns that were expected
        first_invalid_row (list[SupportsStr]): The first row with an invalid column count
    """

    def __init__(self, body: list[list[SupportsStr]], expected_columns: int):
        self.body = body
        self.expected_columns = expected_columns
        self.first_invalid_row = next(
            (row for row in self.body if len(row) != self.expected_columns)
        )
        super().__init__(self._message())

    def _message(self):
        return (
            f"Body column count mismatch: A row with {len(self.first_invalid_row)} "
            f"columns was found, expected {self.expected_columns}."
        )


class AlignmentCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of alignments does not match
    the number of columns in the table

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        alignments (list[Alignment]): The alignments that caused the error
        expected_columns (int): The number of columns that were expected
    """

    def __init__(self, alignments: list[Alignment], expected_columns: int):
        self.alignments = alignments
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self):
        return (
            f"Alignment count mismatch: {len(self.alignments)} alignments "
            f"found, expected {self.expected_columns}."
        )


class ColumnWidthsCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of column widths does not match
    the number of columns in the table

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        column_widths (list[Optional[int]]): The column widths that caused the error
        expected_columns (int): The number of columns that were expected
    """

    def __init__(self, column_widths: list[int | None], expected_columns: int):
        self.column_widths = column_widths
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self):
        return (
            f"Column widths count mismatch: {len(self.column_widths)} column widths "
            f"found, expected {self.expected_columns}."
        )


class InvalidCellPaddingError(TableOptionError):
    """Exception raised when the cell padding is invalid

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        padding (int): The padding that caused the error
    """

    def __init__(self, padding: int):
        self.padding = padding
        super().__init__(self._message())

    def _message(self):
        return f"Invalid cell padding: {self.padding} is not a positive integer."


class ColumnWidthTooSmallError(TableOptionError):
    """Exception raised when the column width is smaller than the minimum
    number of characters that are required to display the content

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        column_index (int): The index of the column that caused the error
        column_width (int): The column width that caused the error
        min_width (int): The minimum width that is allowed
    """

    def __init__(self, column_index: int, column_width: int, min_width: int):
        self.column_index = column_index
        self.column_width = column_width
        self.min_width = min_width
        super().__init__(self._message())

    def _message(self):
        return (
            f"Column width too small: The column width for column index {self.column_index} "
            f" of `column_widths` is {self.column_width}, but the minimum width "
            f"required to display the content is {self.min_width}."
        )


class InvalidAlignmentError(TableOptionError):
    """Exception raised when an invalid value is passed for an :class:`Alignment`

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        alignment (Any): The alignment value that caused the error
    """

    def __init__(self, alignment: Any):
        self.alignment = alignment
        super().__init__(self._message())

    def _message(self):
        return (
            f"Invalid alignment: {self.alignment!r} is not a valid alignment. "
            f"Valid alignments are: {', '.join(a.__repr__() for a in Alignment)}"
        )