"""Import needed for random number generation."""
from random import randint


def check_solution(guess: int, solution: int) -> None:
    """Method to Check if the answer is correct."""
    if guess == solution:
        print("\nCongrats, your answer was correct")
    else:
        print(f"\nUnfortunately the answer was {solution}, try again")


def check_problem_type(problem_type: int) -> None:
    """Method to check if the problem type is correct."""
    if problem_type == 1:
        print(f"{challenge_number} squared equals: ")
    elif problem_type == 2:
        print((f"The square root of {challenge_number} equals: "))
    else:
        raise ValueError("Invalid problem type.")


while True:

    actual_problem_type = randint(1, 2)
    number = randint(11, 30)

    print("Answer the math questions:\n")

    problem_solution = number ** (2 / actual_problem_type)
    challenge_number = number ** actual_problem_type

    check_problem_type(actual_problem_type)

    problem_guess = int(input())
    check_solution(problem_guess, problem_solution)

    print("\nType 1 if you want to play again: ")
    print("************************************************")
    if int(input()) != 1:
        break

print("\nGame has ended")
