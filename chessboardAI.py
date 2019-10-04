class MinimaxTree(object): 
	def __init__(self): 
		self.children = []
		self.data = None
		self.parent = None
		self.min_node = False
		self.resulting_board = None

	def add_data(self, data): 
		self.data = data

	def add_child(self, child): 
		child.parent = self
		child.min_node = not self.min_node
		self.children.append(child)

	def add_board(self, board): 
		self.resulting_board = board




# Some pseudocode: 
# 	1. create COPY of board (not just a pointer to the board)
# 	create MinimaxTree with an empty/dummy root -- this will be the ultimate decision the player makes 

# 	2. make a list
# 	init MinimaxTrees for each possible move 
# 		create a copy of the board given that move
# 		add this board to the MinimaxTree
# 	add the instances initiated to that list
# 	iterate throguh the list, adding each MinimaxTree as children

# 	3. for each child in children, repeat step 2

# 	Traverse this tree, making sure the min/max is working 
# 	Add pruning if possible