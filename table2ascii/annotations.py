import sys
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING or sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


@runtime_checkable
class SupportsStr(Protocol):
    """An abstract base class (ABC) with one abstract method :meth:`__str__`"""

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the object"""
        pass
