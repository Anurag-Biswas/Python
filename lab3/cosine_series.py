import math
n=int(input("Enter the term:"))
v=2
s=1
x=int(input("Enter x:"))
print("cosine(x)",math.cos(x))
for i in range(2,n+1):
    f=1
    for j in range(1,v+1):
        f=f*j
    d=x**v/f
    f=1
    if(i%2==0):
        s=s+d
    else:
        s=s-d
    v=v+2
print(s)    
