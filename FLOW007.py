for i in range(0,int(input())):
	n = int(input())
	m=""
	while(n>0):
		m = m+str(n%10)
		n=n//10
	print(int(m))
