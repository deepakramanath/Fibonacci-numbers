# Python program to find Fibonacci sequence

"""
Usage: Fibonacci-numbers.py

Generates a Fibonacci sequence up to the given number (n) and
calculates the Golden Ratio

At prompt, enter only numbers

Options
-------

-h or help		Displays this message

"""

from sys import argv, exit

def fibonacci(n):
	(Fn_1, Fn) = 0, 1
	FibonacciSequence = [Fn_1, Fn]
	goldenRatio = []
	for i in range(n-1):
		(Fn_1, Fn) = Fn, (Fn_1 + Fn)
		FibonacciSequence.append(Fn)
		goldenRatio.append(Fn/float(Fn_1))
	return FibonacciSequence, goldenRatio

if len(argv) > 1:
	print(__doc__)
	exit(0)

while True:
	number = raw_input("Enter the number, n to obtain the Fibonacci Sequence: ")
	try:
		num = int(number)
		if num > 100:
			print "Enter a value less or equal to 100"
			continue
		print "The number you have entered is: %d" % num
		break
	except:
		print "Error: Enter only numbers"
		continue

FibonacciSequence, goldenRatio = fibonacci(num)

print "\nFibonacci Sequence for the value, n = %d\n" % (num)
print FibonacciSequence
print "\nGolden Ratio\n"
print goldenRatio
