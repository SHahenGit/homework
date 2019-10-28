str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

letter = input("enter your letter: ")
number_of_shifts = int(input("number of shifts: "))
new_letter = []

for i in range(0, len(letter)):
	if letter[i] == " ":
		new_letter.append(" ")
	for j in range(0, len(str1)):	
		if letter[i] == str1[j]:
			new_letter.append(str1[j - number_of_shifts])

new_letter = ''.join(new_letter)
print(new_letter)



