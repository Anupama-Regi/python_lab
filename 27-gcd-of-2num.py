print("Program to find gcd...")
n1=int(input("Enter a number : "))
n2=int(input("Enter another number : "))
while n2>0:
	r=n1%n2
	n1=n2
	n2=r
print("GCD is ",n1)
