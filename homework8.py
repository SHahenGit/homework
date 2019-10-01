# exercise 1

def find_max_number(num1, num2, num3):

	if num1 >= num2:
		num = num1		
	else:
		num = num2

	if num >= num3:
		return num
	else:
		return num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

print(find_max_number(num1, num2, num3))

# exercise 2


def fizz_buzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"

	elif num % 3 == 0:
		return "Fizz"

	elif num % 5 == 0:
		return "Buzz"	

	else:
		return num


num = int(input("Enter a number: "))

print(fizz_buzz(num))

# exercise 3

def showNumbers(lim):
	for i in range (0, lim + 1):
		
		if i % 2 == 0:
			print(i, "Even")
		else:
			print(i, "Odd")


lim = int(input("Enter a number: "))

print(showNumbers(lim))
