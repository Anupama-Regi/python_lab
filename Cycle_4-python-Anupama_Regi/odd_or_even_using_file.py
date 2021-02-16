f1=open('odd_and_even.txt','r')
f2=open('even.txt','w')
f3=open('odd.txt','w')
for i in map(int,f1.readline().split()):
	if i%2==0:
		f2.write(str(i)+" ")
	else:
		f3.write(str(i)+" ")
