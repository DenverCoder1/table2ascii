import os
from table2ascii import styles
from table2ascii.table_to_ascii import table2ascii

# generate README.md containing all themes with previews
if __name__ == "__main__":
    styles = {
        "thin": styles.thin,
        "thin_box": styles.thin_box,
        "thin_rounded": styles.thin_rounded,
        "thin_compact": styles.thin_compact,
        "thin_compact_rounded": styles.thin_compact_rounded,
        "thin_thick": styles.thin_thick,
        "thin_thick_rounded": styles.thin_thick_rounded,
        "thin_double": styles.thin_double,
        "thin_double_rounded": styles.thin_double_rounded,
        "thick": styles.thick,
        "thick_box": styles.thick_box,
        "thick_compact": styles.thick_compact,
        "double": styles.double,
        "double_box": styles.double_box,
        "double_compact": styles.double_compact,
        "double_thin_compact": styles.double_thin_compact,
        "minimalist": styles.minimalist,
        "borderless": styles.borderless,
        "simple": styles.simple,
        "ascii": styles.ascii,
        "ascii_box": styles.ascii_box,
        "ascii_compact": styles.ascii_compact,
        "ascii_double": styles.ascii_double,
        "ascii_minimalist": styles.ascii_minimalist,
        "ascii_borderless": styles.ascii_borderless,
        "ascii_simple": styles.ascii_simple,
        "markdown": styles.markdown,
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
