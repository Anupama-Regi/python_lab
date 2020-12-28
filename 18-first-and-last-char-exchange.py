print("Program to change a given string to a new string where the first and last chars have been exchanged")
s=input("Enter the string : ")
s1=s[-1]+s[1:-1]+s[0]
print("String after exchanging first and last chars : ",s1)