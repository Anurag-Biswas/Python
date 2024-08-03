n=int(input("Enter the number:"))
d=n
s=0
while d>0:
    r=d%10
    f=1
    for i in range (1,r+1):
        f=f*i
    s=s+f
    d=d//10
if s==n:
    print("krishnamurthy number",n)
else:
    print("Not a krishnamurthy number",n)
