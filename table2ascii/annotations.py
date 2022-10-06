from abc import abstractmethod
from typing import TYPE_CHECKING, runtime_checkable

try:
    # Python 3.8+
    from typing import Protocol
except ImportError:
    # Python 3.7
    from typing_extensions import Protocol

if TYPE_CHECKING:
    from typing import Protocol


@runtime_checkable
class SupportsStr(Protocol):
    """An ABC with one abstract method __str__."""

    __slots__ = ()

    @abstractmethod
    def __str__(self) -> str:
        pass