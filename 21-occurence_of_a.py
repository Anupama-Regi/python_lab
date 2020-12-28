print("*Program that store a list of first names.Count the occurences of 'a' within the list.*")
s=input("Enter list of names : ")
l=list(s.split())
print("List of names : ",l)
c=0
#for i in range(s):
#	n=input("Enter the name : ")
#	l.append(n)
for i in l:
	for j in i:
		if j in "Aa":
			c=c+1
print("Occurrences of 'a' in list : ",c)
#x=s.count('a')
#print(x)