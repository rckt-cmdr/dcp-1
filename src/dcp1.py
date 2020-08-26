#!/usr/bin/python3

# File: test_dcp1.py
# Author: Jonathan Belden
# Descripton: Daily Codding Challenge #1 - Figure out if two numbers add up to a specified value


import argparse


def main():
    pass  # reserved for later expansion with argparse


def evaluate(numbers:list, kValue:int):
    result = False  # assuming false until proven true

    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == kValue:
                result = True

    return result


def evaluateSinglePass(numbers:list, kValue:int):
    result = False  # assuming false until proven true
    
    numbers.sort()
    for num in numbers:
        if kValue - num in numbers:
            result = True

    return result

if __name__ == "__main__":
    main()