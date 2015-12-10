class PycrossBoard:
	@classmethod
	def row_hints_from_solution(c, solution):
		row_hints = []
		
		for row in solution:
			# check to ensure rectangular board
			row_width = len(row)
			if row_width != len(solution[0]):
				raise Exception("Encountered rows of different length.")
			
			hint_count = 0
			in_block = False # Currently in a run of filled squares
			hints = []
			for square in row:
				
				if in_block:
					if square == None:
						in_block = False
						hints.append(hint_count)
						hint_count = 0
					elif square == True:
						hint_count += 1
					
				else:
					if square == True:
						in_block = True
						hint_count += 1
					
			if in_block:
				hints.append(hint_count)
			row_hints.append(tuple(hints))
		return row_hints

	@classmethod
	def col_hints_from_solution(c, solution):
		return c.row_hints_from_solution(zip(*solution))
	
	def __init__(self, row_hints, col_hints):
		self.board = []
		self.height = len(row_hints)
		self.width = len(col_hints)
		self.row_hints = row_hints
		self.col_hints = col_hints
		
		for y in xrange(self.height):
			row = []
			for x in xrange(self.width):
				row.append(None)
			self.board.append(row)
			
	def print_text(self):
		max_row = len(max(self.row_hints, key=len)) 
		max_col = len(max(self.col_hints, key=len))
		grid_width = self.width + max_row
		grid_height = max_col + self.height
		print_grid = []
		for y in xrange(max_col):
			print_row = []
			for x in xrange(max_row):
				print_row.append(' ')
			for col_hint in self.col_hints:
				if len(col_hint) >= max_col - y:
					print_row.append(col_hint[len(col_hint) - max_col + y])
			print_grid.append(print_row)
			
		for y in xrange(self.height):
			print_row = []
			for x in xrange(max_row):
				row_hint = self.row_hints[y]
				if len(row_hint) >= max_row - x:
					print_row.append(row_hint[len(row_hint) - max_row + x])
				else:
					print_row.append(' ')
			for x in xrange(self.width):
				square = self.board[y][x]
				if square == None:
					print_row.append(' ')
				elif square == False:
					print_row.append('.')
				elif square == True:
					print_row.append('X')
			print_grid.append(print_row)
			
		for row in print_grid:
			r = ""
			for c in row:
				r += str(c)
			print(r)
			