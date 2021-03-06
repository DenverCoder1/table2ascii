import pytest

from table2ascii import Alignment, table2ascii as t2a


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
            alignments=[9999, -1, Alignment.RIGHT, Alignment.CENTER, Alignment.RIGHT],  # type: ignore
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


def test_alignments_multiline_data():
    text = t2a(
        header=["Multiline\nHeader\nCell", "G", "Two\nLines", "R", "S"],
        body=[[1, "Alpha\nBeta\nGamma", 3, 4, "One\nTwo"]],
        footer=["A", "Footer\nBreak", 1, "Second\nCell\nBroken", 3],
        alignments=[
            Alignment.LEFT,
            Alignment.RIGHT,
            Alignment.CENTER,
            Alignment.LEFT,
            Alignment.CENTER,
        ],
    )
    expected = (
        "╔═══════════════════════════════════════════╗\n"
        "║ Multiline        G    Two    R         S  ║\n"
        "║ Header               Lines                ║\n"
        "║ Cell                                      ║\n"
        "╟───────────────────────────────────────────╢\n"
        "║ 1            Alpha     3     4        One ║\n"
        "║               Beta                    Two ║\n"
        "║              Gamma                        ║\n"
        "╟───────────────────────────────────────────╢\n"
        "║ A           Footer     1     Second    3  ║\n"
        "║              Break           Cell         ║\n"
        "║                              Broken       ║\n"
        "╚═══════════════════════════════════════════╝"
    )
    assert text == expected
