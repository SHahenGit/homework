dict1 = {"key1": 1, "key2": 5, "key3": 2}
dict2 = {"key1": 1, "key2": 5}


for key1  in dict1.keys():
	for key2  in dict2.keys():
		if key1 == key2:
			print(key1, ":", dict2[key1], " present in both dicts")
			


