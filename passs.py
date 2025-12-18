def pass_strength():
    password=input("enter password nigga")
    strength = 0
    a = [0,0,0]
    if(len(password)>8):
        strength+=1
    for c in password:
        if(not c.isalnum() and a[0]==0):
            strength+=1
        if(c.isnumeric() and a[1]==0):
            strength+=1
        if(c.isupper() and a[2]==0):
            strength+=1

    if(strength<1):
        print("gay")
    if(strength<2):
        print("weak")
    if(strength<3):
        print("moderate")
    if(strength<4):
        print("strong")
    if(strength<5):
        print("fap")
pass_strength()