#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Sept 27 2022
# This program asks the user for the radius of
# a circle in cm. It then calculates the circumference of the circle using tau


import constants


def main():
    # get input for radius from the user
    radius = float(input("Enter the radius of the circle in cm: "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
