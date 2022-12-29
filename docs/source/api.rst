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

.. autoexception:: Table2AsciiError

.. autoexception:: TableOptionError

.. autoexception:: ColumnCountMismatchError

.. autoexception:: FooterColumnCountMismatchError

.. autoexception:: BodyColumnCountMismatchError

.. autoexception:: AlignmentCountMismatchError

.. autoexception:: InvalidCellPaddingError

.. autoexception:: ColumnWidthsCountMismatchError

.. autoexception:: ColumnWidthTooSmallError

.. autoexception:: InvalidColumnWidthError

.. autoexception:: InvalidAlignmentError

.. autoexception:: TableStyleTooLongError

Warnings
~~~~~~~~

.. autoclass:: TableStyleTooShortWarning

Annotations
~~~~~~~~~~~

.. autoclass:: SupportsStr
    
    .. automethod:: SupportsStr.__str__
