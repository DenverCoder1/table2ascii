from .table_style import TableStyle


class PresetStyle:
    """
    Importable preset styles for more easily selecting a :ref:`TableStyle`.

    See the :ref:`Preset Styles<styles>` for more information on the available styles.

    Example::

        from table2ascii import PresetStyle

        output = table2ascii(
            ...
            style=PresetStyle.ascii_box
        )
    """

    thin = TableStyle.from_string("┌─┬─┐││ ├─┼─┤├─┼─┤└┴─┘")
    thin_box = TableStyle.from_string("┌─┬┬┐│││├─┼┼┤├─┼┼┤└┴┴┘")
    thin_rounded = TableStyle.from_string("╭─┬─╮││ ├─┼─┤├─┼─┤╰┴─╯")
    thin_compact = TableStyle.from_string("┌─┬─┐││ ├─┼─┤     └┴─┘")
    thin_compact_rounded = TableStyle.from_string("╭─┬─╮││ ├─┼─┤     ╰┴─╯")
    thin_thick = TableStyle.from_string("┌─┬─┐││ ┝━┿━┥├─┼─┤└┴─┘")
    thin_thick_rounded = TableStyle.from_string("╭─┬─╮││ ┝━┿━┥├─┼─┤╰┴─╯")
    thin_double = TableStyle.from_string("┌─┬─┐││ ╞═╪═╡├─┼─┤└┴─┘")
    thin_double_rounded = TableStyle.from_string("╭─┬─╮││ ╞═╪═╡├─┼─┤╰┴─╯")
    thick = TableStyle.from_string("┏━┳━┓┃┃ ┣━╋━┫┣━╋━┫┗┻━┛")
    thick_box = TableStyle.from_string("┏━┳┳┓┃┃┃┣━╋╋┫┣━╋╋┫┗┻┻┛")
    thick_compact = TableStyle.from_string("┏━┳━┓┃┃ ┣━╋━┫     ┗┻━┛")
    double = TableStyle.from_string("╔═╦═╗║║ ╠═╬═╣╠═╬═╣╚╩═╝")
    double_box = TableStyle.from_string("╔═╦╦╗║║║╠═╬╬╣╠═╬╬╣╚╩╩╝")
    double_compact = TableStyle.from_string("╔═╦═╗║║ ╠═╬═╣     ╚╩═╝")
    double_thin_compact = TableStyle.from_string("╔═╦═╗║║ ╟─╫─╢     ╚╩═╝")
    minimalist = TableStyle.from_string(" ───  │  ━━━  ───  ── ")
    borderless = TableStyle.from_string("      ┃  ━            ")
    simple = TableStyle.from_string(" ═    ║  ═            ")
    ascii = TableStyle.from_string("+-+-+|| +-+-++-+-+++-+")
    ascii_box = TableStyle.from_string("+-+++|||+-++++-+++++++")
    ascii_compact = TableStyle.from_string("+-+-+|| +-+-+     ++-+")
    ascii_double = TableStyle.from_string("+-+-+|| +=+=++-+-+++-+")
    ascii_minimalist = TableStyle.from_string(" ---  |  ===  ---  -- ")
    ascii_borderless = TableStyle.from_string("      |  -            ")
    ascii_simple = TableStyle.from_string(" =    |  =            ")
    ascii_rounded = TableStyle.from_string("/===\|| |=|=||-|-|\|=/")
    ascii_rounded_box = TableStyle.from_string("/===\||||=||||-|||\||/")
    markdown = TableStyle.from_string("     ||||-|||         ")
