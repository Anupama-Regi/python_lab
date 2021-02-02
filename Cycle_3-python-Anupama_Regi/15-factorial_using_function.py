print("Program to find factorial using function")
def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	print("Factorial is ",f)
n=int(input("Enter the number to find factorial : "))
factorial(n)
	
