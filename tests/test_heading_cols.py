from table2ascii import table2ascii as t2a


def test_first_column_heading():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
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


def test_first_column_heading_body_only():
    text = t2a(
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        first_col_heading=True,
    )
    expected = (
        "╔═══╦═══════════════════╗\n"
        "║ 1 ║ 30   40   35   30 ║\n"
        "║ 2 ║ 30   40   35   30 ║\n"
        "╚═══╩═══════════════════╝"
    )
    assert text == expected


def test_last_column_heading():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=False,
        last_col_heading=True,
    )
    expected = (
        "╔═══════════════════════╦═════╗\n"
        "║  #     G     H     R  ║  S  ║\n"
        "╟───────────────────────╫─────╢\n"
        "║  1    30    40    35  ║ 30  ║\n"
        "║  2    30    40    35  ║ 30  ║\n"
        "╟───────────────────────╫─────╢\n"
        "║ SUM   130   140   135 ║ 130 ║\n"
        "╚═══════════════════════╩═════╝"
    )
    assert text == expected


def test_last_column_heading_body_only():
    text = t2a(
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        last_col_heading=True,
    )
    expected = (
        "╔══════════════════╦════╗\n"
        "║ 1   30   40   35 ║ 30 ║\n"
        "║ 2   30   40   35 ║ 30 ║\n"
        "╚══════════════════╩════╝"
    )
    assert text == expected


def test_both_column_heading():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=True,
    )
    expected = (
        "╔═════╦═════════════════╦═════╗\n"
        "║  #  ║  G     H     R  ║  S  ║\n"
        "╟─────╫─────────────────╫─────╢\n"
        "║  1  ║ 30    40    35  ║ 30  ║\n"
        "║  2  ║ 30    40    35  ║ 30  ║\n"
        "╟─────╫─────────────────╫─────╢\n"
        "║ SUM ║ 130   140   135 ║ 130 ║\n"
        "╚═════╩═════════════════╩═════╝"
    )
    assert text == expected


def test_neither_column_heading():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=False,
        last_col_heading=False,
    )
    expected = (
        "╔═════════════════════════════╗\n"
        "║  #     G     H     R     S  ║\n"
        "╟─────────────────────────────╢\n"
        "║  1    30    40    35    30  ║\n"
        "║  2    30    40    35    30  ║\n"
        "╟─────────────────────────────╢\n"
        "║ SUM   130   140   135   130 ║\n"
        "╚═════════════════════════════╝"
    )
    assert text == expected
