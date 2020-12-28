print("Program to find gcd of 2 numbers.")
n=int(input("Enter 1st number : "))
m=int(input("Enter 2nd number :"))
while(n!=m):
	if(n>m):
		n=n-m
	else:
		m=m-n
print(n)