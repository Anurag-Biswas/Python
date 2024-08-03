n=int(input("Enter a number"))
s=0
c=n
while(c>0):
    r=c%10
    s=s+r*r*r
    c=c//10
if(s==n):
    print("Armstrong number",n)
else:
    print("Not an armstrong number",n)
