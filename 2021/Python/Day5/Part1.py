import os
import sys
import math
import time

# Fixes CWD
os.chdir(sys.path[0])

Lines = []
Points = {}

class Vector2:
	TotalComparisons = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f"({self.x}, {self.y})"

	def __eq__(self, other): 
		if not isinstance(other, Vector2): return NotImplemented

		Vector2.TotalComparisons += 1
		return (self.x == other.x) and (self.y == other.y)

	def __hash__(self):
		return hash(str(self))

	@staticmethod
	def Distance(vecA, vecB):
		# Just use basic pythagoras
		return math.sqrt((vecB.x - vecA.x) ** 2 + (vecB.y - vecA.y) ** 2)

	@staticmethod
	def Lerp(vecA, vecB, t, shouldRound = False):
		lerpX = vecA.x + (vecB.x - vecA.x) * t
		lerpY = vecA.y + (vecB.y - vecA.y) * t

		if (shouldRound):
			lerpX = round(lerpX)
			lerpY = round(lerpY)

		return Vector2(lerpX, lerpY)


class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def IsStraight(self):
		return (self.p1.x == self.p2.x) or (self.p1.y == self.p2.y)

	def GetPoints(self):
		points = []
		distance = Vector2.Distance(self.p1, self.p2)
		timeStep = 1 / distance

		for i in range(math.ceil(distance) + 1):
			point = Vector2.Lerp(self.p1, self.p2, timeStep * i, True)
			points.append(point)

		return points

with open("input.txt") as file:
	lines = file.readlines()

	for line in lines:
		line = line.rstrip('\n')
		linePoints = line.split(" -> ")

		p1 = linePoints[0].split(',')
		p2 = linePoints[1].split(',')

		newLine = Line(Vector2(int(p1[0]), int(p1[1])), Vector2(int(p2[0]), int(p2[1])))
		if (newLine.IsStraight()): Lines.append(newLine)

print("Calculating Line Points...", end=' ')
startTime = time.time()

for line in Lines:
	for point in line.GetPoints():
		if point in Points: Points[point] += 1
		else: Points[point] = 1

print(f"Complete! (Took {time.time() - startTime:.2f} seconds to complete)")
print(f"There are {len(Points)} points in total")

print("Finding Overlapped Points...", end=' ')
startTime = time.time()

overlappedPoints = 0
for point in Points:
	if (Points[point] > 1): overlappedPoints += 1

print(f"Complete! (Took {time.time() - startTime:.2f} seconds to complete, Made {Vector2.TotalComparisons} Vector2 Comparisons)")
print(f"There are {overlappedPoints} Overlapped points")