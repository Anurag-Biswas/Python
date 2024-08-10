Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=input("Enter a string:")
Enter a string:abcdefgabc
>>> st=""
>>> c=0
>>> for i in s:
...     if i not in st:
...         st=st+i
...         for j in s:
...             if i==j:
...                 c=c+1
...         print(i,",",c)
...         c=0
... 
a , 2
b , 2
c , 2
d , 1
e , 1
f , 1
g , 1
