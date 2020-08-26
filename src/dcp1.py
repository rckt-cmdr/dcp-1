#!/usr/bin/python3

# File: test_dcp1.py
# Author: Jonathan Belden
# Descripton: Daily Codding Challenge #1 - Figure out if two numbers add up to a specified value


import argparse


def main():
	parser = argparse.ArgumentParser(prog="dcp1", description="Daily Coding Challenge #1")
	parser.add_argument("run", default="run")
	parser.add_argument("-o", "--optimized", action="store_true")
	args = parser.parse_args()

	if args.run == "run":
		desc = ("=================================================\n"
				"This program asks for a sequence of integers\n"
				"and then for a single integer. It then evaluates\n"
				"if any two values in the specified sequence add\n"
				"up to the single integer.\n"
				"=================================================\n\n")
		print(desc)
		print(askForInput(args.optimized))


def askForInput(runOptimized=False):
	result = None
	# ToDo: need to split input on space delimiters
	listInput = list(input("Please enter two or more numbers, each seperated by a space: "))
	kInput = int(input("\n\nNow, please enter a single number: "))

	if runOptimized:
		result = evaluateSinglePass(listInput, kInput)
	else:
		result = evaluate(listInput, kInput)

	return result


def evaluate(numbers:list, kValue:int):
	result = False  # assuming false until proven true

	for num1 in numbers:
		for num2 in numbers:
			if num1 + num2 == kValue:
				result = True
	
	if result:
		print(f"{num1} + {num2} = {kValue}")
	else:
		print(f"No combination of numbers add up to {kValue}")

	return result


def evaluateSinglePass(numbers:list, kValue:int):
	result = False  # assuming false until proven true
	
	numbers.sort()
	for num in numbers:
		if int(kValue) - int(num) in numbers:
			result = True
			print(f"{num} + {kValue - num} = {kValue}")
		else:
			print(f"No combination of numbers add up to {kValue}")

	return result

if __name__ == "__main__":
	main()