print("Program to find pattern: \n1 \n2 4 \n3 6 9 \n4 8 12 16 using functions")
def pattern(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(i*j,end=" ")
		print(" ")
i=int(input("Enter a number : "))
pattern(i)