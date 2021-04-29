from table2ascii import table2ascii as t2a, Styles


def test_thin():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=Styles.thin,
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
        style=Styles.thin_box,
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
        style=Styles.thin_rounded,
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
        style=Styles.thin_compact,
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
        style=Styles.thin_compact_rounded,
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
        style=Styles.thin_thick,
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
        style=Styles.thin_thick_rounded,
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
        style=Styles.thin_double,
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
        style=Styles.thin_double_rounded,
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
        style=Styles.thick,
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
        style=Styles.thick_box,
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
        style=Styles.thick_compact,
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
        style=Styles.double,
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
        style=Styles.double_box,
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
        style=Styles.double_compact,
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
        style=Styles.double_thin_compact,
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
        style=Styles.minimalist,
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
        style=Styles.borderless,
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
        style=Styles.simple,
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
        style=Styles.ascii,
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
        style=Styles.ascii_box,
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
        style=Styles.ascii_compact,
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
        style=Styles.ascii_double,
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
        style=Styles.ascii_minimalist,
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
        style=Styles.ascii_borderless,
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


def test_ascii_simple():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=Styles.ascii_simple,
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
        style=Styles.markdown,
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
