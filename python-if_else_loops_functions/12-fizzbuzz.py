#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 5 == 0 and i % 3 == 0:
	    print("FizzBuzz", sep=" ")
	elif i % 3 == 0:
	    print("Fizz", sep=" ")
	elif i % 5 == 0:
            print("Buzz", sep=" ")
	else:
	    print(i, sep=" ")
