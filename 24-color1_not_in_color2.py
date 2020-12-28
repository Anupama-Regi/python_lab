print("Program that prints out all colors from color-list1 not contained in color-list2")
l=input("Enter list1 of colors : ")
l2=input("Enter list2 of colors : ")
a=l.split()
b=l2.split()
l3=[i for i in a if i not in b]
print(l3)