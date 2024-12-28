import string

def check_password_strength():
    password = input("Enter your password: ")
    if not password:
        print("Password cannot be empty. Please try again.")
        return

    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "That is a very bad password.\nYou have to change it as soon as possible."
    elif strength == 2:
        remarks = "That is a weak password.\nYou should change it."
    elif strength == 3:
        remarks = "Your password is okay, but it can be improved."
    elif strength == 4:
        remarks = "Your password is hard to guess. You can make it even more secure."
    elif strength == 5:
        remarks = "Your password is very strong."

    print("\nYour password contains:")
    print(f"{lower_count} lowercase letters.")
    print(f"{upper_count} uppercase letters.")
    print(f"{num_count} numbers.")
    print(f"{wspace_count} white spaces.")
    print(f"{special_count} special characters.\n")

    print(f"Password Strength Score: {strength}/5")
    print(f"Remarks: {remarks}")

def check_pwd(another_pw=False):
    valid = False
    if another_pw:
        choice = input("Do you want to check another password strength? (y/n): ")
    else:
        choice = input("Do you want to check a password's strength? (y/n): ")

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print("Exiting...")
            return False
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    print("========= Welcome to Password Strength Checker =========")
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)
