print("***Program to swap 2 numbers without using temporary variables***")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("Before swapping : ",a,b)
a=a+b
b=a-b
a=a-b
print("After swapping : ",a,b)