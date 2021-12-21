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
	def Lerp(vecA, vecB, t):
		lerpX = vecA.x + (vecB.x - vecA.x) * t
		lerpY = vecA.y + (vecB.y - vecA.y) * t

		roundLerpX = round(lerpX)
		roundLerpY = round(lerpY)

		return Vector2(roundLerpX, roundLerpY)


class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

		self.CalculatePoints()

	def GetGradient(self):
		if (self.p2.x - self.p1.x == 0): return 0
		return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

	def IsStraight(self):
		return (self.p1.x == self.p2.x) or (self.p1.y == self.p2.y)

	def IsDiagonal(self):
		return abs(self.GetGradient()) == 1

	def Length(self):
		# Gets the amounts of points on the line, Inclusing the 2 points that define the line
		# NOTE: This only works with horizontal, vertical, or 45 degree lines
		if (self.IsStraight()): return math.ceil(Vector2.Distance(self.p1, self.p2)) + 1
		
		return int(abs(self.p2.x - self.p1.x)) + 1

	def CalculatePoints(self):
		points = []
		length = self.Length()

		timeStep = 1 / (length - 1)

		for i in range(length):
			point = Vector2.Lerp(self.p1, self.p2, timeStep * i)
			if (point == None): continue

			points.append(point)

		self.m_Points = points

	def GetPoints(self):
		return self.m_Points

with open("input.txt") as file:
	lines = file.readlines()

	for line in lines:
		line = line.rstrip('\n')
		linePoints = line.split(" -> ")

		p1 = linePoints[0].split(',')
		p2 = linePoints[1].split(',')

		newLine = Line(Vector2(int(p1[0]), int(p1[1])), Vector2(int(p2[0]), int(p2[1])))
		if (newLine.IsStraight() or newLine.IsDiagonal()): Lines.append(newLine)

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