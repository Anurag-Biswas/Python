def check_season(m):
    if(m=="September" or m=="October"):
        return "Autumn"
    elif(m=="November" or m=="December" or m=="January"):
        return "Winter"
    elif(m=="February" or m=="March"):
        return "Spring"
    elif(m=="April" or m=="May" or m=="June"):
        return "Summer"
m=input("Enter the month:")
print(check_season(m))
