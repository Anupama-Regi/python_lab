print("Program to merge two dictionaries.")
n=int(input("Enter number of items in dictionary-1 : "))
d1={}
for i in range(n):
	keys=input("Enter key : ")
	values=input("Enter values : ")
	d1[keys]=values
print("Dictionary-1 : ",d1)
m=int(input("Enter number of items in dictionary-2 : "))
d2={}
for i in range(m):
	keys1=input("Enter key : ")
	values1=input("Enter values : ")
	d2[keys1]=values1
print("Dictionary-2 : ",d2)
d3={}
for i in d1:
	if i in d2:
		d3[i]=d1[i] + d2[i]
		del d2[i]
	else:
		d3[i]=d1[i]
d3.update(d2)
print("Merged dictionary : ",d3)
