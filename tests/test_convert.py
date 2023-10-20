import pytest

from table2ascii import table2ascii as t2a
from table2ascii.exceptions import (
    BodyColumnCountMismatchError,
    FooterColumnCountMismatchError,
    NoHeaderBodyOrFooterError,
)


def test_header_body_footer():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
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


def test_body_footer():
    text = t2a(
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  1  ║ 30    40    35    30  ║\n"
        "║  2  ║ 30    40    35    30  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_header_body():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        first_col_heading=True,
    )
    expected = (
        "╔═══╦═══════════════════╗\n"
        "║ # ║ G    H    R    S  ║\n"
        "╟───╫───────────────────╢\n"
        "║ 1 ║ 30   40   35   30 ║\n"
        "║ 2 ║ 30   40   35   30 ║\n"
        "╚═══╩═══════════════════╝"
    )
    assert text == expected


def test_header_footer():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╟─────╫───────────────────────╢\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_header():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        first_col_heading=True,
    )
    expected = (
        "╔═══╦═══════════════╗\n"
        "║ # ║ G   H   R   S ║\n"
        "╟───╫───────────────╢\n"
        "╚═══╩═══════════════╝"
    )
    assert text == expected


def test_body():
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


def test_footer():
    text = t2a(
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_no_header_body_or_footer():
    with pytest.raises(NoHeaderBodyOrFooterError):
        t2a()


def test_header_footer_unequal():
    with pytest.raises(FooterColumnCountMismatchError):
        t2a(
            header=["H", "R", "S"],
            footer=["SUM", "130", "140", "135", "130"],
            first_col_heading=True,
        )


def test_header_body_unequal():
    with pytest.raises(BodyColumnCountMismatchError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[
                ["0", "45", "30", "32", "28"],
                ["1", "30", "40", "35", "30", "36"],
                ["2", "30", "40", "35", "30"],
            ],
            first_col_heading=True,
        )


def test_footer_body_unequal():
    with pytest.raises(BodyColumnCountMismatchError):
        t2a(
            body=[
                ["0", "45", "30", "32", "28"],
                ["1", "30", "40", "35", "30"],
                ["2", "30", "40", "35", "30"],
            ],
            footer=["SUM", "130", "140", "135", "130", "36"],
            first_col_heading=True,
        )


def test_empty_header():
    text = t2a(
        header=[],
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


def test_empty_body():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[],
        first_col_heading=True,
    )
    expected = (
        "╔═══╦═══════════════╗\n"
        "║ # ║ G   H   R   S ║\n"
        "╟───╫───────────────╢\n"
        "╚═══╩═══════════════╝"
    )
    assert text == expected


def test_numeric_data():
    text = t2a(
        header=[1, "G", "H", "R", "S"],
        body=[[1, 2, 3, 4, 5]],
        footer=["A", "B", 1, 2, 3],
        column_widths=[4, 5, 5, 4, 5],
        first_col_heading=True,
    )
    expected = (
        "╔════╦══════════════════════╗\n"
        "║ 1  ║  G     H    R     S  ║\n"
        "╟────╫──────────────────────╢\n"
        "║ 1  ║  2     3    4     5  ║\n"
        "╟────╫──────────────────────╢\n"
        "║ A  ║  B     1    2     3  ║\n"
        "╚════╩══════════════════════╝"
    )
    assert text == expected


def test_stringifiable_classes():
    class Foo:
        def __str__(self):
            return "Foo"

    text = t2a(
        header=[1, Foo(), None],
        body=[[1, Foo(), None]],
        footer=[1, Foo(), None],
        first_col_heading=True,
    )
    expected = (
        "╔═══╦════════════╗\n"
        "║ 1 ║ Foo   None ║\n"
        "╟───╫────────────╢\n"
        "║ 1 ║ Foo   None ║\n"
        "╟───╫────────────╢\n"
        "║ 1 ║ Foo   None ║\n"
        "╚═══╩════════════╝"
    )
    assert text == expected


def test_multiline_cells():
    text = t2a(
        header=["Multiline\nHeader\nCell", "G", "Two\nLines", "R", "S"],
        body=[[1, "Alpha\nBeta\nGamma", 3, 4, "One\nTwo"]],
        footer=["A", "Footer\nBreak", 1, "Second\nCell\nBroken", 3],
    )
    expected = (
        "╔═══════════════════════════════════════════╗\n"
        "║ Multiline     G       Two      R       S  ║\n"
        "║  Header              Lines                ║\n"
        "║   Cell                                    ║\n"
        "╟───────────────────────────────────────────╢\n"
        "║     1       Alpha      3       4      One ║\n"
        "║              Beta                     Two ║\n"
        "║             Gamma                         ║\n"
        "╟───────────────────────────────────────────╢\n"
        "║     A       Footer     1     Second    3  ║\n"
        "║             Break             Cell        ║\n"
        "║                              Broken       ║\n"
        "╚═══════════════════════════════════════════╝"
    )
    assert text == expected


def test_east_asian_wide_characters_and_zero_width_wcwidth():
    # using wcwidth.wcswidth() to count the number of characters
    text = t2a(
        header=["#\u200b", "🦁", "🦡", "🦅", "🐍"],
        body=[["💻", "✅", "✅", "❌", "❌"]],
        footer=["🥞", "日", "月", "火", "水"],
        first_col_heading=True,
    )
    text2 = t2a(
        header=["#\u200b", "🦁", "🦡", "🦅", "🐍"],
        body=[["💻", "✅", "✅", "❌", "❌"]],
        footer=["🥞", "日", "月", "火", "水"],
        first_col_heading=True,
        use_wcwidth=True,
    )
    expected = (
        "╔════╦═══════════════════╗\n"
        "║ #​  ║ 🦁   🦡   🦅   🐍 ║\n"
        "╟────╫───────────────────╢\n"
        "║ 💻 ║ ✅   ✅   ❌   ❌ ║\n"
        "╟────╫───────────────────╢\n"
        "║ 🥞 ║ 日   月   火   水 ║\n"
        "╚════╩═══════════════════╝"
    )
    assert text == expected
    assert text2 == expected


def test_east_asian_wide_characters_and_zero_width_no_wcwidth():
    # using len() to count the number of characters
    text = t2a(
        header=["#\u200b", "🦁", "🦡", "🦅", "🐍"],
        body=[["💻", "✅", "✅", "❌", "❌"]],
        footer=["🥞", "日", "月", "火", "水"],
        first_col_heading=True,
        use_wcwidth=False,
    )
    expected = (
        "╔════╦═══════════════╗\n"
        "║ #​ ║ 🦁   🦡   🦅   🐍 ║\n"
        "╟────╫───────────────╢\n"
        "║ 💻  ║ ✅   ✅   ❌   ❌ ║\n"
        "╟────╫───────────────╢\n"
        "║ 🥞  ║ 日   月   火   水 ║\n"
        "╚════╩═══════════════╝"
    )
    assert text == expected


def test_multiline_cells_with_wrappable_lines():
    text = t2a(
        header=["Test"],
        body=[["Line One...\nSecond Line...\nLineNumThree\nLineFour\nFive FinalLine"]],
    )
    expected = (
        "╔════════════════╗\n"
        "║      Test      ║\n"
        "╟────────────────╢\n"
        "║  Line One...   ║\n"
        "║ Second Line... ║\n"
        "║  LineNumThree  ║\n"
        "║    LineFour    ║\n"
        "║ Five FinalLine ║\n"
        "╚════════════════╝"
    )
    assert text == expected
