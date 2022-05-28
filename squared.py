"""Import needed for random number generation."""
from random import randint

while True:

    ptype = randint(1, 2)
    number = randint(11, 30)

    print("Answer the math questions:\n")

    sol = number ** (2 / ptype)
    challenge_number = number ** ptype

    if ptype == 1:
        print(f"{challenge_number} squared equals: ")
    elif ptype == 2:
        print(input(f"The square root of {challenge_number} equals: "))
    else:
        raise ValueError("Invalid problem type.")

    answer = int(input())

    if answer == sol:
        print("\nCongrats, your answer was correct")
    else:
        print(f"\nUnfortunately the answer was {sol}, try again")

    playagain = int(input("\nType 1 if you want to play again: "))
    if playagain != 1:
        break

print("\nGame has ended")
