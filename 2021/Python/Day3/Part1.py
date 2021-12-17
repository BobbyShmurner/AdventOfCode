import os
import sys

# Fixes CWD
os.chdir(sys.path[0])

Numbers = []
NumberLength = 12

Gamma = ""
Epsilon = ""

def CountBits(bitIndex):
	global Numbers
	oneCount = 0

	for number in Numbers:
		if (number[bitIndex] == "1"):
			oneCount += 1

	if (oneCount >= len(Numbers) / 2):
		return '0'
	else:
		return '1'

with open("input.txt") as file:
	Numbers = file.readlines()

Gamma = "0" * NumberLength
Epsilon = "0" * NumberLength

for i in range(NumberLength):
	gamaList = list(Gamma)
	gamaList[i] = CountBits(i)
	Gamma = "".join(gamaList)

Gamma = int(Gamma, 2)
Epsilon = Gamma ^ int("1" * NumberLength, 2)

print(f"Gamma: {Gamma}, Epsilon: {Epsilon}, Answer: {Gamma * Epsilon}")

