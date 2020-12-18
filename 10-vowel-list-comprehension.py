print("*Program to form a list of vowels selected from a given word using list comprehension*")
w=input("Enter a word : ")
v="aeiouAEIOU"
l1=[]
l1=[i for i in w if i in v]
print(l1)