n=int(input("Enter the value of n:"))
s=0
for i in range(1,n+1,1):
    d=1/i
    if(i%2==0):
        print("- 1/",i,end='')
        s=s-d
    else:
        if i==1:
            print("1/",i,end=' ')
        else:
            print("+ 1/",i,end='')
        s=s+d
print("=",s)            
            
