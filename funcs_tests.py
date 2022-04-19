import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
		
	# ADD MORE TESTS!!!! 

	def test_check_rows0(self):
		puzzle = []
		puzzle.append([5, 1, 2, 3, 4])
		puzzle.append([1, 2, 3, 4, 5])
		puzzle.append([2, 3, 0, 5, 1])
		puzzle.append([3, 0, 0, 1, 2])
		puzzle.append([0, 0, 0, 0, 0])
		self.assertTrue(check_rows_valid(puzzle))
		
	# def test_check_columns0(self):
	# 	puzzle = []
	# 	puzzle.append([5, 1, 2, 3, 4])
	# 	puzzle.append([1, 2, 3, 4, 5])
	# 	puzzle.append([2, 3, 0, 5, 1])
	# 	puzzle.append([3, 0, 0, 1, 2])
	# 	puzzle.append([0, 0, 0, 0, 0])
	# 	self.assertTrue(check_columns_valid(puzzle))
		
	def test_check_cages0(self):
		puzzle = []
		puzzle.append([5, 1, 2, 3, 4])
		puzzle.append([1, 2, 3, 4, 5])
		puzzle.append([2, 3, 0, 5, 1])
		puzzle.append([3, 0, 0, 1, 2])
		puzzle.append([0, 0, 0, 0, 0])
		cages = []
		cages.append([6, 2, 0, 5])
		cages.append([7, 3, 2, 6, 7])
		cages.append([9, 2, 4, 9])
		self.assertTrue(check_cages_valid(puzzle, cages))
		
	# def test_check_valid0(self):
	#    puzzle = []
	#    puzzle.append([5, 1, 2, 3, 4])
	#    puzzle.append([1, 2, 3, 4, 5])
	#    puzzle.append([2, 3, 0, 5, 1])
	#    puzzle.append([3, 0, 0, 1, 2])
	#    puzzle.append([0, 0, 0, 0, 0])
	#    cages = []
	#    cages.append([6, 2, 0, 5])
	#    cages.append([7, 3, 2, 6, 7])
	#    cages.append([9, 2, 4, 9])
	#    self.assertTrue(check_valid(puzzle, cages))
  
	def test_check_one_row1(self):
		puzzle = []
		puzzle.append([5, 1, 2, 3, 4])
		puzzle.append([1, 2, 3, 4, 5])
		puzzle.append([2, 3, 0, 5, 1])
		puzzle.append([3, 0, 0, 1, 2])
		puzzle.append([0, 0, 0, 0, 0])
		self.assertTrue(check_one_row(puzzle))
	
	def test_check_one_row2(self):
		row = [1,1,1,1,1]
		self.assertFalse(check_one_row(row))
  
	def test_check_one_column1(self):
		puzzle = []
		puzzle.append([5, 1, 2, 3, 4])
		puzzle.append([1, 2, 3, 4, 5])
		puzzle.append([2, 3, 0, 5, 1])
		puzzle.append([3, 0, 0, 1, 2])
		puzzle.append([4, 0, 0, 0, 0])
		self.assertTrue(check_columns_valid(puzzle))
  
	def test_check_one_column2(self):
		puzzle = []
		puzzle.append([5, 4, 3, 2, 1])
		puzzle.append([5, 4, 3, 2, 1])
		puzzle.append([5, 4, 3, 2, 1])
		puzzle.append([5, 4, 3, 2, 1])
		puzzle.append([5, 4, 3, 2, 1])
		self.assertFalse(check_columns_valid(puzzle))
	def test_check_one_cage1(self):
		puzzle = []
		puzzle.append([5, 1, 2, 3, 4])
		puzzle.append([1, 2, 3, 4, 5])
		puzzle.append([2, 3, 0, 5, 1])
		puzzle.append([3, 0, 0, 1, 2])
		puzzle.append([0, 0, 0, 0, 0])
		cage = []
		cage.append([5,2, 3, 4])
		self.assertFalse(check_one_cage(puzzle, cage[0]))
	def test_check_one_cage2(self):
		puzzle = []
		puzzle.append([5, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		cage = [9, 3, 0, 5, 6]
		self.assertTrue(check_valid(puzzle, [cage]))
	def test_check_valid1(self):
		puzzle = []
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		puzzle.append([0, 0, 0, 0, 0])
		cages = []
		cages.append([4, 3, 0, 1, 6])
		cages.append([8, 3, 2, 6, 7])
		cages.append([9, 2, 4, 9])

		self.assertTrue(check_valid(puzzle, cages))

	def test_rows(self):
		row = [1,2,3,4,5]
		self.assertTrue(check_one_row(row))

	def test_rows2(self):
			row = [1,0,3,4,5]
			self.assertTrue(check_one_row(row))

	def test_cages_valid2(self):
		puzzle = [[3,5,2,1,4], [5,1,3,4,2], [2,4,1,5,3], [1,2,4,3,5], [4,3,5,2,1]]
		cages = [[9,3,0,5,6], [7,2,1,2], [10,3,3,8,13], [14,4,4,9,14,19], [3,1,7], [8,3,10,11,16], [13,4,12,17,21,22], [5,2,15,20], [6,3,18,23,24]]
		for i in range(9):
			self.assertTrue(check_one_cage(puzzle, cages[i]))

	def test_error(self):
		puzzle = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
		cages = [[1, 1, 5]]
		self.assertTrue(check_columns_valid(puzzle))
# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

