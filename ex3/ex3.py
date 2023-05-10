#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: ./ex3/ex3.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 数字和数学运算
#

def main():
    # print
    print("I will now count my chickens:")

    print("Hens", 25 + 30 / 6)
    print("Roosters", 100 - 25 * 3 % 4)

    print("Now I will count the eggs:")
    print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
    print("Is it true thar 3 + 2 < 5 - 7 ?")

    print(3 + 2 < 5 - 7)
    print ("what is 3 + 2?",3 + 2)
    print ("What is 5 - 7?", 5 - 7)

    print("Oh, that's why it's False.")

    print("How about some more.")

    print("Is it greater?", 5 > -2)
    print("Is it greater or equal?", 5 >= -2)
    print("Is it less or equal?", 5 <= -2)

    print("3.1 + 2.49 =", 3.1 + 2.49)

if __name__ == "__main__":
    main()
