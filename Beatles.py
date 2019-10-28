lyrics = { 1: "Oh yeah, I'll tell you somethin'",
				2:"I think you'll understand",
				3:"When I say that somethin'",
				4:"I want to hold your hand",
				5:"I want to hold your hand",
				6:"I want to hold your hand",
				7:"Oh please, say to me",
				8:"You'll let me be your man",
				9:"And please, say to me",
				10:"You'll let me hold your hand",
				11:"Now, let me hold your hand",
				12:"I want to hold your hand",
				13:"And when I touch you",
				14:"I feel happy inside",
				15:"It's such a feelin' that my love",
				16:"I can't hide",
				17:"I can't hide",
				18:"I can't hide",
				19:"Yeah, you got that somethin'",
				20:"I think you'll understand",
				21:"When I say that somethin'",
				22:"I want to hold your hand",
				23:"I want to hold your hand",
				24:"I want to hold your hand",
				25:"And when I touch you",
				26:"I feel happy inside",
				27:"It's such a feelin' that my love",
				28:"I can't hide",
				29:"I can't hide",
				30:"I can't hide",
				31:"Yeah, you got that somethin'",
				32:"I think you'll understand",
				33:"When I feel that somethin'",
				34:"I want to hold your hand",
				35:"I want to hold your hand",
				36:"I want to hold your hand",
				37:"I want to hold your hand",
	
}




while True:	
	try:
		num = input("enter a number btwn 1 to 37: ")
		num = int(num) 

		if num <= 37 and num >= 1:
			print(lyrics[num])

		else:
			raise IndexError


	except IndexError:
		print("please enter a number btwn 1 - 37")
		
	except ValueError:
		print("please enter a number")




