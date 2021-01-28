print("Program that sorts dictionaries in ascending and descending order.")
n=int(input("Enter number of items : "))
dict1={}
for i in range(n):
	keys=input("Enter key : ")
	values=input("Enter value : ")
	dict1[keys]=values
print(dict1)
#print(dict1.items())
#print(dict1.keys())
#print(dict1.values())
dict_d=dict(sorted(dict1.items()))
print("Sorted dictionary in ascending order : ",dict_d)
dict_d=dict(sorted(dict1.items(),reverse=True))
print("Sorted dictionary in descending order : ",dict_d)
