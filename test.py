
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

	def test_div1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/div?A=10&B=2')
		self.assertEqual(b'5.0', solution.data)

	def test_div2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/div?A=3/4&B=22/4')
		self.assertEqual(b'0.13636363636363635', solution.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/div?A=0.088&B=101.22')
		self.assertEqual(b'0.0008693934005137324', solution.data)

	def test_div4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/div?A=21.222&B=96')
		self.assertEqual(b'0.2210625', solution.data)

	def test_div5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/div?A=9&B=2.1')
		self.assertEqual(b'4.285714285714286', solution.data)

	def test_div6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/div?A=11&B=100')
		self.assertEqual(b'0.11', solution.data)

	def test_div7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/div?A=16&B=2/3')
		self.assertEqual(b'24.0', solution.data)

	def test_div8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/div?A=dhoni&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_div9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/div?A=22&B=dhoni')
		self.assertEqual(b'None', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_div10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('div?A=1/0&B=3')
		self.assertEqual(b'None', solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_div11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('div?A=11&B=2/0')
		self.assertEqual(b'None', solution.data)

	def test_mul1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/mul?A=18&B=2')
		self.assertEqual(b'36.0', solution.data)

	def test_mul2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/mul?A=1/2&B=1/2')
		self.assertEqual(b'0.25', solution.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/mul?A=0.00066&B=100000.00')
		self.assertEqual(b'66.0', solution.data)

	def test_mul4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/mul?A=21.222&B=97')
		self.assertEqual(b'2058.534', solution.data)

	def test_mul5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/mul?A=1000&B=5.36')
		self.assertEqual(b'5360.0', solution.data)

	def test_mul6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/mul?A=10&B=99')
		self.assertEqual(b'990.0', solution.data)

	def test_mul7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/mul?A=23&B=9/13')
		self.assertEqual(b'15.923076923076923', solution.data)

	def test_mul8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/mul?A=dhoni&B=22')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_mul9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/mul?A=22&B=dhoni')
		self.assertEqual(b'0.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_mul10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('mul?A=6/0&B=7')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module

	def test_mul11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('mul?A=11&B=7/0')
		self.assertEqual(b"None", solution.data)

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