total = 0
target = 0


def compound(initial_value: float, growth_rate: float, cycles: int, counter: str):
    global total
    total = initial_value
    rate = growth_rate / 100
    for i in range(cycles):
        total += rate * total

        if counter.strip().upper() == "Y":
            print(f"Year no.{i + 1}: {round(total, 3)}")

    return total


def compound_goal(initial_value, goal, time_frame):
    global target
    target = ((goal / initial_value) ** (1 / time_frame) - 1) * 100
    return target


CAGR_calculator = input("CAGR calculator y/n")

if CAGR_calculator.strip().upper() == "Y":
    starting_value = float(input("the initial value = "))

    growth = float(input("the growth_rate = "))

    time = int(input("cycles = "))

    choise = input("do you want a yearly growth rate counter y/n ")

    compound(starting_value, growth, time, choise)

    if choise.strip().upper() != "Y":
        print(f"total growth: {round(total, 3)}")

goal_request = input("Target goal calculator y/n")

if goal_request.strip().upper() == "Y":
    A = float(input("the current value = "))
    B = float(input("the goal target = "))
    C = int(input("what is your time frame: "))

    compound_goal(A, B, C)

    print(f"You need a growth rate of {round(target, 3)}% a year to reach your goal")
