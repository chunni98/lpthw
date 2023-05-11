#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: ./ex6/ex6.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 字符串和文本
#

def main():
    types_of_people = 10
    x = f"There are {types_of_people} types of people."

    binary = "binary"
    do_not = "don't"
    y = f"Those who know {binary} and those who {do_not}."

    print (x)
    print (y)

    print (f"I said: {x}")
    print (f"I also said: '{y}'")

    hilarious = False
    joke_evaluation = "Isn't that joke so funny? {}!"

    print (joke_evaluation.format(hilarious))

    w = "This is the left side of..."
    e = "a string with a right side."

    print (w + e)

    str1 = "Hello,{}"
    print (str1.format("World!"))

if __name__ == "__main__":
    main()
