# def add_two_numbers (num1, num2):
#  	return num1 + num2


# first_number = int(input("enter first number: "))
# second_number = int(input("enter second number: "))

# print(add_two_numbers(first_number,second_number) == add_two_numbers(first_number,second_number))

# print(add_two_numbers(add_two_numbers(first_number,second_number), second_number))



# def print_hello_world():
# 	print("hello world")

# print_hello_world()


# def big_or_small(num1, num2):
# 	if num1 > num2:
# 		return "number 1 > number 2"
# 	elif num1 < num2:
# 		return "number1 < number2"
# 	else:
# 		return "number1 = number2"

# number_1 = int(input("type number 1: "))
# number_2 = int(input("type number 2: "))

# print(big_or_small(number_1, number_2))



def even_or_odd(number):
	if number % 2 == 0:
		return "Even"
	return "odd"

print(even_or_odd(int(input("number: "))))