a=float(input("Enter side of square : "))
a1=lambda a : a*a
print("Area of square : ",a1(a))
l=float(input("Enter length of rectangle : "))
b=float(input("Enter breadth of rectangle : "))
a2=lambda l,b : l*b
print("Area of rectangle : ",a2(l,b))
b2=float(input("Enter breadth of triangle : "))
h=float(input("Enter height of triangle : "))
a3=lambda b2,h : (1/2)*b2*h
print("Area of triangle : ",a3(b2,h))