#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program reads an integer and display its sign


def main():
    # this code program reads an integer and display its sign

    # input
    integer = int(input("Enter a number are positive or negative: "))

    # process
    if integer > 0:
        print(" + ")
    elif integer < 0:
        print(" - ")
    else:
        print("0")


if __name__ == '__main__':
    main()
