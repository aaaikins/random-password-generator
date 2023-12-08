import random

def generate_characters(num_letters, num_symbols, num_numbers, letters, symbols, numbers):
    """
    Generate a list of characters for the password.

    Args:
        num_letters (int): Number of letters to include.
        num_symbols (int): Number of symbols to include.
        num_numbers (int): Number of numbers to include.
        letters (list): List of letters to choose from.
        symbols (list): List of symbols to choose from.
        numbers (list): List of numbers to choose from.

    Returns:
        list: List of characters for the password.
    """
    password_list = []

    for _ in range(num_letters):
        password_list.append(random.choice(letters))

    for _ in range(num_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(num_numbers):
        password_list.append(random.choice(numbers))

    return password_list

def get_valid_input(prompt, valid_choices):
    """
    Get valid user input.

    Args:
        prompt (str): The prompt to display to the user.
        valid_choices (list): List of valid choices.

    Returns:
        int: Valid user input.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password():
    """
    Generate a password based on user input for the number of letters, symbols, and numbers.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = get_valid_input("How many letters would you like in your password?\n", letters)
    num_symbols = get_valid_input(f"How many symbols would you like?\n", symbols)
    num_numbers = get_valid_input(f"How many numbers would you like?\n", numbers)

    password_list = generate_characters(num_letters, num_symbols, num_numbers, letters, symbols, numbers)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print(f"Your password is: {password}")

def regenerate_password():
    """
    Ask the user if they want to regenerate a password and, if yes, call the generate_password function.
    """
    regenerate = input("Do you want to regenerate a password? (yes/no)\n").lower()
    if regenerate == "yes":
        generate_password()
    else:
        print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    generate_password()
    regenerate_password()
