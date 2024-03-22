import secrets

# here we ask the user what is the desired length for the password that they wants
length = input("Enter the desired length for your password[length * 1.3]\n>>>")
# and here password is going to generate for us
generated_password = secrets.token_urlsafe(int(length))
# and finally here, the password is going to print for us
print(f"Here is your password:\n{generated_password}")
