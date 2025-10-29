from unittest import TestCase
from quiz_functions import suggest_question,suggest_option,check_answer

class TestMyFunctions(TestCase):
	def test_that_suggest_function_work_as_expected(self):
		suggest = ["oyo"]
		actual = suggest_question(suggest)
		expected = "oyo"
		self.assertEqual(actual,expected)

	def test_that_suggest_function_work_as_suggest_one_(self):
		suggest = ["oyo"]
		actual = suggest_question(suggest)
		expected = "oyo"
		self.assertEqual(actual,expected)

	def test_that_suggest_option_work_as_expected(self):
		option = ["oyo"]
		actual =  suggest_option(option)
		expected = 0
		self.assertEqual(actual,expected)

	def test_that_suggest_option_work_suggest_index(self):
		option = ["oyo"]
		actual =  suggest_option(option)
		expected = 0 
		self.assertEqual(actual,expected)

	def test_that_check_answer_function_work_as_expected(self):
		first = ["oyo"]
		second = ["ibadan"]
		answer = 0     
		state = "oyo" 
		actual = check_answer(first, second, answer, state)
		expected = "Correct"
		self.assertEqual(actual, expected)

	def test_that_check_answer_function_raises_error(self):
		self.assertRaises(TypeError,check_answer, ["oyo"],["ibadan"], "o", "oyo")

	def test_that_check_answer_function_raises_error_if_user_input_is_out_of_range(self):
		self.assertRaises(ValueError,check_answer, ["oyo"],["ibadan"], 2, "oyo")






	
