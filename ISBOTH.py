k=int(input())
if(k%5==0 and k%11==0):
    print("BOTH")
elif(k%5==0 or k%11==0):
    print("ONE")
else:
    print("NONE")
