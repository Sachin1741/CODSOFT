import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_chars = lower + upper + digits + special
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
