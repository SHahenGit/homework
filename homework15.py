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
