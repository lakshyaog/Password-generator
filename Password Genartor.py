import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# User input for password criteria
def main():
    length = int(input("Enter password length (minimum 8): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length < 8:
        print("Password length should be at least 8.")
    else:
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

