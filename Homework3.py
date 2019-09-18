import datetime


name = input("Hello, What's your name? ")
print("Nice to meet You ", name)
print("Lets play a Game")

age = input("How old are You? ")
present_year = datetime.datetime.today().year


birth_year = present_year - int(age)

print("You born in ", birth_year , "or in", birth_year - 1, )

answer = input("do you like the game? yes or no ")

if answer == "yes":
	print(":)) bye bye")
else answer == "no":
	print(":(( bye bye")
