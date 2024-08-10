s=input("Enter comma separated words:")
l=s.split(',')
l.sort()
t=""
for i in l:
    t=t+i+","
print(t)
