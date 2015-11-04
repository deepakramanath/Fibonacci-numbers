# Python program to find Fibonacci sequence

"""
Usage: Fibonacci-numbers.py

Generates a Fibonacci sequence up to the given number (n)
At prompt, enter only numbers

Options
-------

-h or help		Displays this message

"""

from sys import argv, exit

def fibonacci(n):
	Fn_1, Fn = 0, 1
	FibonacciSequence = [Fn_1, Fn]
	goldenRatio = [None]
	for i in range(n):
		Fn_1, Fn = Fn, Fn_1+Fn
		FibonacciSequence.append(Fn)
		goldenRatio.append(float(Fn)/Fn_1)
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
	except ValueError:
		print "Error: Enter only numbers"
		continue

FibonacciSequence, goldenRatio = fibonacci(num)

print "Fibonacci Sequence for the value n = %d" % num
print FibonacciSequence
print "\nGolden Ratio\n"
print goldenRatio
