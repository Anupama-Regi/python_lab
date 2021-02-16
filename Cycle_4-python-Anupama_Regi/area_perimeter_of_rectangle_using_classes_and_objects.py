class rect:
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def area(self):
		self.a=0
		self.a=self.length*self.breadth
		print("Area of rectangle with length ",self.length," and breadth ",self.breadth,"is ",self.a)
	def perimeter(self):
		self.p=0
		self.p=2*(self.length+self.breadth)
		print("Perimeter of rectangle  with length ",self.length," and breadth ",self.breadth,"is ",self.p)
	def __gt__(self,r):
		r.area=r.length*r.breadth
		if self.a > r.area:
			print("Area of First rectangle is greater than Second rectangle...")
		elif self.a < r.area:
			print("Area of First rectangle is less than Second rectangle...")
		else:
			print("Both rectangle is equal...")

c=0
n=int(input("Enter the length of first rectangle : "))
m=int(input("Enter the breadth of first rectangle : "))
r1=rect(n,m)
o=int(input("Enter the length of second rectangle : "))
p=int(input("Enter the breadth of second rectangle : "))
r2=rect(o,p)
while(c!=4):
	print("Choices are : \n1.Area\n2.Perimeter\n3.Compare area\n4.Exit")
	c=int(input("Enter your choice : "))
	if c == 1:
		r1.area()
		r2.area()
	elif c == 2:
		r1.perimeter()
		r2.perimeter()
	elif c == 3:
		r1 > r2
	elif c== 4:
		break;
	else:
		print("Invalid choice...")