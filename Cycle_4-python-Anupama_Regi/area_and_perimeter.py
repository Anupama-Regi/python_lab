from Graphics import circle,rectangle
from Graphics.threedgraphics import *
l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
rectangle.rect_area(l,b)
rectangle.rect_perimeter(l,b)

r=int(input("Enter the radius of circle : "))
circle.circle_area(r)
circle.circle_perimeter(r)

a=int(input("Enter the length of cuboid : "))
c=int(input("Enter the breadth of cuboid : "))
d=int(input("Enter the heigth of cuboid : "))
cuboid.cuboid_area(a,c,d)
cuboid.cuboid_perimeter(a,c,d)

r1=int(input("Enter the radius of sphere : "))
sphere.sphere_area(r1)
sphere.sphere_perimeter(r1)