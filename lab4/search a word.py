s=input("Enter a sentence:")
w=input("Enter a word to be searched:")
l=s.split(" ")
for i in l:
    if(i==w):
        print("Word found")
        break
else:
    print("Word not found")
