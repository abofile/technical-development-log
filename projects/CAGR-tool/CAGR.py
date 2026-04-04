import time


def compound(initial_value: float, growth_rate: float, cycles: int, counter: str):
    total = initial_value
    rate = growth_rate / 100
    with open("cagr.txt", "a") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        f.write(f"Initial value: {initial_value}\n")
    for i in range(cycles):
        total += rate * total
        if counter.strip().upper() == "Y":
            print(f"Year no.{i + 1}: {round(total, 3)}")
            with open("cagr.txt", "a") as f:
                f.write(f"Year no.{i + 1}: {round(total, 3)}\n")

    if counter.strip().upper() != "Y":
        print(f"Total growth: {round(total, 3)}")

        with open("cagr.txt", "a") as f:
            f.write(f"The initial value will be {round(total, 2)} in {cycles} years\n")
    with open("cagr.txt", "a") as f:
        f.write("########################################################\n")


def compound_goal(initial_value, goal, time_frame):

    target = ((goal / initial_value) ** (1 / time_frame) - 1) * 100
    return target


CAGR_calculator = input("CAGR calculator y/n")

if CAGR_calculator.strip().upper() == "Y":
    try:
        starting_value = float(input("the initial value = "))
        growth = float(input("the growth_rate = "))
        cycles = int(input("cycles = "))
        choise = input("do you want a yearly growth rate counter y/n ")
        compound(starting_value, growth, cycles, choise)
    except (TypeError, ValueError) as e:
        print("Wrong data type use numbers only", e)
    except ZeroDivisionError as e:
        print("You can't dived zero", e)

goal_request = input("Target goal calculator y/n")

if goal_request.strip().upper() == "Y":
    try:
        A = float(input("the current value = "))
        B = float(input("the goal target = "))
        C = int(input("what is your time frame: "))
        target_goal = compound_goal(A, B, C)
        print(
            f"You need a growth rate of {round(target_goal, 3)}% a year to reach your goal"
        )
    except (TypeError, ValueError) as e:
        print("Wrong data type use numbers only", e)
    except ZeroDivisionError as e:
        print("You can't dived zero", e)
