import unittest
from pycross_board import PycrossBoard

class BasicBoardTestFixture(unittest.TestCase):
	def setUp(self):
		self.square_board = PycrossBoard([[1],[2],[2]],[[2],[2],[1]])
		self.rectangle_board = PycrossBoard([[1,1],[1,1,1],[1]],[[2],[0],[2],[0],[2]])
		
	#def tearDown(self):
	
	def test_print_text(self):
		print("")
		print("")
		self.square_board.print_text()
		print("")
		self.rectangle_board.print_text()
		print("")
	
	def test_dimensions(self):
		self.assertEqual(self.square_board.width, 3)
		self.assertEqual(self.square_board.height, 3)
	
	def test_rectangle_dimensions(self):
		self.assertEqual(self.rectangle_board.width, 5)
		self.assertEqual(self.rectangle_board.height, 3)
	
	def test_from_soln(self):
		self.square_board_soln = [[True, None, None],[True, True, None],[None, True, True]]
		row_hints = PycrossBoard.row_hints_from_solution(self.square_board_soln)
		col_hints = PycrossBoard.col_hints_from_solution(self.square_board_soln)
		self.square_board_from_soln = PycrossBoard(row_hints, col_hints)
		print("")
		print("")
		self.square_board_from_soln.print_text()
		print("")
		
suite = unittest.TestLoader().loadTestsFromTestCase(BasicBoardTestFixture)
unittest.TextTestRunner(verbosity=2).run(suite)