s=input("Enter a string:")
l=s.split(" ")
mnw=""
mn=len(l[0])
mxw=""
mx=0
for i in l:
    if(len(i)>mx):
        mx=len(l)
        mxw=i
    if(len(i)<mn):
        mn=len(i)
        mnw=i
print("largest:",mxw)
print("Smallest:",mnw)
