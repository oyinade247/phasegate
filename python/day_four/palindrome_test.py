from unittest import TestCase
from palindrome import*

class TestMyFunction(TestCase):
	def test_that_palindrome_works_as_expected(self):
		palin = ["level"]
		actual =  isPalindrome(palin)
		expected = [True]
		self.assertEqual(actual, expected)

