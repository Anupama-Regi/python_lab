print("*Program to generate a +ve list of numbers from a given list of integers using list comprehension*")
l=[]
n=int(input("Enter the total number of elements : "))
print("Enter the elements one by one: ")
for i in range (1,n+1):
	e=int(input())
	l.append(e)
print("Original list is : ",l)
l2=[]
l2=[i for i in l if i>0]
print("Positive numbers are : ",l2)