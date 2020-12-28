print("*Program to create a list removing even numbers from a list of integers.*")
n=input("Enter the list of integers : ")
l=list(map(int,n.split()))
print("List of numbers : ",l)
#l2=[i for i in l if i%2!=0]
#print(l2)
for i in l:
	if(i%2==0):
		l.remove(i)
print("List after removing even numbers : ",l)