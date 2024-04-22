"""
Encrypt passwords with argon2

"""

import argon2

def hash_password(password):
    hasher = argon2.PasswordHasher()
    hashed_password = hasher.hash(password)
    return hashed_password

def verify_password(hashed_password, password):
    hasher = argon2.PasswordHasher()
    try:
        hasher.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

if __name__ == "__main__":
    password = input("Enter password to hash with argon2: ")
    
    # Hash the password
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)
    
    # Verify the password
    entered_password = input("Enter password to verify: ")
    if verify_password(hashed_password, entered_password):
        print("Password is correct!")
    else:
        print("Password is incorrect!")
