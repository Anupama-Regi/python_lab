print("*Program to count the occurrences of each word in a line of text*")
s=input("Enter the line of text : ")
s=s.lower()
l1=list(s.split(' '))
print(l1)
l2=list(set(l1))
print(l2)
for i in l2:
	print(i,"occured",l1.count(i))
