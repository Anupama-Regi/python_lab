print("*program to remove the n th index character from a non-empty string*")
s=input("Enter a string : ")
n=int(input("Enter the position of string to remove : "))
s1=s[:n]
s2=s[n+1:]
#print(s1)
#print(s2)
print("The string after removing the n th index character : ",s1+s2)