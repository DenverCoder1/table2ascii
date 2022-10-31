# table2ascii

[![build](https://img.shields.io/github/workflow/status/DenverCoder1/table2ascii/Python%20application/main)](https://github.com/DenverCoder1/table2ascii/actions/workflows/python-app.yml)
[![version](https://img.shields.io/pypi/v/table2ascii)](https://pypi.org/project/table2ascii/)
[![downloads](https://static.pepy.tech/personalized-badge/table2ascii?period=total&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/table2ascii)
[![license](https://img.shields.io/pypi/l/table2ascii)](https://github.com/DenverCoder1/table2ascii/blob/main/LICENSE)
[![discord](https://img.shields.io/discord/819650821314052106?color=5865F2&logo=discord&logoColor=white "Dev Pro Tips Discussion & Support Server")](https://discord.gg/fPrdqh3Zfu)

Library for converting 2D Python lists to fancy ASCII/Unicode tables

Documentation and examples are available at [table2ascii.rtfd.io](https://table2ascii.readthedocs.io/)

## 📥 Installation

`pip install -U table2ascii`

**Requirements:** `Python 3.7+`

## 🧑‍💻 Usage

### Convert lists to ASCII tables

```py
from table2ascii import table2ascii

output = table2ascii(
    header=["#", "G", "H", "R", "S"],
    body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
    footer=["SUM", "130", "140", "135", "130"],
)

print(output)

"""
╔═════════════════════════════╗
║  #     G     H     R     S  ║
╟─────────────────────────────╢
║  1    30    40    35    30  ║
║  2    30    40    35    30  ║
╟─────────────────────────────╢
║ SUM   130   140   135   130 ║
╚═════════════════════════════╝
"""
```

### Set first or last column headings

```py
from table2ascii import table2ascii

output = table2ascii(
    body=[["Assignment", "30", "40", "35", "30"], ["Bonus", "10", "20", "5", "10"]],
    first_col_heading=True,
)

print(output)

"""
╔════════════╦═══════════════════╗
║ Assignment ║ 30   40   35   30 ║
║    Bonus   ║ 10   20    5   10 ║
╚════════════╩═══════════════════╝
"""
```

### Set column widths and alignments

```py
from table2ascii import table2ascii, Alignment

output = table2ascii(
    header=["#", "G", "H", "R", "S"],
    body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
    first_col_heading=True,
    column_widths=[5] * 5,  # [5, 5, 5, 5, 5]
    alignments=[Alignment.LEFT] + [Alignment.RIGHT] * 4, # First is left, remaining 4 are right
)

print(output)

"""
╔═════╦═══════════════════════╗
║ #   ║   G     H     R     S ║
╟─────╫───────────────────────╢
║ 1   ║  30    40    35    30 ║
║ 2   ║  30    40    35    30 ║
╚═════╩═══════════════════════╝
"""
```

### Use a preset style

```py
from table2ascii import table2ascii, PresetStyle

output = table2ascii(
    header=["First", "Second", "Third", "Fourth"],
    body=[["10", "30", "40", "35"], ["20", "10", "20", "5"]],
    column_widths=[10] * 4,
    style=PresetStyle.ascii_box
)

print(output)

"""
+----------+----------+----------+----------+
|  First   |  Second  |  Third   |  Fourth  |
+----------+----------+----------+----------+
|    10    |    30    |    40    |    35    |
+----------+----------+----------+----------+
|    20    |    10    |    20    |    5     |
+----------+----------+----------+----------+
"""
```

### Define a custom style

Check [`TableStyle`](https://github.com/DenverCoder1/table2ascii/blob/main/table2ascii/table_style.py) for more info and [`PresetStyle`](https://github.com/DenverCoder1/table2ascii/blob/main/table2ascii/preset_style.py) for examples.

```py
from table2ascii import table2ascii, TableStyle

my_style = TableStyle.from_string("*-..*||:+-+:+     *''*")

output = table2ascii(
    header=["First", "Second", "Third"],
    body=[["10", "30", "40"], ["20", "10", "20"], ["30", "20", "30"]],
    style=my_style
)

print(output)

"""
*-------.--------.-------*
| First : Second : Third |
+-------:--------:-------+
|  10   :   30   :  40   |
|  20   :   10   :  20   |
|  30   :   20   :  30   |
*-------'--------'-------*
"""
```

## 🎨 Preset styles

See a list of all preset styles [here](https://table2ascii.readthedocs.io/en/latest/styles.html).

## ⚙️ Options

All parameters are optional.

|       Option        |         Type          |        Default        |                                    Description                                    |
| :-----------------: | :-------------------: | :-------------------: | :-------------------------------------------------------------------------------: |
|      `header`       |      `List[Any]`      |        `None`         | First table row seperated by header row seperator. Values should support `str()`. |
|       `body`        |   `List[List[Any]]`   |        `None`         |  List of rows for the main section of the table. Values should support `str()`.   |
|      `footer`       |      `List[Any]`      |        `None`         | Last table row seperated by header row seperator. Values should support `str()`.  |
|   `column_widths`   | `List[Optional[int]]` |  `None` (automatic)   |                List of column widths in characters for each column                |
|    `alignments`     |   `List[Alignment]`   | `None` (all centered) | Column alignments<br/>(ex. `[Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]`) |
|       `style`       |     `TableStyle`      | `double_thin_compact` |                         Table style to use for the table                          |
| `first_col_heading` |        `bool`         |        `False`        |         Whether to add a heading column seperator after the first column          |
| `last_col_heading`  |        `bool`         |        `False`        |         Whether to add a heading column seperator before the last column          |

See the [API Reference](https://table2ascii.readthedocs.io/en/latest/api.html) for more info.

## 👨‍🎨 Use cases

### Discord messages and embeds

-   Display tables nicely inside markdown code blocks on Discord
-   Useful for making Discord bots with [Discord.py](https://github.com/Rapptz/discord.py)

![image](https://user-images.githubusercontent.com/20955511/116203248-2973c600-a744-11eb-97d8-4b75ed2845c9.png)

### Terminal outputs

-   Tables display nicely whenever monospace fonts are fully supported
-   Tables make terminal outputs look more professional

![image](https://user-images.githubusercontent.com/20955511/116204490-802dcf80-a745-11eb-9b4a-7cef49f23958.png)

## 🤗 Contributing

Contributions are welcome!

See [CONTRIBUTING.md](https://github.com/DenverCoder1/table2ascii/blob/main/CONTRIBUTING.md) for more details on how to get involved.
