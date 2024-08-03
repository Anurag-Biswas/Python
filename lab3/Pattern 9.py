N=int(input("Enter the value of n:"))
print(".")
for i in range(1,N*2,1):
    
    if(i%2!=0 and i!=(N*2-1)):
        print("/",end='')
    elif(i%2==0 and i!=(N*2-1)):
        print("\\")
    elif(i==(N*2-1)):
        print("-")
