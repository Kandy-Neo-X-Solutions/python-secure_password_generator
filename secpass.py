import secrets
a= int(input("How long should the password be? 8-20 digits"))
characters = "#1234567890qwertzuiopasdfghjklyxcvbnm"
if 8 <= a <= 20:
    # print(a)
    # number = secrets.randbits(a)
    # print(number)
    result = "".join(secrets.choice(characters) for _ in range(a))
    print(result)
    

else:
    print("password is too short or too long")