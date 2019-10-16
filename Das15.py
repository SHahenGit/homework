# # Dictionaries

# human = {"name": "jirayr", "surname":"melikyan", "age": 19}
# print(human)
# print(human["name"], human["age"], human["surname"])



# human["age"] = 30
# print(human)

# #dictionary um avelacnel
# human["have_pet"] = False
# print(human)

# # dict ic jnjel
# del human["age"]
# print(human)

# print (len(human))


# #veradardznuma list type i
# print(human.keys())
# print(human.values())

# for values in human.values():
# 	print(values)


#xndir 1

# fruits = {"apple": 5, "orange": 14, "pineapple": 1, "bananas":4, "pomegranate": 8}

# for key in fruits.keys():
# 	if fruits[key] > 5:
# 		print(key)
# for (name, kg) in fruits.items():
# 	print(name, "is", kg, "In store")




# xndir 2

# xumb = {"Gor":26, "Davit":26, "Vardges":26, "Rafayel":28, "Khachatur":23}

# print(xumb)

# xumb["Gor"] = 3
# xumb["Rafayel"] = 30

# print(xumb)

#xndir 3

# classes = {"Math":["Davit", "Lucy", "Dana"],
# 		"Physics":["Addison", "Benjamin"],
# 		"Chemistry": ["Sara", "Pele"]}

# print("students in math class", classes["Math"])
# classes["Math"].append("Jirayr")
# print("students in math class", classes["Math"])


#xndir 4

# phonebook = {"Shahen":{"age": 25, "phone number": 555555}, 
# 			"Rafayel":{"age":35, "phone number": 666666 }}

# print(phonebook)
# print(phonebook["Rafayel"]["age"], phonebook["Shahen"]["phone number"])
# print(phonebook.values())





# hashvenq textum vor baric inchqan ka

sample_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industrys standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book It has survived not only five centuries but also the leap into electronic typesetting remaining essentially unchanged It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

words_dict = {}



sample_text = sample_text.replace(",", "")
sample_text = sample_text.replace(".", "")
sample_text = sample_text.lower()
sample_text = sample_text.split(" ")



for word in sample_text:
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict[word] = 1

for(word, amount) in words_dict.items():
	if amount > 2:
		print(word, ":", amount)


