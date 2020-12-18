print("Program to list ordinary value of each element of a word using list comprehension")
w=input("Enter a word : ")
l=[ord(i) for i in w]
print(l)