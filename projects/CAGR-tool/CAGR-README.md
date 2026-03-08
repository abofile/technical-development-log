# CAGR Calculator

A Python CLI tool for compound growth calculations. Built to replace manually using online calculators — inputs your own values and optionally tracks growth year by year.

## Features

- **Compound growth calculator** — calculates total value after N cycles at a given growth rate
- **Yearly counter** — optionally prints the value at the end of each year
- **Goal-based reverse calculator** — given a starting value, target, and time frame, calculates the required annual growth rate

## Usage

Run from the terminal:

```bash
python CAGR.py
```

The script runs interactively and prompts for input at each step.

**Example — Compound Growth:**
```
CAGR calculator y/n: y
the initial value = 10000
the growth_rate = 8
cycles = 5
do you want a yearly growth rate counter y/n: y

Year no.1: 10800.0
Year no.2: 11664.0
Year no.3: 12597.12
Year no.4: 13604.89
Year no.5: 14693.28
```

**Example — Goal Calculator:**
```
Target goal calculator y/n: y
the current value = 10000
the goal target = 20000
what is your time frame: 5

You need a growth rate of 14.87% a year to reach your goal
```

## Requirements

- Python 3.x
- No external libraries

## Notes

- Growth rate is entered as a percentage (e.g. `8` for 8%)
- Both calculators are optional and run independently in the same session
- Inputs use `.strip().upper()` for clean y/n handling
