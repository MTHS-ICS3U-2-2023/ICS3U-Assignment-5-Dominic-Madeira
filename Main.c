// Copyright (c) 2024 Dominic M. All rights reserved
//
// Created by: Dominic M.
// Created on: Apr 2024
// This program calculates the GCF of two numbers

#include <stdio.h>
#include <cs50.h>


int main() {
    // this function calculates the GCF of two numbers
    int number1;
    int number2;
    int gfcCounter;

    // input
    number1 = get_int("Enter an integer ");
    number2 = get_int("Enter another integer ");

    // process
    // check if both numbers are greater than 0
    if (number1 > 0 && number2 > 0) {
        // find the smallest number
        if (number1 > number2) {
            gfcCounter = number2;
        } else {
            gfcCounter = number1;
        }

        // find the GCF
        while (gfcCounter > 0) {
            if (number1 % gfcCounter == 0 && number2 % gfcCounter == 0) {
                break;
            }
            gfcCounter--;
        }

        printf("\n\nThe greatest common factor is %d.", gcf_counter)
    } else {
        printf("\n\nBoth numbers must be greater than 0")
    }

    printf("\n\nDone.\n");
}
