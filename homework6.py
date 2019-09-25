# exercise 1

text = input("write a text: ")

if " " in text:
	print("its a sentence")
else:
	print("its a word")


	

# exercise 2

number = int(input("write a number: "))

if number % 5 == 0 and number % 11 == 0:	
	print("yes")
else:
	print("no")



# exercise 3

year = int(input("tell the year and i will say its leap or not: "))

spec_year = (year / 100) 
if spec_year == int(spec_year) and (year - 2000) % 400 == 0:		
		print("yes")
elif spec_year != int(spec_year) and year % 4 == 0:
			print("yess")
else:
	print("no")
