#!/usr/bin/python3

# File: test_dcp1.py
# Author: Jonathan Belden
# Descripton: Daily Codding Challenge #1 - Figure out if two numbers add up to a specified value


import argparse
import sys


def main():			
	parser = argparse.ArgumentParser(prog="dcp1.py", description="Daily Coding Challenge #1")
	parser.add_argument("-l", "--list", nargs="*", type=str, help="A sequence of at least 2 numbers, separated by <space character>", required=True)
	parser.add_argument("-i", "--integer", nargs=1, type=int, help="A single integer for comparison", required=True)
	parser.add_argument("-o", "--optimized", action="store_true", help="Evaluate the sequence with an optimized algorithm")
	args = parser.parse_args()

	# converting list sequence to all ints
	listInput = [int(i) for i in args.list]
	kValueInput = args.integer[0]  # not sure why this is neccessary, but it is
	
	if len(listInput) < 2:
		print("\n\nNot enough numbers in the sequence!\n")
		sys.exit()
	elif not args.integer:
		print("\n\nYou must specify an integer!\n")
		sys.exit()
	elif args.optimized:
		print("ln 39")
		evaluateSinglePass(listInput, kValueInput)
	else:
		print("ln 42")
		evaluate(listInput, kValueInput)


def evaluate(numbers:list, kValue:int):
	numPairFound = False  # assuming false until proven true

	for num1 in numbers:
		for num2 in numbers:
			if num1 + num2 == kValue:
				numPairFound = True
				print(f"\n>> Found one! [{num1} + {num2} = {kValue}]\n\n")

	if not numPairFound:
		print(f"\n>> No combination of numbers add up to {kValue}\n\n")

	return numPairFound


def evaluateSinglePass(numbers:list, kValue:int):
	numPairFound = False  # assuming false until proven true
	
	numbers.sort()
	for num in numbers:
		if kValue - num in numbers:
			numPairFound = True
			print(f"\n>> Found one! [{num} + {kValue - num} = {kValue}]\n\n")
	
	if not numPairFound:
		print(f"\n>> No combination of numbers add up to {kValue}\n\n")

	return numPairFound

if __name__ == "__main__":
	main()