# 1. Write a Python program to remove duplicate values from Dictionary.

dict1 = {"1":True, "2":False, "3":True, "4":False, "5":True}

dict2 = {}



for key, value in dict1.items():
    if not value in dict2.values():
     dict2[key] = value

print(dict2)

        
#1 version 2. Write a Python program to remove duplicate values from Dictionary.


cinema_seats = {"1":True, "2":False, "3":True, "4":False, "5":True}

free_seats = {}
free_seats_key = []
free_seats_val = []

for key, value in cinema_seats.items():        
    if cinema_seats[key] == False:        
        free_seats_key.append(key)
        free_seats_val.append(value)

for key in free_seats_key:
    for value in free_seats_val:
        free_seats[key] = value
        break
print(free_seats)


# 2. Write a Python program to find the highest 3 values in a dictionary

dict1 = {"first":5, "second":89,"third":4, "forth":66, "fifth":2, "sixth": 7}


dict1_list = []

for value in dict1.values():
    dict1_list.append(value)

dict1_list.sort()

print(dict1_list[-3:])




# 3. Write a Python program to create a dictionary from a string.


str1 = "a5d4l8f3y6"
print(str1)

dict1 = {}

for i in range(0, len(str1), 2):
     dict1[str1[i]] = str1[i+1]        

print(dict1)



# 3 version 2. Write a Python program to create a dictionary from a string.

str1 = "asdasdasdasd"
dict1 = {}
print(str1)

for i in str1:
    if i in dict1.keys():
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)




