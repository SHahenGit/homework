# objects

# class Person:
# 	def __init__(self):
# 		self.first_name = "[no first name]"
# 		self.last_name = "[no last name]"
# 		self.eye_color = "[no eye color]"


# my_person = Person()

# print(my_person.first_name)
# print(my_person.last_name)
# print(my_person.eye_color)

# Encapsulation

# Constructor

# class Person:
# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.eye_color = "[no eye color]"

# my_person = Person("Jirayr", "Melikyan")

# print(my_person.first_name)
# print(my_person.last_name)
# print(my_person.eye_color)

#example

class BankAccount:
	def __init__(self, name, balance = 0.0):
		self.log("Account created")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("Balance checked at " + str(self.balance))
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		self.log("+" + str(amount) + ": " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ": " + str(self.balance))

	def log(self, message):
		print(message)


my_bank_account = BankAccount("Shahen Mehrabyan")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()



# Destructor
# Getters
# Setters




