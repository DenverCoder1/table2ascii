import os

__import__("sys").path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from table2ascii import PresetStyle, table2ascii


def indent_all_lines(text, number_of_spaces=3):
    """Indent all lines in a string by a certain number of spaces"""
    return "\n".join(number_of_spaces * " " + line for line in text.split("\n"))


def generate_style_list():
    """Generate README.rst the style list"""
    # get attributes in PresetStyle
    attribute_names = [attr for attr in dir(PresetStyle) if not attr.startswith("__")]
    attributes = [getattr(PresetStyle, attr) for attr in attribute_names]
    # make a dict mapping style names to TableStyles
    styles = dict(zip(attribute_names, attributes))
    # README output variables
    heading = ".. _styles:\n\nPreset styles\n-------------"
    table_of_contents = ".. contents::\n"
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
        style_heading = f"`{style}`\n" + "~" * len(f"`{style}`")
        output_example = indent_all_lines(full + "\n\n" + body_only)
        style_list += f"{style_heading}\n\n.. code-block:: none\n\n{output_example}\n\n"
    # put it all together
    return f"{heading}\n\n{table_of_contents}\n{style_list}"


def write_to_file(filename, content):
    """Write content to filename"""
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    content = generate_style_list()
    write_to_file(os.path.join(os.path.dirname(__file__), "styles.rst"), content)
    print("Successfully generated styles.rst")
