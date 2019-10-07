# try:
# 	1 / 0
# except:
# 	print("you cant divide by zero")


# try:
# 	print ("good")
# except:
# 	print("sintax error")


my_string = "this string is not a number!"

try:
	print("converting my string to int...")
	1/0
	print("string #" + 1 +  ": " + my_string)
	my_int = int(my_string)
	print(my_int)
except ValueError:
	print("can't convert; my_string to a number")

except TypeError:
	print("can't concatinate number with string")


except:
	print("Unknown error")

else:
	print("no errors occured")


print("Done!")


