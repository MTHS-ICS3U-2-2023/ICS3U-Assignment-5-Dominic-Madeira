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
        # check if both numbers are greater than 0
        if number1 > 0 and number2 > 0:
            # find the smallest number
            if number1 > number2:
                gcf_counter = number2
            else:
                gcf_counter = number1

            # find the GCF
            while gcf_counter > 0:
                if number1 % gcf_counter == 0 and number2 % gcf_counter == 0:
                    break
                gcf_counter -= 1

            # output
            print(f"\nThe greatest common factor is {gcf_counter}.")
        else:
            print(f"\nBoth numbers must be greater than 0")

    print("\nDone.")


if __name__ == "__main__":
    main()
