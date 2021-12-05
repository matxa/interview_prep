#!/usr/bin/env python3
class Node:
	"""Stack and Queues Nodes"""
	def __init__(self, data, prev, _next):
		self.data = data
		self.prev = prev
		self.next = _next


class Stacks:
	"""Stack data structure"""
	def __init__(self):
		self.head = None

	def push(self, data):
		self.head = Node(data, None, self.head)
		return

	def pop(self):
		temp_node = None
		if self.head is None:
			return
		if self.head.next is None:
			temp_node = self.head
			self.head = None
			return temp_node.data

		temp_node = self.head
		self.head = self.head.next
		return temp_node.data

	def _print(self):
		if self.head is None:
			print("Stack is empty")
		current_node = self.head
		while current_node:
			print(f"[ {current_node.data} ]")
			current_node = current_node.next

# TEST
stacks = Stacks()
stacks._print()
print(f"pop -> {stacks.pop()}")
stacks._print()
