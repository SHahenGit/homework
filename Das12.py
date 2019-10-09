# tuple

# a = (1, 2)

# print(a)

# print(a[0], a[1])

# def tuple1():
# 	user_name = input("enter your name: ")
# 	user_surname = input("enter your surname: ")
# 	return user_name, user_surname

# user_info = tuple1()
# print("Your name is " + user_info[0])
# print("Your surname is " + user_info[1])


# nested_tuple = ((1, 2), (3, 4), (5, 6))

# print(nested_tuple[0])
# print(nested_tuple[0][0])


# List

my_list = [1,0,2,3,4,5,6,7,8,9,10,]

my_list.remove(10)
print(my_list, ": After removing 10")

my_list.sort()
print(my_list, ": After sorting")

my_list.reverse()
print(my_list, ": After reversing")


a = my_list.pop()
print(my_list, ": poping")
print(a)


del my_list[-5:]
print(my_list, ": After deleting the last five items")

