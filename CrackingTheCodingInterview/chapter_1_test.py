#!/usr/bin/env python3
import unittest
from chapter_1 import is_unique, check_permutation, urlify, palindrome_permutation

class TestChapterOne(unittest.TestCase):
	def test_is_unique_test(self):
		self.assertFalse(is_unique("44"))
		self.assertFalse(is_unique("122"))
		self.assertTrue(is_unique("132"))

	def test_check_permutation(self):
		self.assertFalse(check_permutation("iamnot", "yesiam"))
		self.assertFalse(check_permutation("iamnot", "IAMNOT"))
		self.assertTrue(check_permutation("iamnot", "iamnot"))

	def test_urlify(self):
		data = [
        ('much ado about nothing      ', 22, 'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

		for [test_string, length, expected] in data:
			actual = urlify(test_string, length)
			self.assertEqual(actual, expected)

	# @unittest.skip("Function not developed yet")
	def test_palindrome_permutation(self):
		data = [
		('Tact Coa', True),
		('jhsabckuj ahjsbckj', True),
		('Able was I ere I saw Elba', True),
		('So patient a nurse to nurse a patient so', False),
		('Random Words', False),
		('Not a Palindrome', False),
		('no x in nixon', True),
		('azAZ', True)]

		for [test_string, expected] in data:
			actual = palindrome_permutation(test_string)
			print(palindrome_permutation(test_string))
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()
