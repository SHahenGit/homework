# # versin 1


# import random
# import string


# def randomString(stringLeght = 10):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLeght))


# rand_string = randomString(3)
# print(rand_string)


# def guess_letters():
#     guess = False

#     len_of_random_string = len(rand_string)

#     guessed_letters_amount = 0

#     while guess == False:
#         if guessed_letters_amount != len_of_random_string:
#             letter = input("enter a letter:: ")

#             while not (letter.isalpha() and len(letter) == 1):
#                 print("you have entered wrong character")

#                 letter = input("enter a letter: ")

#             for i in rand_string:            
#                 if letter == i:
#                     guessed_letters_amount += 1

#                     print("Letter was found")
            
#         else:
#             guess = True
#             print("You found a word", rand_string)


# guess_letters()





# version 2


import random
import string


def randomString(stringLeght = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLeght))


rand_string = randomString(5)
print(rand_string)


def guess_letters():
    guess = False

    len_of_random_string = len(rand_string)

    guessed_letters_amount = 0

    secret_word = []

    for i in range(len_of_random_string):
    	secret_word.append("#")
    print(secret_word)
    

    while guess == False:
        if guessed_letters_amount != len_of_random_string:
            letter = input("enter a letter:: ")

            while not (letter.isalpha() and len(letter) == 1):
                print("you have entered wrong character")

                letter = input("enter a letter: ")

            for i in rand_string:            
                if letter == i:
                    guessed_letters_amount += 1
                    letter_position = rand_string.index(i)
                    secret_word[letter_position] = i
                    print(secret_word)
            
        else:
            guess = True
            print("You found a word", rand_string)


guess_letters()