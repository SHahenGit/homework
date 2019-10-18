class BankAccount:
	def __init__(self, name, balance = 0.0):
		self.log("Account created")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("You Balance is " + str(self.balance))
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		self.log("+" + str(amount) + ": " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ": " + str(self.balance))

	def log(self, message):	
		file = open("log_file.txt","a") 		
		file.write(message + "\n")		 
		file.close()



file = open("log_file.txt","w")  
file.truncate(0)				 
file.close()
my_bank_account = BankAccount("Shahen Mehrabyan")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()



 