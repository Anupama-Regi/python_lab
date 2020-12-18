print("*Program to accept a filename from the user and print the extension of that file*")
f=input("Enter the file name with extension :")
l1=f.split('.')
print("Extension of the file named ",f,"is '",l1[1],"'")