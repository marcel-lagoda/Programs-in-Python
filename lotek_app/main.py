import lotek_app.program as programs


def main():
    # Load User numbers.
    user_numbers = program.get_user_numbers()

    # Generate lottery numbers.
    lottery_numbers = program.generate_lucky_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print(f"You matched {matched_numbers}. You won ${100 ** len(matched_numbers)}!")


if __name__ == "__main__":
    main()
