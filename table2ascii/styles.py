from .table_style import TableStyle

thin = TableStyle.from_string("┌─┬─┐││ ├─┼─┤├─┼─┤└┴─┘")
thin_rounded = TableStyle.from_string("╭─┬─╮││ ├─┼─┤├─┼─┤╰┴─╯")
thin_compact = TableStyle.from_string("┌─┬─┐││ ├─┼─┤     └┴─┘")
thin_compact_rounded = TableStyle.from_string("╭─┬─╮││ ├─┼─┤     ╰┴─╯")
thin_thick = TableStyle.from_string("┌─┬─┐││ ┝━┿━┥├─┼─┤└┴─┘")
thin_thick_rounded = TableStyle.from_string("╭─┬─╮││ ┝━┿━┥├─┼─┤╰┴─╯")
thin_double = TableStyle.from_string("┌─┬─┐││ ╞═╪═╡├─┼─┤└┴─┘")
thin_double_rounded = TableStyle.from_string("╭─┬─╮││ ╞═╪═╡├─┼─┤╰┴─╯")
thick_compact = TableStyle.from_string("┏━┳━┓┃┃ ┣━╋━┫     ┗┻━┛")
double = TableStyle.from_string("╔═╦═╗║║ ╠═╬═╣╠═╬═╣╚╩═╝")
double_compact = TableStyle.from_string("╔═╦═╗║║ ╠═╬═╣     ╚╩═╝")
double_thin = TableStyle.from_string("╔═╦═╗║║ ╟─╫─╢╠═╬═╣╚╩═╝")
minimalist = TableStyle.from_string(" ───     ━━━  ───  ── ")
ascii_compact = TableStyle.from_string("+-+-+|| +-+-+     ++-+")
ascii_double = TableStyle.from_string("+-+-+|| +=+=++-+-+++-+")
ascii_minimalist = TableStyle.from_string(" ---     ===  ---  -- ")
markdown = TableStyle.from_string("     ||||-|||         ")

# prints all themes with previews
if __name__ == "__main__":
    from .table_to_ascii import table2ascii

    styles = {
        "thin": thin,
        "thin_rounded": thin_rounded,
        "thin_compact": thin_compact,
        "thin_compact_rounded": thin_compact_rounded,
        "thin_thick": thin_thick,
        "thin_thick_rounded": thin_thick_rounded,
        "thin_double": thin_double,
        "thin_double_rounded": thin_double_rounded,
        "thick_compact": thick_compact,
        "double": double,
        "double_compact": double_compact,
        "double_thin": double_thin,
        "minimalist": minimalist,
        "ascii_compact": ascii_compact,
        "ascii_double": ascii_double,
        "ascii_minimalist": ascii_minimalist,
        "markdown": markdown,
    }
    for style in list(styles.keys()):
        full = table2ascii(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["SUM", "130", "140", "135", "130"],
            first_col_heading=True,
            last_col_heading=False,
            style=styles[style],
        )
        body_only = table2ascii(
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            first_col_heading=True,
            last_col_heading=False,
            style=styles[style],
        )
        print(f"### `{style}`\n\n```\n{full}\n{body_only}```\n")
