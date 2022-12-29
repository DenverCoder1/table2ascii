from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from .alignment import Alignment
from .annotations import SupportsStr


class Table2AsciiError(Exception):
    """Base class for all table2ascii exceptions"""

    def _message(self) -> str:
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
        footer (:class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]):
            The footer that caused the error
        expected_columns (:class:`int`): The number of columns that were expected
    """

    def __init__(self, footer: Sequence[SupportsStr], expected_columns: int):
        self.footer = footer
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Footer column count mismatch: {len(self.footer)} columns "
            f"found, expected {self.expected_columns}."
        )


class BodyColumnCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of columns in the body
    does not match the number of columns in the footer or header

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        body (:class:`Sequence <collections.abc.Sequence>`\ [\ :class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]]):
            The body that caused the error
        expected_columns (:class:`int`): The number of columns that were expected
        first_invalid_row (:class:`Sequence <collections.abc.Sequence>`\ [:class:`SupportsStr`]):
            The first row with an invalid column count
    """

    def __init__(self, body: Sequence[Sequence[SupportsStr]], expected_columns: int):
        self.body = body
        self.expected_columns = expected_columns
        self.first_invalid_row = next(
            (row for row in self.body if len(row) != self.expected_columns)
        )
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Body column count mismatch: A row with {len(self.first_invalid_row)} "
            f"columns was found, expected {self.expected_columns}."
        )


class AlignmentCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of alignments does not match
    the number of columns in the table

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        alignments (:class:`Sequence <collections.abc.Sequence>`\ [:class:`Alignment`]):
            The alignments that caused the error
        expected_columns (:class:`int`): The number of columns that were expected
    """

    def __init__(self, alignments: Sequence[Alignment], expected_columns: int):
        self.alignments = alignments
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Alignment count mismatch: {len(self.alignments)} alignments "
            f"found, expected {self.expected_columns}."
        )


class ColumnWidthsCountMismatchError(ColumnCountMismatchError):
    """Exception raised when the number of column widths does not match
    the number of columns in the table

    This class is a subclass of :class:`ColumnCountMismatchError`.

    Attributes:
        column_widths (:class:`Sequence <collections.abc.Sequence>`\ [:data:`Optional <typing.Optional>`\ [:class:`int`]]):
            The column widths that caused the error
        expected_columns (:class:`int`): The number of columns that were expected
    """

    def __init__(self, column_widths: Sequence[int | None], expected_columns: int):
        self.column_widths = column_widths
        self.expected_columns = expected_columns
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Column widths count mismatch: {len(self.column_widths)} column widths "
            f"found, expected {self.expected_columns}."
        )


class NoHeaderBodyOrFooterError(TableOptionError):
    """Exception raised when no header, body or footer is provided

    This class is a subclass of :class:`TableOptionError`.
    """

    def __init__(self):
        super().__init__(self._message())

    def _message(self) -> str:
        return "At least one of header, body or footer must be provided."


class InvalidCellPaddingError(TableOptionError):
    """Exception raised when the cell padding is invalid

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        padding (:class:`int`): The padding that caused the error
    """

    def __init__(self, padding: int):
        self.padding = padding
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Invalid cell padding: The cell padding provided was {self.padding} "
            f"but it must be a non-negative integer."
        )


class ColumnWidthTooSmallError(TableOptionError):
    """Exception raised when the column width is smaller than the minimum
    number of characters that are required to display the content

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        column_index (:class:`int`): The index of the column that caused the error
        column_width (:class:`int`): The column width that caused the error
        min_width (:class:`int`): The minimum width that is allowed
    """

    def __init__(self, column_index: int, column_width: int, min_width: int | None = None):
        self.column_index = column_index
        self.column_width = column_width
        self.min_width = min_width
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Column width too small: The column width for index {self.column_index} "
            f"of `column_widths` is {self.column_width}, but the minimum width "
            f"required to display the content is {self.min_width}."
        )


class InvalidColumnWidthError(ColumnWidthTooSmallError):
    """Exception raised when the column width is invalid

    This class is a subclass of :class:`ColumnWidthTooSmallError`.
    """

    def _message(self) -> str:
        return (
            f"Invalid column width: The column width for index {self.column_index} "
            f"of `column_widths` is {self.column_width}, but the column width "
            f"must be a positive integer."
        )


class InvalidAlignmentError(TableOptionError):
    """Exception raised when an invalid value is passed for an :class:`Alignment`

    This class is a subclass of :class:`TableOptionError`.

    Attributes:
        alignment (:data:`Any <typing.Any>`): The alignment value that caused the error
    """

    def __init__(self, alignment: Any):
        self.alignment = alignment
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Invalid alignment: {self.alignment!r} is not a valid alignment. "
            f"Valid alignments are: {', '.join(a.__repr__() for a in Alignment)}"
        )


class TableStyleTooLongError(Table2AsciiError, ValueError):
    """Exception raised when the number of characters passed in the string
    for creating the table style exceeds the number of parameters that the
    table style accepts

    This class is a subclass of :class:`Table2AsciiError` and :class:`ValueError`.

    Attributes:
        string (:class:`str`): The string that caused the error
        max_characters (:class:`int`): The maximum number of characters that are allowed
    """

    def __init__(self, string: str, max_characters: int):
        self.string = string
        self.max_characters = max_characters
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Too many characters for table style: {len(self.string)} characters "
            f"found, but the maximum number of characters allowed is {self.max_characters}."
        )


class TableStyleTooShortWarning(UserWarning):
    """Warning raised when the number of characters passed in the string
    for creating the table style is fewer than the number of parameters
    that the table style accepts

    This class is a subclass of :class:`UserWarning`.

    It can be silenced using :func:`warnings.filterwarnings`.

    Attributes:
        string (:class:`str`): The string that caused the warning
        max_characters (:class:`int`): The number of characters that :class:`TableStyle` accepts
    """

    def __init__(self, string: str, max_characters: int):
        self.string = string
        self.max_characters = max_characters
        super().__init__(self._message())

    def _message(self) -> str:
        return (
            f"Too few characters for table style: {len(self.string)} characters "
            f"found, but table styles can accept {self.max_characters} characters. "
            f"Missing characters will be replaced with spaces."
        )
