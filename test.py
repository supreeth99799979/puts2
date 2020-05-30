import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_add1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/add?A=10&B=4')
		self.assertEqual(b'14.0', solution.data)

	def test_add2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/add?A=3/4&B=5/4')
		self.assertEqual(b'2.0', solution.data)

	def test_add3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/add?A=103.22&B=1.006')
		self.assertEqual(b'104.226', solution.data)

	def test_add4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/add?A=16.222&B=96')
		self.assertEqual(b'112.222', solution.data)

	def test_add5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/add?A=102&B=96.7')
		self.assertEqual(b'198.7', solution.data)

	def test_add6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/add?A=1/4&B=88')
		self.assertEqual(b'88.25', solution.data)

	def test_add7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/add?A=18&B=6/10')
		self.assertEqual(b'18.6', solution.data)

	def test_add8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/add?A=mahendrasingh&B=7')
		self.assertEqual(b'7.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_add9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/add?A=7&B=dhoni')
		self.assertEqual(b'7.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_add10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('add?A=6/0&B=3')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module 

	def test_add11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('add?A=11&B=3/0')
		self.assertEqual(b"None", solution.data)


if __name__ == '__main__':
	unittest.main()
