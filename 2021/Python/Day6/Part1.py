import os
import sys

# Fixes CWD
os.chdir(sys.path[0])

CurrentStates = []

def UpdateStates(states):
	for i in range(len(states)):
		if (states[i] == 0):
			states[i] = 6
			states.append(8)
		else:
			states[i] -= 1

with open("input.txt") as file:
	fishStates = file.read().rstrip('\n').split(',')
	
	for fishState in fishStates:
		CurrentStates.append(int(fishState))

for day in range(80):
	UpdateStates(CurrentStates)

print(f"Total Fish: {len(CurrentStates)}")
