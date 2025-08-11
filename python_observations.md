# Python Behavior Notes

## Loop Variable Retention

In Python, a variable used in a `for` loop remains accessible after the loop ends, holding the last value from the iteration.

```python
for i in range(3):
    print(i)
print("After loop:", i)  # i is still 2
```
