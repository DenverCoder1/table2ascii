import sys
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING or sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


@runtime_checkable
class SupportsStr(Protocol):
    """An ABC with one abstract method __str__."""

    @abstractmethod
    def __str__(self) -> str:
        pass
