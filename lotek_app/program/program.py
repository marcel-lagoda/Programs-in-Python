"""
This is the "program" module.

Program module supplies 2 functions, get_user_numbers(), generate_lucky_numbers().

>>> import random
>>> random.seed(1)
>>> generate_lucky_numbers()
{3, 5, 19, 25, 26, 28}
"""

import random


def get_user_numbers():
    """
    Get user input. Return it as a set.
    :return: user_numbers
    """
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            user_input = int(
                input("Enter your six lucky numbers one by one [between 1 and 29]: ")
            )
            if user_input in range(1, 29 + 1):
                user_numbers.add(user_input)
                print(f"Your all lucky numbers so far: {user_numbers}")
            else:
                continue
        except ValueError:
            print("Please try again: ")

    return user_numbers


def generate_lucky_numbers():
    """
    Generate random numbers.
    :return: numbers
    """
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 29))
    return numbers
