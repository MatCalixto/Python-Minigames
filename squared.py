"""Import needed for random number generation."""
from random import randint

while True:

    ptype = randint(1, 2)
    number = randint(11, 30)

    print("Answer the math questions:\n")

    if ptype == 1:
        answer = int(input(str(number) + " squared equals: "))
        sol = number**2
    elif ptype == 2:
        answer = int(input("The square root of "
                           + str(number**2) + " equals: "))
        sol = number
    else:
        print("Error, Not a valid problem type.")

    if answer == sol:
        print("\nCongrats, your answer was correct")
    else:
        print("\nUnfortunately the answer was " + str(sol) + ", try again")

    playagain = int(input("\nType 1 if you want to play again: "))
    if playagain != 1:
        break

print("\nGame has ended")
