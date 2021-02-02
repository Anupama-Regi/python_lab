print("Program to find sum of all items in a list using functions")
def sum(l1):
	sum=0
	for i in l1:
		sum=sum+i
	#print("Sum of all items is ",sum)
	return sum
list1=input("Enter the items in a list : ")
l1=list(map(int,list1.split()))
print("List items are : ",l1)
#sum(l1)
print("Sum of all items is ",sum(l1))
