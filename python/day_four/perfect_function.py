from unittest import TestCase
from perfect_square import*

class TestMyFunction(TestCase):
	def test_that_perfect_works_as_expected(self):
		palin = [4]
		actual = is_perfect_square(palin)
		expected = [True]
		self.assertEqual(actual, expected)

