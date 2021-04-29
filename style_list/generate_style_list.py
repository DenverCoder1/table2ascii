import os
from table2ascii import PresetStyle
from table2ascii.table_to_ascii import table2ascii

# generate README.md containing all themes with previews
if __name__ == "__main__":
    # get attributes in PresetStyle
    attribute_names = [attr for attr in dir(PresetStyle) if not attr.startswith("__")]
    attributes = [getattr(PresetStyle, attr) for attr in attribute_names]
    # make a dict mapping style names to TableStyles
    styles = dict(zip(attribute_names, attributes))
    # README output variables
    heading = "## Preset styles"
    table_of_contents = "- [Preset styles](#preset-styles)\n"
    style_list = ""
    # generate tables for each style
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
        table_of_contents += f"  - [`{style}`](#{style})\n"
        style_list += f"### `{style}`\n\n```\n{full}\n\n{body_only}\n```\n"
    # put it all together
    output = f"{heading}\n\n{table_of_contents}\n{style_list}"

    # overwrite `style_list/README.md` with the changes
    f = open(os.path.join("style_list", "README.md"), "w")
    f.write(output)
    f.close()
