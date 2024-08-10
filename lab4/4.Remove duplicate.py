s=input("Enter white space separated words:")
l=s.split(" ")
lst=[]
for i in l:
    if i not in lst:
        lst.append(i)
lst.sort()
st=""
for i in lst:
    st=st+i+" "
print(st)    
