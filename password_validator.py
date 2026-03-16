password = input("Enter your password: ")
length = len(password)

print("Data type:", type(password))

if length >= 8:
    print("Password is valid")
else:
    print("Password must be at least 8 characters long")