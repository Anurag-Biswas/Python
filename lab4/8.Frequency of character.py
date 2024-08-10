s=input("Enter a string:")
st=""
c=0
for i in s:
    if i not in st:
        st=st+i
        for j in s:
            if i==j:
                c=c+1
        print(i,",",c)
        c=0
         
    
