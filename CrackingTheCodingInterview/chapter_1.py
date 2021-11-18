#!/usr/bin/env python3

def reverse_str(string):
	new_str = ''
	for index in range(1, len(string)):
		new_str += string[index * -1]
	new_str += string[0]
	return new_str


def is_unique(string):
	return len(string) == len(set(string))


def check_permutation(str1, str2):
	if len(str1) != len(str2):
		return

	str1 = sorted(str1)
	str2 = sorted(str2)

	return str1 == str2


def urlify(string, string_len):
	new_string = ''
	for index in range(string_len):
		if string[index] == ' ':
			new_string += "%20"
		else:
			new_string += string[index]
	return new_string


def palindrome_permutation(str1):
	str1 = sorted(str1)
	print(str1)


def one_way(str1, str2):
	str1_len = len(str1)
	str2_len = len(str2)
	replaced = 0
	removed = 0
	inserted = 0
	if str1_len == str2_len: # same length it means replacement or no replacement took place
		for idx in range(str1_len):
			if str1[idx] != str2[idx]:
				replaced += 1
		if replaced > 1:
			return False
	elif str1_len > str2_len: # original string is biggeer it means str2 has removed char(s)
		removed = str1_len - str2_len
		if removed > 1:
			return False
	return True

def string_compression(string):
	len_string = len(string)
	compressed_string = ''

	if len_string == 0:
		return

	current_letter = string[0]
	current_letter_count = 0
	incrementor = 0
	while incrementor < len(string):
		if string[incrementor] == current_letter:
			current_letter_count += 1
		else:
			compressed_string += (current_letter + str(current_letter_count))
			current_letter = string[incrementor]
			current_letter_count = 1
		incrementor += 1

	compressed_string += (current_letter + str(current_letter_count))
	return compressed_string if len(compressed_string) < len_string else string

"""
Input
[
	[0-0, 0-1, 0-2, 0-3]

	[1-0, 1-1, 1-2, 1-3]

	[2-0, 2-1, 2-2, 2-3]

	[3-0, 3-1, 3-2, 3-3]
],
Output
[
	[13, 09, 05, 01],
	[14, 10, 06, 02],
	[15, 11, 07, 03],
	[16, 12, 08, 04]
]
"""

def matrix_print(matrix):
	print(end="\n")
	for ls in matrix:
		print(f"\t{ls}", end="\n")
	print(end="\n")

def rotate_matrix(matrix):
	matrix_len = len(matrix)
	new_matrix = [[0, 0, 0, 0] for i in range(matrix_len)]

	for out in range(matrix_len):
		for inner in range(matrix_len):
			new_matrix[inner][(matrix_len - 1) - out] = matrix[out][inner]

	return new_matrix


matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]
]
print("---- BEFORE ----")
matrix_print(matrix)
print("---- AFTER ----")
matrix_print(rotate_matrix(matrix))
