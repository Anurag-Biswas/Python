ages=[19,22,19,24,20,25,26,24,25,24]
print(ages)
ages.sort()
print("Sorted list:",ages)
print("Minimum age:",ages[0])
print("Maximum age:",ages[len(ages)-1])
l=len(ages)
m=l//2
print("median age:",ages[m]/2)
s=0
for i in ages:
    s=s+i
    avg=s/l
print("Average age:",avg)
print("Range of the ages:",ages[l-1]-ages[0])
print("Min-average:",abs(ages[0]-avg))
print("Max-average:",abs(ages[l-1]-avg))
    
