import random

def generate_password(length=12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def reshuffle_password(password):
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


password = generate_password()
print("Generated password:", password)

choice = input("Would you like to reshuffle it? (yes/no): ").strip().lower()

if choice == 'yes':
    reshuffled = reshuffle_password(password)
    print("Reshuffled password:", reshuffled)
else:
    print("Okay! Your password is:", password)