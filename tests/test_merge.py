from table2ascii import Alignment, Merge, PresetStyle, table2ascii as t2a


def test_merge_all_edges():
    text = t2a(
        header=["Header", Merge.LEFT, "A", "B"],
        body=[
            ["A", "B", "C", Merge.LEFT],
            ["D", Merge.LEFT, "E", Merge.LEFT],
            ["F", "G", "H", "I"],
            ["J", "K", "L", Merge.LEFT],
        ],
        column_widths=[4, 4, None, None],
        footer=["Footer", Merge.LEFT, "A", "B"],
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════════╤═══╤═══╗\n"
        "║ Header  │ A │ B ║\n"
        "╠════╤════╪═══╧═══╣\n"
        "║ A  │ B  │   C   ║\n"
        "╟────┴────┼───────╢\n"
        "║    D    │   E   ║\n"
        "╟────┬────┼───┬───╢\n"
        "║ F  │ G  │ H │ I ║\n"
        "╟────┼────┼───┴───╢\n"
        "║ J  │ K  │   L   ║\n"
        "╠════╧════╪═══╤═══╣\n"
        "║ Footer  │ A │ B ║\n"
        "╚═════════╧═══╧═══╝"
    )
    assert text == expected


def test_merge_no_header_column():
    text = t2a(
        header=["#", "G", "Merge", Merge.LEFT, "S"],
        body=[
            [1, 5, 6, 200, Merge.LEFT],
            [2, "E", "Long cell", Merge.LEFT, Merge.LEFT],
            ["Bonus", Merge.LEFT, Merge.LEFT, "F", "G"],
        ],
        footer=["SUM", "100", "200", Merge.LEFT, "300"],
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════╤═════╤═══════╤═════╗\n"
        "║  #  │  G  │ Merge │  S  ║\n"
        "╠═════╪═════╪═══╤═══╧═════╣\n"
        "║  1  │  5  │ 6 │   200   ║\n"
        "╟─────┼─────┼───┴─────────╢\n"
        "║  2  │  E  │  Long cell  ║\n"
        "╟─────┴─────┴───┬───┬─────╢\n"
        "║     Bonus     │ F │  G  ║\n"
        "╠═════╤═════╤═══╧═══╪═════╣\n"
        "║ SUM │ 100 │  200  │ 300 ║\n"
        "╚═════╧═════╧═══════╧═════╝"
    )
    assert text == expected


def test_merge_header_column():
    text = t2a(
        header=["#", "G", "Merge", Merge.LEFT, "S"],
        body=[
            [1, 5, 6, 200, Merge.LEFT],
            [2, "E", "Long cell", Merge.LEFT, Merge.LEFT],
            ["Bonus", Merge.LEFT, Merge.LEFT, "F", "G"],
        ],
        footer=["SUM", "100", "200", Merge.LEFT, "300"],
        style=PresetStyle.double_thin_box,
        first_col_heading=True,
    )
    expected = (
        "╔═════╦═════╤═══════╤═════╗\n"
        "║  #  ║  G  │ Merge │  S  ║\n"
        "╠═════╬═════╪═══╤═══╧═════╣\n"
        "║  1  ║  5  │ 6 │   200   ║\n"
        "╟─────╫─────┼───┴─────────╢\n"
        "║  2  ║  E  │  Long cell  ║\n"
        "╟─────╨─────┴───┬───┬─────╢\n"
        "║     Bonus     │ F │  G  ║\n"
        "╠═════╦═════╤═══╧═══╪═════╣\n"
        "║ SUM ║ 100 │  200  │ 300 ║\n"
        "╚═════╩═════╧═══════╧═════╝"
    )
    assert text == expected


def test_merge_line_wrap():
    text = t2a(
        header=["Name", "Price", "Category", "Stock", "Sku"],
        body=[
            ["test", 443, "test", 67, "test"],
        ],
        footer=[
            "Description",
            "Long cell value that is merged and wraps to multiple lines",
            Merge.LEFT,
            Merge.LEFT,
            Merge.LEFT,
        ],
        alignments=[Alignment.LEFT] * 5,
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════════════╤═══════╤══════════╤═══════╤══════╗\n"
        "║ Name        │ Price │ Category │ Stock │ Sku  ║\n"
        "╠═════════════╪═══════╪══════════╪═══════╪══════╣\n"
        "║ test        │ 443   │ test     │ 67    │ test ║\n"
        "╠═════════════╪═══════╧══════════╧═══════╧══════╣\n"
        "║ Description │ Long cell value that is merged  ║\n"
        "║             │ and wraps to multiple lines     ║\n"
        "╚═════════════╧═════════════════════════════════╝"
    )
    assert text == expected


