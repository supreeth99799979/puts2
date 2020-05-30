import unittest
import main

class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_sub1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/sub?A=7&B=3')
		self.assertEqual(b'4.0', solution.data)

	def test_sub2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/sub?A=3/4&B=1/4')
		self.assertEqual(b'0.5', solution.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/sub?A=9.2&B=1.001')
		self.assertEqual(b'8.199', solution.data)

	def test_sub4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/sub?A=21.222&B=3')
		self.assertEqual(b'18.222', solution.data)

	def test_sub5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/sub?A=11&B=1.112')
		self.assertEqual(b'9.888', solution.data)

	def test_sub6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/sub?A=1/4&B=11')
		self.assertEqual(b'-10.75', solution.data)

	def test_sub7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/sub?A=2&B=3/10')
		self.assertEqual(b'1.7', solution.data)

	def test_sub8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/sub?A=dhoni&B=7')
		self.assertEqual(b'-7.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_sub9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/sub?A=22&B=dhoni')
		self.assertEqual(b'22.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_sub10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('sub?A=3/0&B=5')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_sub11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('sub?A=11&B=7/0')
		self.assertEqual(b"None", solution.data)


if __name__ == '__main__':
	unittest.main()