import random


def get_user_numbers():
    """
    Get user input. Return it as a set.
    :return: user_numbers
    """
    user_numbers = set()
    counter = 0
    while counter <= 5:
        try:
            user_input = int(input("Enter your six lucky numbers [between 1 and 29]: "))
            user_numbers.add(user_input)
            print(f"Your all lucky numbers so far : {user_numbers}")
            counter += 1
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
