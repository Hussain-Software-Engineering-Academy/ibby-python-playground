password = "dragon"
attempts = 3
while attempts > 0:
    password_attempt = input("Enter the password: ")
    if password_attempt == password:
        print("Access granted.")
        break
    elif password_attempt != password:
        attempts = attempts - 1
print("Access denied.")