print("***Program to check whether a year is Leap year or not...***")
a=int(input("Enter a year : "))
if a%4==0 and a%100!=0 or a%400==0:
	print(a,"is Leap year")
else:
	print(a,"is not leap year")