import os
from table2ascii import Styles
from table2ascii.table_to_ascii import table2ascii

# generate README.md containing all themes with previews
if __name__ == "__main__":
    styles = {
        "thin": Styles.thin,
        "thin_box": Styles.thin_box,
        "thin_rounded": Styles.thin_rounded,
        "thin_compact": Styles.thin_compact,
        "thin_compact_rounded": Styles.thin_compact_rounded,
        "thin_thick": Styles.thin_thick,
        "thin_thick_rounded": Styles.thin_thick_rounded,
        "thin_double": Styles.thin_double,
        "thin_double_rounded": Styles.thin_double_rounded,
        "thick": Styles.thick,
        "thick_box": Styles.thick_box,
        "thick_compact": Styles.thick_compact,
        "double": Styles.double,
        "double_box": Styles.double_box,
        "double_compact": Styles.double_compact,
        "double_thin_compact": Styles.double_thin_compact,
        "minimalist": Styles.minimalist,
        "borderless": Styles.borderless,
        "simple": Styles.simple,
        "ascii": Styles.ascii,
        "ascii_box": Styles.ascii_box,
        "ascii_compact": Styles.ascii_compact,
        "ascii_double": Styles.ascii_double,
        "ascii_minimalist": Styles.ascii_minimalist,
        "ascii_borderless": Styles.ascii_borderless,
        "ascii_simple": Styles.ascii_simple,
        "markdown": Styles.markdown,
    }
    output = "## Preset styles\n\n"
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
        output += f"### `{style}`\n\n```\n{full}\n\n{body_only}\n```\n"

    f = open(os.path.join("style_list", "README.md"), "w")
    f.write(output)
    f.close()
