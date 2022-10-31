from table2ascii import PresetStyle, table2ascii as t2a


def test_thin():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘"
    )
    assert text == expected


def test_thin_box():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_box,
    )
    expected = (
        "┌─────┬─────┬─────┬─────┬─────┐\n"
        "│  #  │  G  │  H  │  R  │  S  │\n"
        "├─────┼─────┼─────┼─────┼─────┤\n"
        "│  1  │ 30  │ 40  │ 35  │ 30  │\n"
        "├─────┼─────┼─────┼─────┼─────┤\n"
        "│  2  │ 30  │ 40  │ 35  │ 30  │\n"
        "├─────┼─────┼─────┼─────┼─────┤\n"
        "│ SUM │ 130 │ 140 │ 135 │ 130 │\n"
        "└─────┴─────┴─────┴─────┴─────┘"
    )
    assert text == expected


def test_thin_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯"
    )
    assert text == expected


def test_thin_compact():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_compact,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘"
    )
    assert text == expected


def test_thin_compact_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_compact_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯"
    )
    assert text == expected


def test_thin_thick():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_thick,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘"
    )
    assert text == expected


def test_thin_thick_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_thick_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯"
    )
    assert text == expected


def test_thin_double():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_double,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘"
    )
    assert text == expected


def test_thin_double_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thin_double_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│  1  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│  2  │ 30    40    35    30  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯"
    )
    assert text == expected


def test_thick():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thick,
    )
    expected = (
        "┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        "┃  #  ┃  G     H     R     S  ┃\n"
        "┣━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        "┃  1  ┃ 30    40    35    30  ┃\n"
        "┣━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        "┃  2  ┃ 30    40    35    30  ┃\n"
        "┣━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        "┃ SUM ┃ 130   140   135   130 ┃\n"
        "┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┛"
    )
    assert text == expected


def test_thick_box():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thick_box,
    )
    expected = (
        "┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓\n"
        "┃  #  ┃  G  ┃  H  ┃  R  ┃  S  ┃\n"
        "┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫\n"
        "┃  1  ┃ 30  ┃ 40  ┃ 35  ┃ 30  ┃\n"
        "┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫\n"
        "┃  2  ┃ 30  ┃ 40  ┃ 35  ┃ 30  ┃\n"
        "┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫\n"
        "┃ SUM ┃ 130 ┃ 140 ┃ 135 ┃ 130 ┃\n"
        "┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛"
    )
    assert text == expected


def test_thick_compact():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.thick_compact,
    )
    expected = (
        "┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓\n"
        "┃  #  ┃  G     H     R     S  ┃\n"
        "┣━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        "┃  1  ┃ 30    40    35    30  ┃\n"
        "┃  2  ┃ 30    40    35    30  ┃\n"
        "┣━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫\n"
        "┃ SUM ┃ 130   140   135   130 ┃\n"
        "┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┛"
    )
    assert text == expected


def test_double():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.double,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╠═════╬═══════════════════════╣\n"
        "║  1  ║ 30    40    35    30  ║\n"
        "╠═════╬═══════════════════════╣\n"
        "║  2  ║ 30    40    35    30  ║\n"
        "╠═════╬═══════════════════════╣\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_double_box():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.double_box,
    )
    expected = (
        "╔═════╦═════╦═════╦═════╦═════╗\n"
        "║  #  ║  G  ║  H  ║  R  ║  S  ║\n"
        "╠═════╬═════╬═════╬═════╬═════╣\n"
        "║  1  ║ 30  ║ 40  ║ 35  ║ 30  ║\n"
        "╠═════╬═════╬═════╬═════╬═════╣\n"
        "║  2  ║ 30  ║ 40  ║ 35  ║ 30  ║\n"
        "╠═════╬═════╬═════╬═════╬═════╣\n"
        "║ SUM ║ 130 ║ 140 ║ 135 ║ 130 ║\n"
        "╚═════╩═════╩═════╩═════╩═════╝"
    )
    assert text == expected


def test_double_compact():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.double_compact,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╠═════╬═══════════════════════╣\n"
        "║  1  ║ 30    40    35    30  ║\n"
        "║  2  ║ 30    40    35    30  ║\n"
        "╠═════╬═══════════════════════╣\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_double_thin_compact():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.double_thin_compact,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║  1  ║ 30    40    35    30  ║\n"
        "║  2  ║ 30    40    35    30  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_minimalist():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.minimalist,
    )
    expected = (
        " ───────────────────────────── \n"
        "   #  │  G     H     R     S   \n"
        " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n"
        "   1  │ 30    40    35    30   \n"
        " ───────────────────────────── \n"
        "   2  │ 30    40    35    30   \n"
        " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n"
        "  SUM │ 130   140   135   130  \n"
        " ───────────────────────────── "
    )
    assert text == expected


def test_borderless():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.borderless,
    )
    expected = (
        "   #  ┃  G     H     R     S   \n"
        " ━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━ \n"
        "   1  ┃ 30    40    35    30   \n"
        "   2  ┃ 30    40    35    30   \n"
        " ━━━━━ ━━━━━ ━━━━━ ━━━━━ ━━━━━ \n"
        "  SUM ┃ 130   140   135   130  "
    )
    assert text == expected


