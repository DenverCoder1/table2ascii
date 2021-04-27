from table2ascii import table2ascii as t2a, Alignment


def test_first_left_four_right():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        alignments=[Alignment.LEFT] + [Alignment.RIGHT] * 4,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║ #   ║   G     H     R     S ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ 1   ║  30    40    35    30 ║\n"
        "║ 2   ║  30    40    35    30 ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝\n"
    )
    assert text == expected
