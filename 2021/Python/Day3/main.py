import os
import sys

# Fixes CWD
os.chdir(sys.path[0])

Numbers = []
NumberLength = 12

O2Num = "0"
CO2Num = "0"

def CountBits(bitIndex, isReversed, nums):
	oneCount = 0

	for number in nums:
		if (number[bitIndex] == "1"):
			oneCount += 1
		elif (number[bitIndex] != "0"):
			raise Exception("WHAT THE FUUUUck")

			#print(f"Index: {i}, Number: {number.rstrip(os.linesep)}, BitIndex: {bitIndex}, Bit: {number[bitIndex]}, CurrentCount: {count}, IsReversed: {isReversed}")

	# The "isReversed !=" is just and XOR
	if (isReversed != (oneCount >= len(nums) / 2)):
		print(f"Removing 0s (oneCount: {oneCount}, zeroCount: {abs(len(nums) - oneCount)}, listLenght: {len(nums)}, reversed: {isReversed})")
		return '0'
	else:
		print(f"Removing 1s (oneCount: {oneCount}, zeroCount: {abs(len(nums) - oneCount)}, listLenght: {len(nums)}, reversed: {isReversed})")
		return '1'

def RemoveNumbers(bitIndex, bitToRemove, nums):
	if (len(nums) == 1): return nums[0]

	numsToRemove = []

	for number in nums:
		if (number[bitIndex] == bitToRemove): numsToRemove.append(number)

	for number in numsToRemove:
		nums.remove(number)
		if (len(nums) == 1): break

	print(f"New Num Count: {len(nums)}")
	if (len(nums) == 1): return nums[0]

with open("input.txt") as file:
	Numbers = file.readlines()

O2Nums = Numbers.copy()
CO2Nums = Numbers.copy()

for i in range(NumberLength):
	tmpVal = RemoveNumbers(i, CountBits(i, False, O2Nums), O2Nums)
	if (tmpVal != None): O2Num = tmpVal.rstrip('\n')
	#print(f"Iteration {i}, O2: {tmpVal}")

	tmpVal = RemoveNumbers(i, CountBits(i, True, CO2Nums), CO2Nums)
	if (tmpVal != None): CO2Num = tmpVal.rstrip('\n')
	#print(f"Iteration {i}, CO2: {tmpVal}")

print(f"O2: {O2Num} ({int(O2Num, 2)}), CO2: {CO2Num} ({int(CO2Num, 2)})")
print(f"Answer: {int(O2Num, 2) * int(CO2Num, 2)}")