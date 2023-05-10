#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: ./ex4/ex4.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 这个文件是习题 4 变量和命名的练习
#

def main():
    cars = 100
    space_in_a_car = 4
    drivers = 30
    passengers = 90
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven

    print ("There are", cars, "cars available.")
    print ("There are only", drivers, "drivers available.")
    print ("There will be", cars_not_driven, "empty cars today")
    print ("We can transport", carpool_capacity, "people today.")
    print ("We have", passengers, "to carpool today.")
    print ("We need to put about", average_passengers_per_car, "in each car")

if __name__ == "__main__":
    main()
