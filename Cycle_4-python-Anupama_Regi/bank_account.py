class bank:
	def __init__(self,n,acno,t,a):
		self.name=n
		self.ac=acno
		self.type=t
		self.amount=a
	def display(self):
		print("\nDETAILS :\n\nName : ",self.name,"\nAccount no. : ",self.ac,"\nAccount type : ",self.type,"\nAmount : ",self.amount)
	def deposit(self,am):
		self.am=am
		print("Total amount : ",self.amount)
		print("Deposited amount : ",self.am)
		self.amount=self.amount+self.am
		print("Current balance amount : ",self.amount)
	def withdraw(self,w):
		self.w=w
		if self.w>self.amount:
			print("Not having enough balance...\nYour balance amount is",self.amount)
		else:
			self.amount=self.amount-w
			print("Balance amount : ",self.amount)
n=input("Enter the name : ")
m=int(input("Enter the account number : "))
o=input("Enter type of the account : ")
p=int(input("Enter the amount : "))
n=bank(n,m,o,p)
c=0
print("\nChoices are : \n1.Bank Details\n2.Deposit\n3.Withdraw Amount\n4.Exit")
while(c!=4):
	c=int(input("\n\nEnter a choice : "))
	if c==1:
		n.display()
	elif c==2:
		am=int(input("Enter the amount to be deposited : "))
		n.deposit(am)
	elif c==3:
		w=int(input("Enter the amount to be withdrawed : "))
		n.withdraw(w)
	elif c==4:
		break;
	else:
		print("Invalid choice...")