import unittest

from mul import multiply

class TestSum(unittest.TestCase):
	def test_1(self):
		a_1 = 10
		b_1 = 10
		result = multiply(a_1, b_1)
		self.assertEqual(result, 100)
		
	def test_2(self):
		a_2 = 10
		b_2 = 5
		result = multiply(a_2, b_2)
		self.assertEqual(result, 50)

	def test_3(self):
		a_3 = 5
		b_3 = 5
		result = multiply(a_3, b_3)
		self.assertEqual(result, 25)


if __name__ == '__main__':
	unittest.main()
