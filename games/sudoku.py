import string

class Sudoku:
	"""Game of Sudoku with AutoComplete and check when complete."""
	
	def __init__(self):
		
		#blank starting board
		self.board = [['' for i in range(9)] for row in range(9)] 
		
		#dictionary of valid positions and their list positions
		self.positions = {string.ascii_uppercase[col]+string.digits[row+1]:(row,col) for row in range(9) for col in range(9)}
		
	def display(self):
		"""Print self.board with guides."""
		
		#TODO: print values from self.board
		pass
		
