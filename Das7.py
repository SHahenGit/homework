
#for i in range(0,10):
#		print("hello", i)



'''for i in range(10, 1, -1):
	print("hello", i)


print("")


for i in range(0, 10, 2):
	print("hello", i)


sum = 0
a = 0

for i in range(1, 10, 2):
	next_number = int(input("enter number " + str(i) + ": "))
	sum += next_number
	a += 1

print(sum/a)


some_string = "hello world"

for i in some_string:
	print(i)



i = 7

while  i <= 10:
	print(i)
	i += 1 '''

import random

hidden_number = random.randint(1,100)

user_guess = 0

while not user_guess == hidden_number:

	user_guess = int(input("guess a number: "))

	if user_guess > hidden_number:
		print("too high")
	elif user_guess < hidden_number:
		print("too low")
	else:
		print("thats right")





