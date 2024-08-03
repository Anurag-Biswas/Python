n=int(input("Enter n:"))
if(n==2):
    for i in range(1,n*3):
        if i%2!=0:
            print("-")
        else:
            for j in range(1,3):
                if i==2 and j==i or i==4 and j==1:
                    print("|")
                else:
                    print(" ",end='')
elif n==3:
    for i in range(1,n*2):
        if(i%2!=0):
            print("-")
        else:
            for j in range(1,4):
                if j==3:
                    print("|")
                else:
                    print(" ",end='')
elif n==4:
    for i in range(1,5):
        if(i<=3):
            if i%2!=0:
                print("|",end='')
            else:
                print("_",end='')
        else:
            print("\n  |")
                
