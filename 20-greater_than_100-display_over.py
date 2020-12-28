print("Program that prompts the user for a list of integers.For all values greater than 100,store 'over' instead.")
l=input("Enter a list of integers : ")
l=list(map(int,l.split()))
l1=[]
for i in l:
	if(i>100):
		l1.append("over")
	else:
		l1.append(i)
print(l1)