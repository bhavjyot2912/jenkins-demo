import unittest

from mul import multiply

class TestSum(unittest.TestCase):
	def test_4(self):
		a_4 = 2
		b_4 = 5
		result = multiply(a_4, b_4)
		self.assertEqual(result, 20) 

	def test_5(self):
		a_5 = 5
		b_5 = 4
		result = multiply(a_5, b_5)
		self.assertEqual(result, 25)

if __name__ == '__main__':
	unittest.main()
