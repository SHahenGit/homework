
#exercise 1

sent = input("Write a  sentence: ")

first_char = sent[0]

sent2 = sent.replace(first_char, "$")
sent2 = sent2.replace("$", first_char, 1)

print(sent)
print(sent2)


#exercise 2


def add_ing_or_ly(sent):
	if len(sent) >= 3:
		if sent[-3:len(sent)] != "ing":
			return sent + "ing"
		else:
			return sent + "ly"
	else:
		return sent


sent = input("Write a String: ")
print(add_ing_or_ly(sent))


#exercise 3

sent = input("Write a sentence: ")

not_dest = sent.find("not")
poor_dest = sent.find("poor")

if not_dest < poor_dest:
	change = sent[not_dest:poor_dest + 4]
	sent2 = sent.replace(change, "good")
	print(sent2)
else:	
	print(sent)