def test_merge_compact():
    text = t2a(
        header=["Header", Merge.LEFT, "A", "B"],
        body=[
            ["A", "B", "C", Merge.LEFT],
            ["D", Merge.LEFT, "E", Merge.LEFT],
            ["F", "G", "H", "I"],
            ["J", "K", "L", Merge.LEFT],
        ],
        footer=["Footer", Merge.LEFT, "A", "B"],
        column_widths=[4, 4, None, None],
        style=PresetStyle.double_thin_compact,
        first_col_heading=True,
    )
    expected = (
        "╔═════════════════╗\n"
        "║ Header    A   B ║\n"
        "╟────╥────────────╢\n"
        "║ A  ║ B      C   ║\n"
        "║    D        E   ║\n"
        "║ F  ║ G    H   I ║\n"
        "║ J  ║ K      L   ║\n"
        "╟────╨────────────╢\n"
        "║ Footer    A   B ║\n"
        "╚═════════════════╝"
    )
    assert text == expected


def test_row_beginning_with_merge():
    text = t2a(
        header=[Merge.LEFT, "A", "B", Merge.LEFT],
        body=[
            [Merge.LEFT, "A", "B", "C"],
            [Merge.LEFT, Merge.LEFT, Merge.LEFT, Merge.LEFT],
            ["F", "G", "H", "I"],
            ["J", "K", "L", Merge.LEFT],
        ],
        footer=[Merge.LEFT, Merge.LEFT, "A", "B"],
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═══╤═══╤═══════╗\n"
        "║   │ A │   B   ║\n"
        "╠═══╪═══╪═══╤═══╣\n"
        "║   │ A │ B │ C ║\n"
        "╟───┴───┴───┴───╢\n"
        "║               ║\n"
        "╟───┬───┬───┬───╢\n"
        "║ F │ G │ H │ I ║\n"
        "╟───┼───┼───┴───╢\n"
        "║ J │ K │   L   ║\n"
        "╠═══╧═══╪═══╤═══╣\n"
        "║       │ A │ B ║\n"
        "╚═══════╧═══╧═══╝"
    )
    assert text == expected


def test_merge_up():
    text = t2a(
        header=["0", "1", "A", "B", "C", "D"],
        body=[
            ["A", Merge.UP, "C", Merge.UP, Merge.UP, Merge.UP],
            ["D", Merge.LEFT, "E", Merge.LEFT, "F", "G"],
            ["F", "G", "H", "I", "J", "K"],
            ["J", Merge.UP, "L", "M", Merge.UP, Merge.UP],
        ],
        column_widths=[5] * 6,
        footer=["Footer", Merge.LEFT, Merge.UP, "N", "O", Merge.UP],
        first_col_heading=True,
        last_col_heading=True,
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════╦═════╤═════╤═════╤═════╦═════╗\n"
        "║  0  ║  1  │  A  │  B  │  C  ║  D  ║\n"
        "╠═════╣     ╞═════╡     │     ║     ║\n"
        "║  A  ║     │  C  │     │     ║     ║\n"
        "╟─────╨─────┼─────┴─────┼─────╫─────╢\n"
        "║     D     │     E     │  F  ║  G  ║\n"
        "╟─────╥─────┼─────┬─────┼─────╫─────╢\n"
        "║  F  ║  G  │  H  │  I  │  J  ║  K  ║\n"
        "╟─────╢     ├─────┼─────┤     ║     ║\n"
        "║  J  ║     │  L  │  M  │     ║     ║\n"
        "╠═════╩═════╡     ╞═════╪═════╣     ║\n"
        "║  Footer   │     │  N  │  O  ║     ║\n"
        "╚═══════════╧═════╧═════╧═════╩═════╝"
    )
    assert text == expected


def test_merge_left_and_up_square():
    text = t2a(
        header=["0", "1", "A", "B", "C", "D"],
        body=[
            ["A", Merge.UP, "C", Merge.UP, Merge.UP, Merge.UP],
            ["D", Merge.LEFT, "E", Merge.LEFT, "F", "G"],
            ["F", "G", Merge.UP, Merge.UP, "J", "K"],
            ["J", Merge.UP, "L", "M", Merge.UP, Merge.UP],
        ],
        column_widths=[5] * 6,
        footer=["Footer", Merge.LEFT, Merge.UP, "N", "O", Merge.UP],
        first_col_heading=True,
        last_col_heading=True,
        style=PresetStyle.double_thin_box,
    )
    expected = (
        "╔═════╦═════╤═════╤═════╤═════╦═════╗\n"
        "║  0  ║  1  │  A  │  B  │  C  ║  D  ║\n"
        "╠═════╣     ╞═════╡     │     ║     ║\n"
        "║  A  ║     │  C  │     │     ║     ║\n"
        "╟─────╨─────┼─────┴─────┼─────╫─────╢\n"
        "║     D     │     E     │  F  ║  G  ║\n"
        "╟─────╥─────┤           ├─────╫─────╢\n"
        "║  F  ║  G  │           │  J  ║  K  ║\n"
        "╟─────╢     ├─────┬─────┤     ║     ║\n"
        "║  J  ║     │  L  │  M  │     ║     ║\n"
        "╠═════╩═════╡     ╞═════╪═════╣     ║\n"
        "║  Footer   │     │  N  │  O  ║     ║\n"
        "╚═══════════╧═════╧═════╧═════╩═════╝"
    )
    assert text == expected
