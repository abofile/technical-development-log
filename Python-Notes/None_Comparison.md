## Python None Comparison Issue

**Problem:** Cannot use comparison operators (`<=`, `>=`, `<`, `>`) with `None`
```python
if HEAT_INDEX <= 25:  # CRASHES if HEAT_INDEX is None
```

**Why:** `None` is not a number. Python can't evaluate "is None less than 25?" - it raises TypeError.

**Solution:** Check for `None` using `is` operator BEFORE numeric comparisons
```python
if HEAT_INDEX is None:  # Safe - uses identity check
    # handle None case
elif HEAT_INDEX <= 25:  # Safe - only runs if HEAT_INDEX is a number
    # handle numeric case
```

**In Heat Index project:** 
- Table returns `None` for off-chart temp/humidity combinations (the `**` values)
- Must check `None` first, otherwise numeric comparisons crash
- Order matters: identity checks before value comparisons

**Key takeaway:** Always handle `None` before attempting mathematical operations or comparisons
