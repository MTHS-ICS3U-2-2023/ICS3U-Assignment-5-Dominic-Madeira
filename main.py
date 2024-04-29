#!/usr/bin/env python3
"""
Created by: Dominic M.
Created on: Apr 2024
This module calculates the GCF of two numbers
"""

def volume_cylinder(number1: int, numbmer2: int) -> int:
    """This function calculates the GCF of two numbers, returns GCF."""

    # process
    if number1 > number2:
        counter = number2
    else:
        counter = number1

    while counter > 0
        divider1 = number1 / counter
        divider2 = number2 / counter

    return gcf


def main() -> None:
    """The main() function gets input, calls other functions, shows output,
    returns None."""

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
        print(
            "The volume of a cylinder with radius" +
            f" {radius} cm and height {height} cm is {volume} cm³."
        )


    print("\n\nDone.")


if __name__ == "__main__":
    main()