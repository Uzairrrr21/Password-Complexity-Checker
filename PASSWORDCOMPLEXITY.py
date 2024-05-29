import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check if the password is at least 8 characters long
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long")

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        suggestions.append("Password should contain at least one uppercase letter")

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        suggestions.append("Password should contain at least one lowercase letter")

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        suggestions.append("Password should contain at least one digit")

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

    # If all the conditions are met, the password is valid
    if not suggestions:
        return "Strong", []

    # If there are suggestions, the password is weak
    return "Weak", suggestions

password = input("Input your password: ")
strength, suggestions = check_password_strength(password)

if strength == "Strong":
    print("Valid Password.")
else:
    print("Password does not meet requirements.")
    for suggestion in suggestions:
        print(suggestion)