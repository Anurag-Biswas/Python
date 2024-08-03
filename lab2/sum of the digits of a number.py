n=int(input("Enter a number:"))
s=0
d=n
while d>0:
    r=d%10
    s=s+r
    d=d//10
print(s)    
