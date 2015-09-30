#this is some phython testing

#print("hello world")
a = [1, 2, 3, 4, 5, 15]

def say(msg):
	print(msg)

'''
Programming background in Python.

The first exercise allows you to assess your ability to program in Python.
As a data analyst, you will spend much of your time writing code and
programs to work with data or to build mathematical, statistical, or
machine learning models to find insights from data.

Complete this function that transforms a list of integers.

1)  For numbers that are multiples of three replace the integer with the string "Fizz".

2)  For numbers that are multiples of five replace the integer with the string "Buzz".

3)  For numbers that are multiples of both three AND five replace the integer
    with the string "FizzBuzz"

Your function should take in a list of integers as input.
Your function should not modify the input list.
Your function should return an updated list with integers and strings.
'''

def fizzbuzz(intList):
    '''
    Your fizzbuzz function. The grader will run `fizzbuzz(intList)` to check if your
    function returns the correct output.
    
    intList: list containing integers

    Make sure you write the script so that your algorithm is part of the
    function; you do not need to call the function yourself.
    '''

    # YOUR CODE HERE
    b = []
    #print(intList)

    for item in intList:
		#print(item)

		newItem = item

		if item % 3 == 0:
			pass
			#print("-mod 3 test passed")
			newItem = "Fizz"
		if item % 5 == 0:
			pass
			#print("-mod 5 test passed")
			newItem = "Buzz"	
		if item % 5 == 0 and item % 3 == 0:
			pass
			#print("-mod 3&5 test passed")
			newItem = "FizzBuzz"

		b.append(newItem)

    return b

print(fizzbuzz(a))

