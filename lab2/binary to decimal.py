n=int(input("Enter the binary number:"))
s=0
i=0
while(n>0):
    r=n%10
    s=s+2**i*r
    n=n//10
    i=i+1   
print(s)    
