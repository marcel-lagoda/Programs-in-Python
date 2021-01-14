import lotek_app.programs as programs


def main():
    """

    :return:
    """
    # Load User numbers.
    user_numbers = programs.get_user_numbers()

    # Generate lottery numbers.
    lottery_numbers = programs.generate_lucky_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print(f"You matched {matched_numbers}. You won ${100 ** len(matched_numbers)}!")


if __name__ == '__main__':
    main()
