'''a = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))

if a < b:
	print("A is less than B")

if a > b:
	print("A is greater than B")

if a == b and c > 7:
	print("A is equal B")

else:
	print("gggg")



weather = "cold"

a = 5
b = 3


message = "hello world"
length_of_message = len(message)

print(length_of_message)

if weather == "cold" and a > b and length_of_message > 3:
	print("it works")
	if b > 1:
		print("b is greater than 1 ")
	print("if statment ends there")

print("our code ends")




a = int(input("number 1: "))


if a >= 0:
	if a == 0:
		print("a = 0")
	else:
		print("a > 0")
	
else:
	print("a < 0") '''


temp = int(input("air temperature: "))

if temp <= 10:
	cloth = input("what you wear? ")

	if cloth == "hot jaket":
		print("its ok, have a nice day")
	elif cloth == "jaket":
		print("may be you will freeze lil bit ")
	else:
		print("be carefuul ")
elif temp > 10 and temp < 25:
	print("the weather is warm")
else:
	question = input("Do you know Gagik Surenyan ")

	if question == "yes" or question == "may be":
		print("then ask him what to wear")
	else:
		print("have a good day")





