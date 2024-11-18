import random
import string

def generate_custom_password(length=10, use_upper=True, use_lower=True, use_digits=True, use_punctuation=True):
    
    character_pool = ''
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_punctuation:
        character_pool += string.punctuation
    
   
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    
    password = []
    
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_punctuation:
        password.append(random.choice(string.punctuation))
    
    
    while len(password) < length:
        password.append(random.choice(character_pool))
    
   
    random.shuffle(password)
    
   
    return ''.join(password)


password_length = int(input("Enter the desired password length (minimum 8): "))
if password_length < 8:
    print("Password length should be at least 8 characters for better security.")
else:
    print("Choose character types to include:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

    try:
        password = generate_custom_password(password_length, use_upper, use_lower, use_digits, use_punctuation)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)