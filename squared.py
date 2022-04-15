import random
playagain = 1
while playagain == 1:
    ptype = random.randint(1,2)
    number = random.randint(11,30)
    sol = 0
    print("Answer the math questions:")
    print("")
    if ptype == 1:
        answer = int(input(str(number) + " squared equals: "))
        sol = number**2
    else:
        answer = int(input("The square root of " + str(number**2) + " equals: "))
        sol = number
    print("")
    if answer == sol:
        print("Congrats, your answer was correct")
    else:
        print("Unfortunately the answer was " + str(sol) + ", try again")
    print("")
    playagain = 0
    playagain = int(input("Type 1 if you want to play again: "))
    print("")
print("Game has ended")
