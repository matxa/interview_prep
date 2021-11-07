#!/usr/bin/env python3

from typing import Counter


class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node

class LinkedList:
	"""Linked List"""
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data, self.head)
		self.head = new_node

	def insert_at_the_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		current_node = self.head
		while current_node.next_node:
			current_node = current_node.next_node
		current_node.next_node = Node(data, None)

	def insert_at_index(self, index, data):
		if index > self.length() or index < 0:
			raise Exception("Out of range index")
		if index == self.length():
			self.insert_at_the_end(data)
			return
		if index == 0:
			self.insert_at_beginning(data)
			return

		count = 0
		current_node = self.head
		while current_node.next_node:
			if count == (index - 1):
				current_node.next_node = Node(data, current_node.next_node)
			count+=1
			current_node = current_node.next_node

	def insert_in_sorted(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return
		if data < self.head.data:
			self.insert_at_beginning(data)
			return

		current_node = self.head
		while current_node:
			if current_node.next_node is None:
				current_node.next_node = Node(data, current_node.next_node)
				break
			if current_node.data < data and current_node.next_node.data >= data:
				current_node.next_node = Node(data, current_node.next_node)
				break
			current_node = current_node.next_node

	def reverse(self):
		if self.length() == 1 or self.head is None:
			return
		current_node = self.head
		self.head = None
		while current_node:
			self.insert_at_beginning(current_node.data)
			current_node = current_node.next_node

	def add_from_array(self, list_of_data):
		self.head = None
		if len(list_of_data) <= 0:
			raise Exception("Array is empty")
		for i in range(len(list_of_data)):
			self.insert_in_sorted(list_of_data[i])

	def pop(self):
		self.head = self.head.next_node
		return

	def length(self):
		if self.head is None:
			return 0
		current_node = self.head
		counter = 0
		while current_node:
			current_node = current_node.next_node
			counter += 1
		return counter

	def list_sum(self):
		sum_total = 0
		current_node = self.head
		while current_node:
			sum_total += current_node.data
			current_node = current_node.next_node
		return sum_total

	def delete_at_index(self, index):
		if index > self.length() or index < 0:
			raise Exception("Out of range index")
		if index == 0:
			self.pop()
			return

		count = 0
		current_node = self.head
		while current_node.next_node:
			if (count + 1) == index:
				current_node.next_node = None
				break
			if count == (index - 1):
				current_node.next_node = current_node.next_node.next_node
				break
			count+=1
			current_node = current_node.next_node

	def print_ll(self):
		if self.head is None:
			print("LinkedList is empty")

		current_node = self.head
		while current_node:
			print(f"[ {current_node.data} ]", end="-->" if current_node.next_node != None else "\n")
			current_node = current_node.next_node

	def free(self):
		self.head = None
		return
