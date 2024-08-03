m=int(input("Enter the number:"))
n=int(input("Enter the second number:"))
for i in range(1,m+1):
    p=1
    for j in range(1,n+1):
        p=i*j
        print(i,"x",j,"=",p)
        
