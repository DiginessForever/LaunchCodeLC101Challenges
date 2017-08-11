class TreeNode:
	value = 0
	left = None
	right = None

	def __init__(self, value):
		self.value = value

	def insert(self, value):
		if self.value > value:
			if type(self.left) != TreeNode:
				self.left = TreeNode(value)
			else:
				self.left.insert(value)
		elif self.value <= value:
			if type(self.right) != TreeNode:
				self.right = TreeNode(value)
			else:
				self.right.insert(value)

	#This is so slow that I have to put it down (do NOT use, I gave up and 
	#force quit the program before it ended, and that was for merging two SMALL trees):
	def insertNode(self, node):
		while type(node) != None and (type(node.left) == TreeNode or type(node.right) == TreeNode):
			self.insert(node.value)
			node.delete(node.value)
		if type(node) != None:
			self.insert(node.value) #one last insert to account for tree root value.

	def flattenTree():
		'''Makes a list out of the tree'''
		myList = []
		if type(self.left) == TreeNode:
			myList += self.left.flattenTree()
		myList += self.value
		if type(self.right) == TreeNode:
			myList += self.right.flattenTree()
		return myList		
				
	def print(self):
		if type(self.left) == TreeNode:
			self.left.print()
		print(self.value)
		if type(self.right) == TreeNode:
			self.right.print()

	def contains(self, value):
		if self.value == value:
			return True
		if self.value > value:
			if type(self.left) == TreeNode:
				if self.left.contains(value):
					return True
		elif self.value < value:
			if type(self.right) == TreeNode:
				if self.right.contains(value):
					return True
		return False

	def delete(self, value):
		if value is not None:
			if (self.value == value):
				if type(self.left) == TreeNode:
					#print("Aaahh, I have kids!  I'll sacrifice myself to save the kids!  Leftie, you're the one now!")
					self.left.insertNode(self.right)
					self = self.left
				elif type(self.right) == TreeNode:
					#print("Aaah, I have no leftie, rightie, you're it!  Save yourself!")
					self = self.right
				else:  #poor guy has no kids
					self = None
					return
			while self.contains(value):
				if self.value > value:
					self.left.delete(value)
				else:
					self.right.delete(value)		

#Mike recommends this talk on Youtube - PyCon 2017 - Dictionaries - What was once old is new again...
def main():
	tree = TreeNode(5)
	tree = doSomeInserts(tree, [3,4,7,13,0,20,-5])
	tree = doSomeDeletes(tree, [-5,20,0,13])
	tree.print()

	tree2 = TreeNode(3)
	tree2 = doSomeInserts(tree, [5,9,9,12,-3,-2,-1])
	
	for i in tree.flattenTree():
		tree2.insert(i)

	tree2.print()

def doSomeInserts(tree, list):
	for i in range(0, len(list)):
		tree.insert(list[i])
	return tree

def doSomeDeletes(tree, list):
	for i in range(0, len(list)):
		tree.delete(list[i])
	return tree

if __name__ == "__main__":
	main()

