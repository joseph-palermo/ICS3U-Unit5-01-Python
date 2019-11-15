#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program converts temperature from Celcius to Farenheit


def conversion():
    # this program converts Celcius to Farenheit

    # input
    try:
        tc = float(input("Enter a temperature here (°C): "))

        # process
        tf = (tc*9/5)+32

        # Output
        print("")
        print("{0}°C is {1}°F"
              .format(tc, tf))
    except ValueError:
        print("")
        print("Please insert a valid temperature.")


def main():
    # this function calls other functions

    # call function
    conversion()


if __name__ == "__main__":
    main()
