n=int(input("Enter a number"))
s=0
for i in range(1,n,1):
    if(n%i==0):
        s=s+i
if(s==n):
    print("Perfect number",n)
else:
    print("Not a perfect number",n)
    
