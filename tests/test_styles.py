import pytest

from table2ascii import PresetStyle, TableStyle, table2ascii as t2a
from table2ascii.exceptions import TableStyleTooLongError, TableStyleTooShortWarning


def _build_table_with_style(table_style: TableStyle) -> str:
    return t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["SUM", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=False,
        style=table_style,
    )


def test_table_style_from_string():
    table_style = TableStyle.from_string("╔═╦╤╗║║│╠═╬╪╣╟─╫┼╢╚╩╧╝┬┴╤╧╥╨╦╩")
    text = _build_table_with_style(table_style)
    expected = (
        "╔═════╦═════╤═════╤═════╤═════╗\n"
        "║  #  ║  G  │  H  │  R  │  S  ║\n"
        "╠═════╬═════╪═════╪═════╪═════╣\n"
        "║  1  ║ 30  │ 40  │ 35  │ 30  ║\n"
        "╟─────╫─────┼─────┼─────┼─────╢\n"
        "║  2  ║ 30  │ 40  │ 35  │ 30  ║\n"
        "╠═════╬═════╪═════╪═════╪═════╣\n"
        "║ SUM ║ 130 │ 140 │ 135 │ 130 ║\n"
        "╚═════╩═════╧═════╧═════╧═════╝"
    )
    assert text == expected


def test_table_style_from_string_too_long_error():
    with pytest.raises(TableStyleTooLongError):
        TableStyle.from_string("╔═╦╤╗║║│╠═╬╪╣╟─╫┼╢╚╩╧╝┬┴╤╧╥╨╦╩╦XXXX")


def test_table_style_from_string_too_short():
    with pytest.warns(TableStyleTooShortWarning):
        table_style = TableStyle.from_string("╔═╦╤╗║║│╠═╬╪╣╟─╫┼╢")
    text = _build_table_with_style(table_style)
    expected = (
        "╔═════╦═════╤═════╤═════╤═════╗\n"
        "║  #  ║  G  │  H  │  R  │  S  ║\n"
        "╠═════╬═════╪═════╪═════╪═════╣\n"
        "║  1  ║ 30  │ 40  │ 35  │ 30  ║\n"
        "╟─────╫─────┼─────┼─────┼─────╢\n"
        "║  2  ║ 30  │ 40  │ 35  │ 30  ║\n"
        "╠═════╬═════╪═════╪═════╪═════╣\n"
        "║ SUM ║ 130 │ 140 │ 135 │ 130 ║\n"
        " ═════ ═════ ═════ ═════ ═════ "
    )
    assert text == expected


def test_thin():
    text = _build_table_with_style(PresetStyle.thin)
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
    text = _build_table_with_style(PresetStyle.thin_box)
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


def test_thin_compact():
    text = text = _build_table_with_style(PresetStyle.thin_compact)
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


def test_plain():
    text = _build_table_with_style(PresetStyle.plain)
    expected = (
        "  #     G     H     R     S  \n"
        "  1    30    40    35    30  \n"
        "  2    30    40    35    30  \n"
        " SUM   130   140   135   130 "
    )
    assert text == expected
