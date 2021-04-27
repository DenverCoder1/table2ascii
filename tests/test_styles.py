from table2ascii import table2ascii as t2a, styles


def test_double_thin():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.double_thin,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║  1  ║ 30    40    35    30  ║\n"
        "║  2  ║ 30    40    35    30  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝\n"
    )
    assert text == expected


def test_thin():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.thin,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘\n"
        ""
    )
    assert text == expected


def test_thin_thick():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.thin_thick,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘\n"
    )
    assert text == expected


def test_thin_double():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.thin_double,
    )
    expected = (
        "┌─────┬───────────────────────┐\n"
        "│  #  │  G     H     R     S  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "╞═════╪═══════════════════════╡\n"
        "│ SUM │ 130   140   135   130 │\n"
        "└─────┴───────────────────────┘\n"
    )
    assert text == expected


def test_thin_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.thin_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "├─────┼───────────────────────┤\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "├─────┼───────────────────────┤\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯\n"
    )
    assert text == expected


def test_thin_thick_rounded():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=styles.thin_thick_rounded,
    )
    expected = (
        "╭─────┬───────────────────────╮\n"
        "│  #  │  G     H     R     S  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│  1  │ 30    40    35    30  │\n"
        "│  2  │ 30    40    35    30  │\n"
        "┝━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┥\n"
        "│ SUM │ 130   140   135   130 │\n"
        "╰─────┴───────────────────────╯\n"
    )
    assert text == expected
