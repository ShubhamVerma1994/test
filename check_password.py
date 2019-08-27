password = (input("Enter a password: "))
dcount = dalpha = dupper = 0
for i in password:
    if i.isdigit():
        dcount += 1
    if not i.isalnum():
        dalpha += 1
    if not i.isupper():
        dupper += 1
if dcount >= 1 and dalpha >= 1 and dupper >= 1 and password[0].isalpha() and len(password) >= 6:
        print("Valid Password")
else :
    print("Invalid Password")


