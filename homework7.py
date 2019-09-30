
#exercise 1
# any_number = int(input("type any number: "))

# for i in range(1, 11):
# 	print(any_number, "*", i, "=", any_number * i)

#exercise 2

# number = input("type a number: ")
# dig_in_a_number = 0

# for i in number:
# 	dig_in_a_number += 1

# print(dig_in_a_number)


#exercise 3

# max_num = int(input("type a number: "))
# sign = ""

# for i in range (1, max_num + 1):
# 	sign = i * "*"
# 	print(sign)
# for i in range (max_num -1, 0, -1):
# 	sign = i * "*"
# 	print(sign)


# max_num = int(input("type a number: "))
# sign = ""

# for i in range (max_num, - max_num - 1, -1):
# 	if i == 0:
# 		continue

# 	sign = abs(i) * "*"
# 	print(sign)



max_num = int(input("type a number: "))


for i in range (max_num, - max_num - 1, -max_num):
	 for j in range(i, -1, -1):
	 	h = i - j
	 	print(abs(h) * "*")
		

		