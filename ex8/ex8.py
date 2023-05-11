#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: ex8/ex8.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 打印，打印
#

def main():
    formatter = "{} {} {} {}"

    print (formatter.format (1, 2, 3, 4))
    print (formatter.format ("one", "two", "three", "four"))
    print (formatter.format (True, False, False, True))
    print (formatter.format (formatter, formatter, formatter, formatter))
    print(formatter.format(
8   "Try your",
9   "Own text here",
10  "Maybe a poem",
11  "Or a song about fear"
12  ))

if __name__ == "__main__":
    main()
