print("Program to find square of n numbers using list comprehension")
l=[]
n=int(input("Enter total number of numbers to be squared : "))
print("Enter the numbers one by one :")
for i in range(1,n+1):
	e=int(input())
	l.append(e)
print("Original list : ",l)
l2=[]
l2=[i*i for i in l]
print("Squared list : ",l2)