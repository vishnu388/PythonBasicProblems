"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'Power of 2 '
"""

class Powerof2:
	def power(self):
		print("Enter the N value :")
		N = int(input())
		num=0
		# as per the given condition the resultant should be less than 2^31
		if 0<= N and N<31:
			if N==0:
				print("2 * ", N, " = ", num)
			for i in range(1, N):
				num = pow(2, i)
				if num <=(pow(2, N)):
					# Printing the table of two powers
					print("2 pow ", i, " = ", num)
		else:
			print("Given number should be less than 31")
powr = Powerof2()
powr.power()