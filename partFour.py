username = input("Username: ")
password = input("Password: ")

correct_username = ("admin")
correct_password = ("password123")

if username == correct_username and password == correct_password:
    print("access granted")

else:
    print("error access denied")
