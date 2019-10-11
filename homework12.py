# exercise 1
list1 = []
for i in range(0,3):
	string = input("Enter a string: ")	
	list1.append(string)

print(list1)
count = 0

for i in list1:
	if len(i) >= 2 and i[0] == i[len(i) - 1]:
		count += 1

print(count)
		


# exercise 2

list1 = []
list2 = [5,5,5,5,5,5]


def list_is_empty(list1):
	if len(list1) != 0:
		return "is not empty"
	else:
		return "empty"

print(list_is_empty(list1))
print(list_is_empty(list2))


# exercise 3

list1 = []
for i in range(0,3):
	string = input("Enter a string: ")	
	list1.append(string)

print(list1)

def longest_word(listN):

	big = ""

	for i in listN:
		if len(i) > len(big):
			big = i

	return big

print(longest_word(list1))


# exercise 4

list1 = ["a",2,3,4,5]
list2 = [5,6,"a",8,3]

count = 0

for i in list1:
	for j in list2:
		if j == i:
			count += 1

print(count)