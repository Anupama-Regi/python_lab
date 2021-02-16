class rectangle:
	x=0
	y=0
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __lt__(self,a2):
		self.a=self.x*self.y
		self.b=a2.x*a2.y
		if self.a < self.b:
			print("Area ",self.a,"is less than Area",self.b)
		elif  self.a == self.b:
			print("Areas are equal")
		else:
			print("Area ",self.a,"is greater than Area",self.b)
l1=int(input("Enter the length of rectangle 1 : "))
b1=int(input("Enter the breadth of rectangle 1 : "))
a1=rectangle(l1,b1)
l2=int(input("Enter the length of rectangle 2 : "))
b2=int(input("Enter the breadth of rectangle 2 : "))
a2=rectangle(l2,b2)
a1<a2