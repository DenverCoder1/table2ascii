import sys
from abc import abstractmethod
from typing import TYPE_CHECKING

try:
    from typing import Protocol, runtime_checkable
except ImportError:  # Python < 3.8
    from typing_extensions import Protocol, runtime_checkable

if TYPE_CHECKING:
    from typing import Protocol


@runtime_checkable
class SupportsStr(Protocol):
    """An ABC with one abstract method __str__."""

    @abstractmethod
    def __str__(self) -> str:
        pass
