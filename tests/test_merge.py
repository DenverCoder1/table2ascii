import pytest

from table2ascii import Alignment, Merge, PresetStyle, table2ascii as t2a


def test_merge():
    text = t2a(
        header=["#", "G", "H", "Other", Merge.LEFT],
        body=[["1", "60", "40", "45", "80"], ["2", "30", "20", "90", "50"]],
        footer=["SUM", "Merged", Merge.LEFT, "135", "130"],
        first_col_heading=True,
    )
    expected = (
        "╔═════╦═════════════════════╗\n"
        "║  #  ║ G    H      Other   ║\n"
        "╟─────╫─────────────────────╢\n"
        "║  1  ║ 60   40   45    80  ║\n"
        "║  2  ║ 30   20   90    50  ║\n"
        "╟─────╫─────────────────────╢\n"
        "║ SUM ║ Merged    135   130 ║\n"
        "╚═════╩═════════════════════╝"
    )
    assert text == expected