def test_simple():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.simple,
    )
    expected = (
        " ═════ ═════ ═════ ═════ ═════ \n"
        "   #  ║  G     H     R     S   \n"
        " ═════ ═════ ═════ ═════ ═════ \n"
        "   1  ║ 30    40    35    30   \n"
        "   2  ║ 30    40    35    30   \n"
        " ═════ ═════ ═════ ═════ ═════ \n"
        "  SUM ║ 130   140   135   130  \n"
        " ═════ ═════ ═════ ═════ ═════ "
    )
    assert text == expected


def test_ascii():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii,
    )
    expected = (
        "+-----+-----------------------+\n"
        "|  #  |  G     H     R     S  |\n"
        "+-----+-----------------------+\n"
        "|  1  | 30    40    35    30  |\n"
        "+-----+-----------------------+\n"
        "|  2  | 30    40    35    30  |\n"
        "+-----+-----------------------+\n"
        "| SUM | 130   140   135   130 |\n"
        "+-----+-----------------------+"
    )
    assert text == expected


def test_ascii_box():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_box,
    )
    expected = (
        "+-----+-----+-----+-----+-----+\n"
        "|  #  |  G  |  H  |  R  |  S  |\n"
        "+-----+-----+-----+-----+-----+\n"
        "|  1  | 30  | 40  | 35  | 30  |\n"
        "+-----+-----+-----+-----+-----+\n"
        "|  2  | 30  | 40  | 35  | 30  |\n"
        "+-----+-----+-----+-----+-----+\n"
        "| SUM | 130 | 140 | 135 | 130 |\n"
        "+-----+-----+-----+-----+-----+"
    )
    assert text == expected


def test_ascii_compact():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_compact,
    )
    expected = (
        "+-----+-----------------------+\n"
        "|  #  |  G     H     R     S  |\n"
        "+-----+-----------------------+\n"
        "|  1  | 30    40    35    30  |\n"
        "|  2  | 30    40    35    30  |\n"
        "+-----+-----------------------+\n"
        "| SUM | 130   140   135   130 |\n"
        "+-----+-----------------------+"
    )
    assert text == expected


def test_ascii_double():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_double,
    )
    expected = (
        "+-----+-----------------------+\n"
        "|  #  |  G     H     R     S  |\n"
        "+=====+=======================+\n"
        "|  1  | 30    40    35    30  |\n"
        "+-----+-----------------------+\n"
        "|  2  | 30    40    35    30  |\n"
        "+=====+=======================+\n"
        "| SUM | 130   140   135   130 |\n"
        "+-----+-----------------------+"
    )
    assert text == expected


def test_ascii_minimalist():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_minimalist,
    )
    expected = (
        " ----------------------------- \n"
        "   #  |  G     H     R     S   \n"
        " ============================= \n"
        "   1  | 30    40    35    30   \n"
        " ----------------------------- \n"
        "   2  | 30    40    35    30   \n"
        " ============================= \n"
        "  SUM | 130   140   135   130  \n"
        " ----------------------------- "
    )
    assert text == expected


def test_ascii_borderless():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_borderless,
    )
    expected = (
        "   #  |  G     H     R     S   \n"
        " ----- ----- ----- ----- ----- \n"
        "   1  | 30    40    35    30   \n"
        "   2  | 30    40    35    30   \n"
        " ----- ----- ----- ----- ----- \n"
        "  SUM | 130   140   135   130  "
    )
    assert text == expected


def test_ascii_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_rounded,
    )
    expected = (
        "/=============================\\\n"
        "|  #  |  G     H     R     S  |\n"
        "|=====|=======================|\n"
        "|  1  | 30    40    35    30  |\n"
        "|-----|-----------------------|\n"
        "|  2  | 30    40    35    30  |\n"
        "|=====|=======================|\n"
        "| SUM | 130   140   135   130 |\n"
        "\\=====|=======================/"
    )
    assert text == expected


def test_ascii_rounded_box():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_rounded_box,
    )
    expected = (
        "/=============================\\\n"
        "|  #  |  G  |  H  |  R  |  S  |\n"
        "|=====|=====|=====|=====|=====|\n"
        "|  1  | 30  | 40  | 35  | 30  |\n"
        "|-----|-----|-----|-----|-----|\n"
        "|  2  | 30  | 40  | 35  | 30  |\n"
        "|=====|=====|=====|=====|=====|\n"
        "| SUM | 130 | 140 | 135 | 130 |\n"
        "\\=====|=====|=====|=====|=====/"
    )
    assert text == expected


def test_ascii_simple():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.ascii_simple,
    )
    expected = (
        " ===== ===== ===== ===== ===== \n"
        "   #  |  G     H     R     S   \n"
        " ===== ===== ===== ===== ===== \n"
        "   1  | 30    40    35    30   \n"
        "   2  | 30    40    35    30   \n"
        " ===== ===== ===== ===== ===== \n"
        "  SUM | 130   140   135   130  \n"
        " ===== ===== ===== ===== ===== "
    )
    assert text == expected


def test_markdown():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.markdown,
    )
    expected = (
        "|  #  |  G  |  H  |  R  |  S  |\n"
        "|-----|-----|-----|-----|-----|\n"
        "|  1  | 30  | 40  | 35  | 30  |\n"
        "|  2  | 30  | 40  | 35  | 30  |\n"
        "|-----|-----|-----|-----|-----|\n"
        "| SUM | 130 | 140 | 135 | 130 |"
    )
    assert text == expected


def test_plain():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=PresetStyle.plain,
    )
    expected = (
        "  #     G     H     R     S  \n"
        "  1    30    40    35    30  \n"
        "  2    30    40    35    30  \n"
        " SUM   130   140   135   130 "
    )
    assert text == expected
