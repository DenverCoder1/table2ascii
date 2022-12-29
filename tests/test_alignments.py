import pytest

from table2ascii import Alignment, PresetStyle, table2ascii as t2a
from table2ascii.exceptions import AlignmentCountMismatchError, InvalidAlignmentError


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


def test_wrong_number_of_alignments():
    with pytest.raises(AlignmentCountMismatchError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["SUM", "130", "140", "135", "130"],
            first_col_heading=True,
            alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT],
        )


def test_invalid_alignments():
    with pytest.raises(InvalidAlignmentError):
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


def test_decimal_alignment():
    text = t2a(
        header=["1.1.1", "G", "Long Header", "H", "R", "３.８"],
        body=[[100.00001, 2, 3.14, 33, "AB", "1.5"], [10.0001, 22.0, 2.718, 3, "CD", "３.０３"]],
        footer=[10000.01, "123", 10.0, 0, "E", "A"],
        alignments=[Alignment.DECIMAL] * 6,
        first_col_heading=True,
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════════════╦═══════╤═════════════╤════╤════╤═════════╗\n"
        "║    1.1.1    ║   G   │ Long Header │ H  │ R  │ ３.８   ║\n"
        "╠═════════════╬═══════╪═════════════╪════╪════╪═════════╣\n"
        "║   100.00001 ║   2   │    3.14     │ 33 │ AB │  1.5    ║\n"
        "╟─────────────╫───────┼─────────────┼────┼────┼─────────╢\n"
        "║    10.0001  ║  22.0 │    2.718    │  3 │ CD │ ３.０３ ║\n"
        "╠═════════════╬═══════╪═════════════╪════╪════╪═════════╣\n"
        "║ 10000.01    ║ 123   │   10.0      │  0 │ E  │    A    ║\n"
        "╚═════════════╩═══════╧═════════════╧════╧════╧═════════╝"
    )
    assert text == expected


def test_single_decimal_alignment():
    text = t2a(
        header=["1.1.1", "G", "Long Header"],
        body=[[100.00001, 2, 3.14], [10.0001, 22.0, 2.718]],
        alignments=Alignment.DECIMAL,
    )
    expected = (
        "╔════════════════════════════════╗\n"
        "║   1.1.1      G     Long Header ║\n"
        "╟────────────────────────────────╢\n"
        "║ 100.00001    2        3.14     ║\n"
        "║  10.0001    22.0      2.718    ║\n"
        "╚════════════════════════════════╝"
    )
    assert text == expected


def test_single_left_alignment():
    text = t2a(
        header=["1.1.1", "G", "Long Header"],
        body=[[100.00001, 2, 3.14], [10.0001, 22.0, 2.718]],
        alignments=Alignment.LEFT,
    )
    expected = (
        "╔════════════════════════════════╗\n"
        "║ 1.1.1       G      Long Header ║\n"
        "╟────────────────────────────────╢\n"
        "║ 100.00001   2      3.14        ║\n"
        "║ 10.0001     22.0   2.718       ║\n"
        "╚════════════════════════════════╝"
    )
    assert text == expected


def test_number_alignments():
    text = t2a(
        header=["1.1.1", "G", "Long Header", "Another Long Header"],
        body=[[100.00001, 2, 3.14, 6.28], [10.0001, 22.0, 2.718, 1.618]],
        alignments=[Alignment.LEFT, Alignment.RIGHT, Alignment.CENTER, Alignment.RIGHT],
        number_alignments=[Alignment.DECIMAL, Alignment.LEFT, Alignment.RIGHT, Alignment.DECIMAL],
    )
    expected = (
        "╔══════════════════════════════════════════════════════╗\n"
        "║ 1.1.1          G   Long Header   Another Long Header ║\n"
        "╟──────────────────────────────────────────────────────╢\n"
        "║ 100.00001   2             3.14                 6.28  ║\n"
        "║  10.0001    22.0         2.718                 1.618 ║\n"
        "╚══════════════════════════════════════════════════════╝"
    )
    assert text == expected


def test_single_number_alignments():
    text = t2a(
        header=["1.1.1", "G", "Long Header", "S"],
        body=[[100.00001, 2, 3.14, 6.28], [10.0001, 22.0, 2.718, 1.618]],
        alignments=[Alignment.LEFT, Alignment.CENTER, Alignment.CENTER, Alignment.RIGHT],
        number_alignments=Alignment.RIGHT,
    )
    expected = (
        "╔════════════════════════════════════════╗\n"
        "║ 1.1.1        G     Long Header       S ║\n"
        "╟────────────────────────────────────────╢\n"
        "║ 100.00001      2          3.14    6.28 ║\n"
        "║   10.0001   22.0         2.718   1.618 ║\n"
        "╚════════════════════════════════════════╝"
    )
    assert text == expected
