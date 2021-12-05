#!/usr/bin/env python3

class BinaryTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if self.data == data:
			return
		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinaryTreeNode(data)
		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinaryTreeNode(data)

	def print_in_order(self, root):
		if root:
			self.print_in_order(root.left)
			print(root.data, end=", ")
			self.print_in_order(root.right)

	def print_pre_order(self, root):
		if root:
			print(root.data, end=", ")
			self.print_pre_order(root.left)
			self.print_pre_order(root.right)

	def print_post_order(self, root):
		if root:
			self.print_post_order(root.left)
			self.print_post_order(root.right)
			print(root.data, end=", ")


# tree = BinaryTreeNode(20)
# tree.add_child(2)
# tree.add_child(31)
# tree.add_child(13)
# tree.add_child(1)
# tree.add_child(3)
# tree.add_child(5)


def binary_search(arr, item, left_index, right_index):
	middle = (left_index + right_index) // 2
	if arr[middle] == item:
		return middle

	if item < arr[middle]:
		right_index = middle
		return binary_search(arr, item, left_index, right_index)
	else:
		left_index = middle
		return binary_search(arr, item, left_index, right_index)

	return -1


arr = [-2, 3, 4, 7, 8, 9, 11, 13]
print(binary_search(arr, 7, 0, len(arr)))
