print("*Program to get a string from a given string where all occurrences of its first char have been changed to '$' except the first char itself.*")
s=input("Enter a string : ")
f=s[0]
#print(f)
f2=s[1:].replace(f,'$')
f3=f+f2
print("String after replacing all occurrences of its first char with '$': ",f3)