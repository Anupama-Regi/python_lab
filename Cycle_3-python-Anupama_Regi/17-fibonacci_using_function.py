print("Program to find fibonacci series of n terms")
def fib(n):
	a=0
	b=1
	print("Fibonacci series : ")
	for i in range(1,n+1):
		print(a)
		c=a+b
		a=b
		b=c
n=int(input("Enter the number limit to find fibonacci : "))
fib(n)