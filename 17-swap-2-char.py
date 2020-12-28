print("*Program to get a single string from two given strings, separated by a space and swap the first two characters of each string*")
s1=input("Enter the first string : ")
s2=input("Enter the second string : ")
n1=s1[:2]
n2=s2[:2]
print(n2+s1[2:]+' '+n1+s2[2:])
