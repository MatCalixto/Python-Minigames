"""Import needed for random number generation."""
from random import randint

while True:

    ptype = randint(1, 2)
    number = randint(11, 30)

    print("Answer the math questions:\n")

    sol = number ** (2 / ptype)

    if ptype == 1:
        answer = int(input(f"{number**ptype} squared equals: "))
    elif ptype == 2:
        answer = int(input(f"The square root of {number**ptype} equals: "))
    else:
        raise ValueError("Invalid problem type.")

    if answer == sol:
        print("\nCongrats, your answer was correct")
    else:
        print(f"\nUnfortunately the answer was {sol}, try again")

    playagain = int(input("\nType 1 if you want to play again: "))
    if playagain != 1:
        break

print("\nGame has ended")
