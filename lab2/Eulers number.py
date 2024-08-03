n=int(input("Enter a limit:"))
s=1
f=1
for i in range(1,n+1):
    f=f*i
    s=s+1/f
print(s)    
    
