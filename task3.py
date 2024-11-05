import re
import getpass

def check_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[@$!%*?&#]', password) is not None
    
    # Calculate the strength score
    strength_score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    # Provide feedback based on the score
    if strength_score == 5:
        return "Strong password"
    elif strength_score >= 3:
        return "Moderate password"
    else:
        return "Weak password"

# Masked input
password = getpass.getpass("Enter your password: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
