import os
import sys

# Fixes CWD
os.chdir(sys.path[0])

class Board:
	def __init__(self, numbers):
		self.m_Numbers = []
		self.m_NumbersCalled = []

		for row in numbers:
			self.m_Numbers.append(row.rstrip('\n').split(' '))

		# Remove Any Blank Items From The List
		for row in self.m_Numbers:
			while "" in row:
				row.remove("")

			# Initalise m_NumbersCalled to False
			tmpFalseList = []
			for num in row:			
				tmpFalseList.append(False)

			self.m_NumbersCalled.append(tmpFalseList)

	def GetSumOfUncalledNumbers(self):
		sum = 0

		for x in range(len(self.m_Numbers)):
			for y in range(len(self.m_Numbers[x])):
				if not (self.m_NumbersCalled[x][y]): sum += int(self.m_Numbers[x][y].rstrip('\n'))

		return sum
				

	def CheckLine(self, index, isRow):
		isBingo = True
		for i in range(len(self.m_NumbersCalled)):
			numCalled = False
			numCalled = self.m_NumbersCalled[i][index] if isRow else self.m_NumbersCalled[index][i]

			if not numCalled:
				isBingo = False
				break

		if isBingo:
			print(f"Bingo! \nSum: {self.GetSumOfUncalledNumbers()}, Last Num: {self.m_LastNumberCalled}, Answer: {self.GetSumOfUncalledNumbers() * int(self.m_LastNumberCalled)}")

			# Yes i am just crashing the program when there's a bingo, whatcha gonna do about it?
			raise Exception("Bingo!")
			

	def IsBingo(self):
		for x in range(len(self.m_NumbersCalled)):
			if not self.m_NumbersCalled[x][x]: continue

			self.CheckLine(x, False)
			self.CheckLine(x, True)
			
		


	def NumberCalled(self, num):
		for x in range(len(self.m_Numbers)):
			if num in self.m_Numbers[x]:
				y = self.m_Numbers[x].index(num)
				self.m_NumbersCalled[x][y] = True
				self.m_LastNumberCalled = num

				self.IsBingo()

CalledNums = []
Boards = []

with open("input.txt") as file:
	lines = file.readlines()

	CalledNums = lines[0].rstrip('\n').split(',')
	for i in range(2): lines.pop(0)

	tmpBoardLines = []
	for line in lines:
		if (line == '\n'):
			newBoard = Board(tmpBoardLines)
			Boards.append(newBoard)

			tmpBoardLines = []
			continue

		tmpBoardLines.append(line.rstrip('\n'))
	
for num in CalledNums:
	for board in Boards:
		board.NumberCalled(num)
