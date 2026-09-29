#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: September 2026
# This program calculates the area and perimeter of a rectangle
# based on user input for length and width.


def main():
    # input
    print("Calculate the area and perimeter of a rectangle.")
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print(f"The area is {area} cm².")
    print(f"The perimeter is {perimeter} cm.")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
