s="India is my motherland. I love my country. Capital of India is New Delhi."
print("Length of the string",len(s))
print(s[33:40])
d={}
c=0
l=s.split(' ')
for i in l:

    for j in l:
        if i==j:
            c=c+1
    d[i]=c
    c=0
print(d)
