# table2ascii

Module for converting 2D Python lists to a fancy ASCII/Unicode tables

- [table2ascii](#table2ascii)
  - [🧑‍💻 Usage](#-usage)
  - [⚙️ Options](#️-options)
  - [🧰 Development](#-development)

<!-- 
## 📥 Installation

``pip install table2ascii`` 
-->

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
╔═════╦═══════════════════════╗
║  #  ║  G     H     R     S  ║
╟─────╫───────────────────────╢
║  1  ║  30    40    35    30 ║
║  2  ║  30    40    35    30 ║
╟─────╫───────────────────────╢
║ SUM ║ 130   140   135   130 ║
╚═════╩═══════════════════════╝
"""
```

```py
from table2ascii import table2ascii

output = table2ascii(
    body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]]
)

print(output)

"""
╔═════╦═══════════════════════╗
║  1  ║  30    40    35    30 ║
║  2  ║  30    40    35    30 ║
╚═════╩═══════════════════════╝
"""
```

## ⚙️ Options

Soon table2ascii will support more options for customization.


## 🧰 Development

To run tests (pytest)

``python setup.py test``

To lint (flake8):

``python setup.py lint``