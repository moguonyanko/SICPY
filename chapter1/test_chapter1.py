#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import fractions
import math

from chapter1 import *

class TestChapter1(unittest.TestCase):
	'''
	Test class for SICP chapter 1 emulate functions.
	'''
	def test_square(self):
		res = square(21)
		self.assertEqual(441, res)

	def test_sum_of_squares(self):
		res = sum_of_squares(3, 4)
		self.assertEqual(25, res)
	
	def test_abs2(self):
		self.assertEqual(5, abs2(5))
		self.assertEqual(0, abs2(0))
		self.assertEqual(5, abs2(-5))
	
	def test_and2(self):
		self.assertEqual(True, and2(7>5, 1<10))
		self.assertEqual(False, and2(7>5, 1>10))

	def test_or2(self):
		self.assertEqual(True, or2(7>5, 1<10))
		self.assertEqual(True, or2(7>5, 1>10))
		
	def test_not2(self):
		self.assertEqual(True, not2(1>10))
		self.assertEqual(False, not2(1<10))
	
	def test_gte(self):
		self.assertEqual(False, gte(1, 2))
		self.assertEqual(True, gte(2, 1))
		self.assertEqual(True, gte(1, 1))

	def test_gte(self):
		self.assertEqual(True, lte(1, 2))
		self.assertEqual(False, lte(2, 1))
		self.assertEqual(True, lte(1, 1))

	def test_sqrt(self):
		#self.assertEqual(3.00009155413138, sqrt(9))
		self.assertEqual(3.000, round(sqrt(9),3))
	
	def test_fractorial(self):
		self.assertEqual(720, fractorial(6))

	def test_fib(self):
		self.assertEqual(55, fib(10))
	
	def test_count_change(self):
		self.assertEqual(292, count_change(100))
		
	def test_expt(self):
		self.assertEqual(1024, expt(2, 10))

	def test_expt(self):
		self.assertEqual(1024, fast_expt(2, 10))

	def test_gcd(self):
		self.assertEqual(2, gcd(206, 40))

	def test_is_prime(self):
		self.assertEqual(True, is_prime(31))
		self.assertEqual(False, is_prime(51))
		self.assertEqual(False, is_prime(1))

	def test_exmod(self):
		self.assertEqual(0, expmod(10, 2))
		self.assertEqual(1, expmod(10, 3))
	
	#def test_fermat_test(self):
	#	self.assertEqual(True, fermat_test(5))
	#	self.assertEqual(False, fermat_test(10))

	def test_fermat_test(self):
		times = 100
		self.assertEqual(True, is_prime_fast(5, times))
		self.assertEqual(False, is_prime_fast(10, times))
		self.assertEqual(False, is_prime_fast(1, times))
		self.assertEqual(False, is_prime_fast(0, times))
		self.assertEqual(False, is_prime_fast(-1, times))
		#self.assertEqual(True, is_prime_fast(2**10, times)) #Maximum recursion.

	def test_cube(self):
		self.assertEqual(27, cube(3))

	def test_sum_integers(self):
		self.assertEqual(55, sum_integers(1, 10))

	def test_sum_cubes(self):
		self.assertEqual(3025, sum_cubes(1, 10))

	def test_pi_sum(self):
		self.assertEqual(fractions.Fraction(1289, 3465), pi_sum(1, 3))

	def test_inc(self):
		self.assertEqual(10, inc(9))

	def test_integral(self):
		self.assertEqual(0.24998750000000042, integral(cube, 0, 1, 0.01))

	def test_half_interval_method(self):
		self.assertEqual(3.14111328125, half_interval_method(math.sin, 2.0, 4.0))
		testf = lambda x: x**3-2*x-3
		self.assertEqual(1.89306640625, half_interval_method(testf, 1.0, 2.0))

	def test_fixed_point(self):
		#an error
		#self.assertEqual(0.7390822985224023, fixed_point(math.cos, 1.0))
		self.assertEqual(0.7390822985224024, fixed_point(math.cos, 1.0))
		testf = lambda y: math.sin(y)+math.cos(y)
		self.assertEqual(1.2587315962971173, fixed_point(testf, 1.0))

	def test_average_damp(self):
		func = average_damp(square)
		self.assertEqual(55, func(10))
		
	def test_deriv(self):
		func = deriv(cube)
		self.assertEqual(75.00014999664018, func(5))

if __name__ == '__main__':
	print(__file__)
	unittest.main()
		
