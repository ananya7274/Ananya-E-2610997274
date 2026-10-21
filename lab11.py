username = input("Enter your username: ")
password = input("Enter your password: ")
minimum_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
password_valid = minimum_length and has_digit and has_uppercase
print("\n" + "=" * 40)
print("PASSWORD VALIDATION REPORT")
print("=" * 40)

print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print("\n--- Validation Rules ---")

if minimum_length:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_uppercase:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")
print("\n--- Result ---")
if password_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID.")
    print("Account creation failed.")
print("=" * 40)
