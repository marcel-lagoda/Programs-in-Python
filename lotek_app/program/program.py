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
