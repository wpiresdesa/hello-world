#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# This file have been added by Wanderley Pires de Sá
# Modifications have been done to understand git local repository

# 30/October/2018 - #01 - CheckIfANumberIsOddOrEven.py before git add <this file>
# 30/October/2018 - #02 - CheckIfANumberIsOddOrEven.py before git add <this file>

# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
