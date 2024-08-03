n=int(input("Enter a number:"))
for i in range (1,n+1):
    print(i,end='')
    for j in range(1,n):
        print(i**(j-1),end='')
    print()    
