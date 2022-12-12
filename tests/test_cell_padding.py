import pytest

from table2ascii import Alignment, table2ascii as t2a
from table2ascii.exceptions import InvalidCellPaddingError


def test_without_cell_padding():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[[1, 2, 3, 4, 5]],
        footer=["A", "B", 1, 2, 3],
        first_col_heading=True,
        cell_padding=0,
    )
    expected = (
        "╔═╦═══════╗\n"
        "║#║G H R S║\n"
        "╟─╫───────╢\n"
        "║1║2 3 4 5║\n"
        "╟─╫───────╢\n"
        "║A║B 1 2 3║\n"
        "╚═╩═══════╝"
    )
    assert text == expected


def test_column_width_and_alignment_without_cell_padding():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[[1, 2, 3, 4, 5]],
        footer=["A", "B", 1, 2, 3],
        column_widths=[4, 8, 5, 4, 5],
        alignments=[
            Alignment.LEFT,
            Alignment.CENTER,
            Alignment.RIGHT,
            Alignment.LEFT,
            Alignment.RIGHT,
        ],
        first_col_heading=True,
        cell_padding=0,
    )
    expected = (
        "╔════╦═════════════════════════╗\n"
        "║#   ║   G         H R        S║\n"
        "╟────╫─────────────────────────╢\n"
        "║1   ║   2         3 4        5║\n"
        "╟────╫─────────────────────────╢\n"
        "║A   ║   B         1 2        3║\n"
        "╚════╩═════════════════════════╝"
    )
    assert text == expected


def test_cell_padding_more_than_one():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[[1, 2, 3, 4, 5]],
        footer=["A", "B", 1, 2, 3],
        first_col_heading=True,
        cell_padding=2,
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║  1  ║  2     3     4     5  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║  A  ║  B     1     2     3  ║\n"
        "╚═════╩═══════════════════════╝"
    )
    assert text == expected


def test_negative_cell_padding():
    with pytest.raises(InvalidCellPaddingError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[[1, 2, 3, 4, 5]],
            footer=["A", "B", 1, 2, 3],
            first_col_heading=True,
            cell_padding=-1,
        )
