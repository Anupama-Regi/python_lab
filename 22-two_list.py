print("Program to enter 2 lists of integers \n-a)whether list are of same length \n-b)whether list sums to same value \n-c)whether any value occur in both")
n=input("Enter first list of integers : ")
m=input("Enter second list of integers : ")
a=list(map(int,n.split()))
b=list(map(int,m.split()))
if len(a)==len(b):
	print("Yes,Lists are of same length..")
else:
	print("No,Lists are not of same length..")
s1=0
s2=0
for i in a:
	s1=s1+i
print("list1 sum is ",s1)
for i in b:
	s2=s2+i
print("list2 sum is ",s2)
if s1==s2:
	print("Yes,Sum of list1 and list2 are same..")
else:
	print("No,Sum of list1 and list2 are not same..")
l=[i for i in a if i in b]
print("List of elements occured in both lists are : ",l)	