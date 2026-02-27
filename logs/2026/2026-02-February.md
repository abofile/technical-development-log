# February 2026
**Period:** 2026-02-01 — 2026-02-28
**Mode:** Monthly
**Primary Focus:** GUI Development (Tkinter & Pygame), OOP, Projects

---

## Learning Progress

- Object-Oriented Programming — built a `Product` class with instance methods, class attributes, and applied logic (discounts, tax, currency conversion, threshold checks)
- Functions with applied logic — even number checker, list filter, value extractor
- Tkinter GUI basics — window setup, Label and Button widgets, image loading with Pillow, event handling, layout
- Pygame basics — display loop, frame rate control, surface rendering, image loading, basic sprite animation
- `None` handling — documented the identity check pattern before numeric comparisons to avoid `TypeError`
- Loop variable scope — documented global vs local behavior and how to avoid leftover variables

---

## Code & Projects

**Heat Index Alert System** (`projects/Heat-index-alert/`)
- Runs on Raspberry Pi Pico 2W with DHT22 sensor and 16x2 I2C LCD
- Reads live temp and humidity, looks up heat index from a reference table, displays alert level on LCD
- Handles out-of-range sensor values with rounding logic
- Fixed and documented a `None` comparison bug
- Set up SSH for headless remote access

**CAGR Calculator** (`projects/CAGR.py`)
- CLI tool for compound growth and target goal calculations
- Derived the CAGR formula independently and implemented it correctly
- Optional year-by-year counter, modular functions

**Tkinter** (`code/Tkinter/`)
- Window setup, geometry, icon loading
- Label and Button widgets with styling, image compound, event handling

**Pygame** (`code/Pygame/`)
- Window loop with proper quit handling
- Image and font rendering with `.blit()`
- Moving sprite animation with position reset

**OOP Practice** (`code/Python notebooks/classes_practice.py`)
- `Product` class with 8 methods covering display, calculation, and business logic

---

## Struggles & Notes

- `None` comparisons crashed the Heat Index project before the fix — pattern now documented
- Tkinter required Pillow workaround for JPEG support
- Loop variable scope behavior noted as a subtle Python quirk worth remembering