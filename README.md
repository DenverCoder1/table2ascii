# table2ascii

[![build](https://img.shields.io/github/workflow/status/DenverCoder1/table2ascii/Python%20application/main)](https://github.com/DenverCoder1/table2ascii/actions/workflows/python-app.yml)
[![version](https://img.shields.io/pypi/v/table2ascii)](https://pypi.org/project/table2ascii/)
[![license](https://img.shields.io/pypi/l/table2ascii)](https://github.com/DenverCoder1/table2ascii/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/819650821314052106?color=7289DA&logo=discord&logoColor=white "Dev Pro Tips Discussion & Support Server")](https://discord.gg/fPrdqh3Zfu)

Module for converting 2D Python lists to a fancy ASCII/Unicode tables

- [table2ascii](#table2ascii)
  - [📥 Installation](#-installation)
  - [🧑‍💻 Usage](#-usage)
  - [⚙️ Options](#️-options)
  - [👨‍🎨 Use cases](#-use-cases)
  - [🧰 Development](#-development)


## 📥 Installation

``pip install table2ascii`` 


## 🧑‍💻 Usage

Convert Python lists to ASCII tables

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

## ⚙️ Options

Soon table2ascii will support more options for customization.

|       Option        |  Type  | Default |                           Description                            |
| :-----------------: | :----: | :-----: | :--------------------------------------------------------------: |
| `first_col_heading` | `bool` | `False` | Whether to add a heading column seperator after the first column |
| `last_col_heading`  | `bool` | `False` | Whether to add a heading column seperator before the last column |

## 👨‍🎨 Use cases

### Discord messages and embeds

* Display tables nicely inside markdown codeblocks on Discord
* Useful for making Discord bots with [Discord.py](https://github.com/Rapptz/discord.py)

![image](https://user-images.githubusercontent.com/20955511/116203248-2973c600-a744-11eb-97d8-4b75ed2845c9.png)

### Terminal outputs

* Tables display nicely whenever monospace fonts are fully supported
* Tables make terminal outputs look more professional

![image](https://user-images.githubusercontent.com/20955511/116204490-802dcf80-a745-11eb-9b4a-7cef49f23958.png)


## 🧰 Development

To run tests (pytest)

``python setup.py test``

To lint (flake8):

``python setup.py lint``
