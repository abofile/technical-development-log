total = 0
target = 0


def compound(initial_value: float, growth_rate: float, cycles: int, counter: str):
    global total
    total = initial_value
    rate = growth_rate / 100
    for i in range(cycles):
        if counter.strip().upper() == "Y":
            total += rate * total
            print(f"Year no.{i + 1}: {total}")
        else:
            total += rate * total
    return total


def compound_goal(initial_value, goal, time_frame):
    global target
    target = ((goal / initial_value) ** (1 / time_frame) - 1) * 100
    return target


starting_value = float(input("the initial value = "))

growth = float(input("the growth_rate = "))

time = int(input("cycles = "))

choise = input("do you want a yearly growth rate counter y/n ")

compound(starting_value, growth, time, choise)

if choise.strip().upper() != "Y":
    print(f"total growth: {total}")

needed_growth = compound_goal(8335, 18000, 10)

print(f"You need a growth rate of {target}% a year to reach your goal")
