.. currentmodule:: table2ascii

API Reference
=============

table2ascii
~~~~~~~~~~~

.. autofunction:: table2ascii

Alignment
~~~~~~~~~

.. autoenum:: Alignment
    :members:

.. _Merge:

Merge
~~~~~

.. autoenum:: Merge
    :members:

PresetStyle
~~~~~~~~~~~

.. autoclass:: PresetStyle
    :members:

.. _TableStyle:

TableStyle
~~~~~~~~~~

.. autoclass:: TableStyle
    :members:

Exceptions
~~~~~~~~~~

.. autoexception:: table2ascii.exceptions.Table2AsciiError

.. autoexception:: table2ascii.exceptions.TableOptionError

.. autoexception:: table2ascii.exceptions.ColumnCountMismatchError

.. autoexception:: table2ascii.exceptions.FooterColumnCountMismatchError

.. autoexception:: table2ascii.exceptions.BodyColumnCountMismatchError

.. autoexception:: table2ascii.exceptions.AlignmentCountMismatchError

.. autoexception:: table2ascii.exceptions.InvalidCellPaddingError

.. autoexception:: table2ascii.exceptions.ColumnWidthsCountMismatchError

.. autoexception:: table2ascii.exceptions.ColumnWidthTooSmallError

.. autoexception:: table2ascii.exceptions.InvalidColumnWidthError

.. autoexception:: table2ascii.exceptions.InvalidAlignmentError

.. autoexception:: table2ascii.exceptions.TableStyleTooLongError

Warnings
~~~~~~~~

.. autoclass:: table2ascii.exceptions.TableStyleTooShortWarning
