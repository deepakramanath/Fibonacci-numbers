# Python program to find Fibonacci sequence

"""
Usage: Fibonacci-numbers.py

Generates a Fibonacci sequence up to the given number (n)
At prompt, enter only numbers

Options
-------

-h or help		Displays this message

"""

import sys

arg = sys.argv

def fibonacci(n, Fn, Fn_1, count):
	while True:
		count = count + 1
		Fn = Fn + Fn_1
		Fn_1 = Fn - Fn_1
		gR = Fn/float(Fn_1)
		FibonacciSequence.append(int(Fn))
		goldenRatio.append(gR)
		if count == n:
			break

while len(arg) > 1:
	print(__doc__)
	sys.exit(0)

while True:
	number = raw_input("Enter the number, n to obtain the Fibonacci Sequence: ")
	try:
		num = int(number)
		if num > 100:
			print "Enter a value less or equal to 100"
			continue
		print "Your entered number is: %d\n" % (num)
		break
	except:
		print "Error:Enter only numbers"
		continue

FibonacciSequence = [1]
goldenRatio = []

iniFn = 1
iniFn_1 = 1
count = 2

fibonacci(num, iniFn, iniFn_1, count)


print "Fibonacci Sequence for the value n = %d\n" %(num)
print FibonacciSequence
print "\nGolden Ratio\n"
print goldenRatio
