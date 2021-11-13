print("Create an account.")
username = input("Enter your username: ")
password = input("Enter your passcode: ")

print("You have created your acoount.\nNow log in to your account.")
val1 = input("Username: ")
val2 = input("Password: ")

if val1 == username and val2 == password:
    print("Welcome to your account")
else:
    print("Invalid credentials")