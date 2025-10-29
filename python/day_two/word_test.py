from unittest import TestCase
from word import backward

class TestmyFunction(TestCase):
	def test_that_backward_function_work_as_expected(self):
		word = "abcdefd"
		check = "d"
		actual = backward(word, check)
		expected = "dcbadefd"
		self.assertEqual(actual ,expected )
		
