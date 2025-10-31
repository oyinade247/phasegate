from unittest import TestCase
from parking_function import*

class TestMyFunctions(TestCase):
	def test_that_park_car_work_as_expected(self):
		list = [0, 0, 0]
		actual = park_car(list)
		expected = 1
		self.assertEqual(actual,expected)

	def test_that_remove_car_work_as_expected(self):
		list = [1,0,0]
		remove = 1
		actual = remove_car(list,remove)
		expected = "removed"
		self.assertEqual(actual,expected)
	
	def test_that_remove_car_raise_error_if_type_is_not_int(self):
		self.assertRaises(TypeError, remove_car,[1,0,0], "one")

	def test_that_remove_car_raise_error_if_space_does_not_exist(self):
		self.assertRaises(ValueError, remove_car, [1,0,0], 5)

		
		