from table2ascii import alignment, table2ascii as t2a, Alignment

import pytest


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
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_wrong_number_alignments():
    with pytest.raises(ValueError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["SUM", "130", "140", "135", "130"],
            first_col_heading=True,
            alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT],
        )


def test_invalid_alignments():
    with pytest.raises(ValueError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["SUM", "130", "140", "135", "130"],
            first_col_heading=True,
            alignments=[9999, -1, Alignment.RIGHT, Alignment.CENTER, Alignment.RIGHT],
        )


def test_alignment_numeric_data():
    text = t2a(
        header=[1, "G", "H", "R", "S"],
        body=[[1, 2, 3, 4, 5]],
        footer=["A", "B", 1, 2, 3],
        column_widths=[4, 5, 5, 4, 5],
        alignments=[Alignment.RIGHT] + [Alignment.CENTER] * 4,
        first_col_heading=True,
    )
    expected = (
        "╔════╦══════════════════════╗\n"
        "║  1 ║  G     H    R     S  ║\n"
        "╟────╫──────────────────────╢\n"
        "║  1 ║  2     3    4     5  ║\n"
        "╟────╫──────────────────────╢\n"
        "║  A ║  B     1    2     3  ║\n"
        "╚════╩══════════════════════╝"
    )
    assert text == expected
