#exercise 1

def kilotomiles(number):
	number = number*0.62

	print(number, "miles")

number = int(input("Input kilometers: "))

kilotomiles(number)



#exercise 2

def celtofar(temp):
	temp = temp*1.8+32
	return temp
temp = int(input("Input temperature in celsius: "))
print((celtofar(temp)), "fahrenheit")




#exercise 3





#exercise 4

def wordcounter(sent):
	count = 0

	j = sent[0]



	for i in sent[1:len(sent)]:
		
		if i != " " and j == " ":
			print(i, "start")
		if i == " " and j != " ":
			print(i, "end")

			count += 1
		j = i


	if sent.endswith(" ") == False:
		return count + 1

	else:
		return count



sent = input("write a sentence: ")
start = wordcounter(sent)
print(start)


#exercise5

def symbol_checker(sent):
	print(sent.isalpha())

sent = input("type a string: ")
symbol_checker(sent)


