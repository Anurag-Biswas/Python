lines=""
print("Enter the lines:")
while True:
    l=input()
    if not l:
        break
    lines=lines+"\n"+l.upper()
print(lines)
