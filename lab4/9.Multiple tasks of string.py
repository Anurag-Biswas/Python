def reverse(s):
    st=""
    for i in range(len(s)-1,-1,-1):
        st=st+s[i]
    print("Reverse",st)
def palindrome(s):
    s=s.upper()
    print(s)
    st=""
    for i in range(len(s)-1,-1,-1):
        st=st+s[i]
    print(st)    
    if st==s:
        print("palindrome")
    else:
        print("not palindrome")
def substring(s,sb):
    if s.endswith(sb)==True:
        print("The string ends with substring")
    else:
        print("The string does not ends with substring")
def capitalyze(s):
    s=s+" "
    st=""
    w=""
    for i in range(0,len(s)):
        if s[i]!=' ':
            w=w+s[i]
        else:
            w=w.capitalize()
            st=st+w+" "
            w=""
    print(st)
def anagram(s,st):
    if len(s)!=len(st):
        print("They are not anagram due to different length")
    else:
        for i in s:
            if i not in st:
                print("not anagram")
                break
        else:
            print("They are anagram")
def remove_vowel(s):
    st=""
    for i in s:
        if i not in 'aeiou' and i not in 'AEIOU':
            st=st+i
    print("After removing vowel",st)
def longest_word(s):
    l=s.split(' ')
    mx=0
    lw=""
    for i in l:
        if len(i)>mx:
            mx=len(i)
            lw=i
    print("Longest word ",lw," size ",mx)        
    
            
    
s=input("Enter a string:")
print("1:reverse\n2:palindrome checking\n3:ends with specific substring or not\n4:capitalise each word\n5:anagram or not\n6:remove vowels\n7:length of longest word:")
ch=int(input("Enter your choice:"))
if ch==1:
    reverse(s)
elif ch==2:
    palindrome(s)
elif ch==3:
    sb=input("Enter the substring:")
    substring(s,sb)
elif ch==4:
    capitalyze(s)
elif ch==5:
    st=input("Enter another word")
    anagram(s,st)
elif ch==6:
    remove_vowel(s)
elif ch==7:
    longest_word(s)
else:
    print("Wrong input")

    
    
    
