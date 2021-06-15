from collections import Counter
for i in range(0,int(input())):
	k=input()
	m=len(k)//2
	if(len(k)%2==0):

		first_half=k[:m]
		second_half=k[m:]
		count1= Counter(first_half)
		count2 = Counter(second_half)
		if(count1==count2):
			print("YES")
		else:
			print("NO")
	else:

		first_half=k[:m]
		second_half=k[m+1:]
		count1= Counter(first_half)
		count2 = Counter(second_half)
		if(count1==count2):
			print("YES")
		else:
			print("NO")
