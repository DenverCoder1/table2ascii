Usage
---------

Convert lists to ASCII tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from table2ascii import table2ascii

   output = table2ascii(
       header=["#", "G", "H", "R", "S"],
       body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
       footer=["SUM", "130", "140", "135", "130"],
   )

   print(output)

   """
   ╔═════════════════════════════╗
   ║  #     G     H     R     S  ║
   ╟─────────────────────────────╢
   ║  1    30    40    35    30  ║
   ║  2    30    40    35    30  ║
   ╟─────────────────────────────╢
   ║ SUM   130   140   135   130 ║
   ╚═════════════════════════════╝
   """

Set first or last column headings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from table2ascii import table2ascii

   output = table2ascii(
       body=[["Assignment", "30", "40", "35", "30"], ["Bonus", "10", "20", "5", "10"]],
       first_col_heading=True,
   )

   print(output)

   """
   ╔════════════╦═══════════════════╗
   ║ Assignment ║ 30   40   35   30 ║
   ║    Bonus   ║ 10   20    5   10 ║
   ╚════════════╩═══════════════════╝
   """

Set column widths and alignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

   from table2ascii import table2ascii, Alignment

   output = table2ascii(
       header=["#", "G", "H", "R", "S"],
       body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
       first_col_heading=True,
       column_widths=[5] * 5,  # [5, 5, 5, 5, 5]
       alignments=[Alignment.LEFT] + [Alignment.RIGHT] * 4, # First is left, remaining 4 are right
   )

   print(output)

   """
   ╔═════╦═══════════════════════╗
   ║ #   ║   G     H     R     S ║
   ╟─────╫───────────────────────╢
   ║ 1   ║  30    40    35    30 ║
   ║ 2   ║  30    40    35    30 ║
   ╚═════╩═══════════════════════╝
   """

Use a preset style
~~~~~~~~~~~~~~~~~~

.. code:: py

   from table2ascii import table2ascii, PresetStyle

   output = table2ascii(
       header=["First", "Second", "Third", "Fourth"],
       body=[["10", "30", "40", "35"], ["20", "10", "20", "5"]],
       column_widths=[10] * 4,
       style=PresetStyle.ascii_box
   )

   print(output)

   """
   +----------+----------+----------+----------+
   |  First   |  Second  |  Third   |  Fourth  |
   +----------+----------+----------+----------+
   |    10    |    30    |    40    |    35    |
   +----------+----------+----------+----------+
   |    20    |    10    |    20    |    5     |
   +----------+----------+----------+----------+
   """

Define a custom style
~~~~~~~~~~~~~~~~~~~~~

Check :ref:`TableStyle` for more info.

.. code:: py

   from table2ascii import table2ascii, TableStyle

   my_style = TableStyle.from_string("*-..*||:+-+:+     *''*")

   output = table2ascii(
       header=["First", "Second", "Third"],
       body=[["10", "30", "40"], ["20", "10", "20"], ["30", "20", "30"]],
       style=my_style
   )

   print(output)

   """
   *-------.--------.-------*
   | First : Second : Third |
   +-------:--------:-------+
   |  10   :   30   :  40   |
   |  20   :   10   :  20   |
   |  30   :   20   :  30   |
   *-------'--------'-------*
   """