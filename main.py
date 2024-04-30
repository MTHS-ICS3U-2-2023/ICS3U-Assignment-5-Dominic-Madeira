#!/usr/bin/env python3
"""
Created by: Dominic M.
Created on: Apr 2024
This module calculates the GCF of two numbers
"""


def greatest_common_factor(number1: int, number2: int) -> int:
    """This function calculates the GCF of two numbers, returns GCF."""

    # process
    # find the smallest number
    if number1 > number2:
        counter = number2
    else:
        counter = number1

    # find the GCF
    while counter > 0:
        divider1 = number1 / counter
        divider2 = number2 / counter
        if divider1 % 1 == 0 and divider2 % 1 == 0:
            gcf = counter
            break
        else:
            counter -= 1

    return gcf


def main() -> None:
    """The main() function gets input, calls other functions, shows output,
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

        # call the function
        gcf = greatest_common_factor(number1, number2)

        # output
        print(f"The greatest common factor is {gcf}.")

    print("\nDone.")


if __name__ == "__main__":
    main()
