import random
import string


user_choice_list ="123456789"
big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]



while True:
	def print_game(list1):
		for i in range(0, len(list1)):
			if (i != 0 and i == 2) or (i != 0 and i == 5) or (i != 0 and i == 8):
				print(list1[i], "\n")
			else:
				print(list1[i], end = " " )

	def comp_choice(list1, list2):
		while True:
			num = random.randint(1,9)			
			for i in range(0, len(list1)):								
				if num == list1[i]:
					print("comp choice is ", list1[i])
					list2 = list2.replace(str(list1[i]), "")
					list1[i] = "O"
					
			break

		return list1, list2

	def user_choice(list1, list2):  #list1 - big list, list2 - user choice list
		num = int(input("enter a number btwn  " + list2 + "  "))
		list1[num -1] = "X"
		list2 = list2.replace(str(num), "")
		return list1, list2


	
	

	

	big_list, user_choice_list = user_choice(big_list, user_choice_list)
	print_game(big_list)


	if ((big_list[0] == big_list[1] == big_list[2] == "X") or
			(big_list[3] == big_list[4] == big_list[5] == "X") or
			(big_list[6] == big_list[7] == big_list[8] == "X") or
			(big_list[0] == big_list[3] == big_list[6] == "X") or
			(big_list[1] == big_list[4] == big_list[7] == "X") or
			(big_list[2] == big_list[5] == big_list[8] == "X") or
			(big_list[0] == big_list[4] == big_list[8] == "X") or
			(big_list[2] == big_list[4] == big_list[6] == "X")):

			print("you WIN")

			break


	big_list, user_choice_list = comp_choice(big_list, user_choice_list)
	print_game(big_list)
	

	if ((big_list[0] == big_list[1] == big_list[2] == "or") or
			(big_list[3] == big_list[4] == big_list[5] == "O") or
			(big_list[6] == big_list[7] == big_list[8] == "O") or
			(big_list[0] == big_list[3] == big_list[6] == "O") or
			(big_list[1] == big_list[4] == big_list[7] == "O") or
			(big_list[2] == big_list[5] == big_list[8] == "O") or
			(big_list[0] == big_list[4] == big_list[8] == "O") or
			(big_list[2] == big_list[4] == big_list[6] == "O")):

		print("you LOSE")

		break




