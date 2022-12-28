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
        header=["Product", "Category", "Price", "Rating"],
        body=[
            ["Milk", "Dairy", "$2.99", "6.283"],
            ["Cheese", "Dairy", "$10.99", "8.2"],
            ["Apples", "Produce", "$0.99", "10.00"],
        ],
        column_widths=[12, 12, 12, 12],
        alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT, Alignment.DECIMAL],
    )

    print(output)

    """
    ╔═══════════════════════════════════════════════════╗
    ║ Product       Category         Price     Rating   ║
    ╟───────────────────────────────────────────────────╢
    ║ Milk           Dairy           $2.99      6.283   ║
    ║ Cheese         Dairy          $10.99      8.2     ║
    ║ Apples        Produce          $0.99     10.00    ║
    ╚═══════════════════════════════════════════════════╝
    """

Use a preset style
~~~~~~~~~~~~~~~~~~

.. code:: py

    from table2ascii import table2ascii, Alignment, PresetStyle

    output = table2ascii(
        header=["First", "Second", "Third", "Fourth"],
        body=[["10", "30", "40", "35"], ["20", "10", "20", "5"]],
        column_widths=[10, 10, 10, 10],
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

    output = table2ascii(
        header=["First", "Second", "Third", "Fourth"],
        body=[["10", "30", "40", "35"], ["20", "10", "20", "5"]],
        style=PresetStyle.plain,
        cell_padding=0,
        alignments=[Alignment.LEFT] * 4,
    )

    print(output)

    """
    First Second Third Fourth
    10    30     40    35
    20    10     20    5
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
        style=my_style,
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

Merge adjacent cells
~~~~~~~~~~~~~~~~~~~~

Check :ref:`Merge` for more info.

.. code:: py

    from table2ascii import table2ascii, Merge, PresetStyle

    output = table2ascii(
        header=["#", "G", "Merge", Merge.LEFT, "S"],
        body=[
            [1, 5, 6, 200, Merge.LEFT],
            [2, "E", "Long cell", Merge.LEFT, Merge.LEFT],
            ["Bonus", Merge.LEFT, Merge.LEFT, "F", "G"],
        ],
        footer=["SUM", "100", "200", Merge.LEFT, "300"],
        style=PresetStyle.double_thin_box,
        first_col_heading=True,
    )

    print(output)

    """
    ╔═════╦═════╤═══════╤═════╗
    ║  #  ║  G  │ Merge │  S  ║
    ╠═════╬═════╪═══╤═══╧═════╣
    ║  1  ║  5  │ 6 │   200   ║
    ╟─────╫─────┼───┴─────────╢
    ║  2  ║  E  │  Long cell  ║
    ╟─────╨─────┴───┬───┬─────╢
    ║     Bonus     │ F │  G  ║
    ╠═════╦═════╤═══╧═══╪═════╣
    ║ SUM ║ 100 │  200  │ 300 ║
    ╚═════╩═════╧═══════╧═════╝
    """
