import os
import sys
from typing import Match

# Fixes CWD
os.chdir(sys.path[0])

HPos = 0
Depth = 0

def PerformInstruction(instruction):
	global HPos
	global Depth

	instruction = instruction.split(' ')

	opcode = instruction[0]
	operand = int(instruction[1])

	# Theres no switch statements in python so uh ¯\_(ツ)_/¯
	# NVM THEY ADDED SWITCH STATEMENTS????? (https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching)

	match opcode:
		case "forward":
			HPos += operand
		case "down":
			Depth += operand
		case "up":
			Depth -= operand

with open("input.txt") as file:
	for line in file.readlines():
		PerformInstruction(line.rstrip('\n'))

print(f"HPos: {HPos}, Depth: {Depth}, Answer: {HPos * Depth}")

