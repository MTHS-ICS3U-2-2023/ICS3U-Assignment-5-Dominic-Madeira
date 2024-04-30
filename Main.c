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
    int counter;
    int gcf;


    // input
    number1 = get_int("Enter an integer ");
    number2 = get_int("Enter another integer ");

    // process
    // find the smallest number
    if (number1 > number2) {
        counter = number2;
    } else {
        counter = number1;
    }

    // find the GCF
    while (counter > 0) {
        if (number1 % counter == 0 && number2 % counter == 0) {
            gcf = counter;
            break;
        }
        counter--;
    }

    printf("\n\nDone.\n");
}
