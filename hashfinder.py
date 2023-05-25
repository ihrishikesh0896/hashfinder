import itertools
import hashlib

def crack_password(password_hash, character_set, password_length):
    for password in itertools.product(character_set, repeat=password_length):
        password = ''.join(password)
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == password_hash:
            return password
    return None

password_hash = input("Enter the password hash: ")
character_set = input("Enter the character set (e.g., abcdefghijklmnopqrstuvwxyz0123456789): ")
password_length = int(input("Enter the maximum password length: "))

password = crack_password(password_hash, character_set, password_length)
if password:
    print("Password found:", password)
else:
    print("Password not found.")
