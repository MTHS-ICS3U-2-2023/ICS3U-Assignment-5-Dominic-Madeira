#!/usr/bin/env python3
"""
Created by: Dominic M.
Created on: Apr 2024
This module calculates the GCF of two numbers
"""


def main() -> None:
    """The main() function calculates the GCF of two numbers from user input,
    returns None."""

    # input
    number1 = input("Enter an integer: ")
    number2 = input("Enter another integer: ")

    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("\nYou did not enter a valid number.")
    else:

        # process
        # find the smallest number
        if number1 > number2:
            counter = number2
        else:
            counter = number1

        # find the GCF
        while counter > 0:
            if number1 % counter == 0 and number2 % counter == 0:
                gcf = counter
                break
            counter -= 1

        # output
        print(f"\nThe greatest common factor is {gcf}.")

    print("\nDone.")


if __name__ == "__main__":
    main()
