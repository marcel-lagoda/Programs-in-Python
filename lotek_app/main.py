import lotek_app.program as program


def main():
    # Load User numbers.
    user_numbers = program.get_user_numbers()

    # Generate lottery numbers.
    lottery_numbers = program.generate_lucky_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print(
        f"You matched {len(matched_numbers)} number{'s' if len(matched_numbers) != 1 else ''}."
        f"You won ${10 ** len(matched_numbers)}!"
    )


if __name__ == "__main__":
    main()
