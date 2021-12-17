import os
import sys

# Fixes CWD
os.chdir(sys.path[0])

IncreaseCount = 0

with open("input.txt") as file:
	lines = file.readlines()
	for i in range(len(lines)):
		if (i == 0): continue

		if (int(lines[i].rstrip('\n')) > int(lines[i - 1].rstrip('\n'))): IncreaseCount += 1

print(f"Depth Increased {IncreaseCount} Times")