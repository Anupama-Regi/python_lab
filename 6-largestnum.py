print("*** Program to find the largest number among 3 numbers...***")
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if a>b and a>c:
	print(a,"is the largest number.")
elif b>c:
	print(b,"is the largest number.")
else:
	print(c,"is the largest number.")