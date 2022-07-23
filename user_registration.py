print("Wellcome to Lígia's code!")
Login=(str(input("Type your login: ")))
Password=(str(input("Type your password: ")))

while Login == Password:
    print("Repeat your password. Login and password cannot be equal!")
    Login=(str(input("Type your login: ")))
    Password=(str(input("Type your password: ")))

else:
    print("Registration Sucessful")
