import re
"""Module to retrieve inputs from user"""

def input_type(message : str, convert_type = str):
    """Asks the user for input. If the program is unable to convert to the type 'convert_type', the program will ask the user again.
    Args:
        message (string): Message displayed to user
        convert_type (class): Type to convert input to
    Returns:
        convert_type: Input of type (convert_type)
    """
    while True:
        user_input = input(message)
        try:
            return convert_type(user_input)
        except:
            print(f"That was not of the type {convert_type.__name__}. Please enter again")

def license_input(message : str):
    """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$', the program will ask the user again.
    Args:
        message (string): Message displayed to user
    Returns:
        user_input: Input matched to regular expression ('^[A-Z]{3}\d{3}$')
    """
    while True:
        user_input = input_type(message, str)
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input)):
            return user_input
        else:
            print(f"You did not enter a valid license number (ABC123). Please try again")

def exit_input(message : str, parking_list : dict):
    """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$' and find the input in a list, the program will ask the user again.
    Args:
        message (string): Message displayed to user
        parking_list (list): List to check license number against
    Returns:
        user_input: Input matched to regular expression ('^[A-Z]{3}\d{3}$') and checked to exist in list
    """
    while True:
        user_input = input_type(message, str)   
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input) and user_input in parking_list):
            return user_input
        else:
            print(f"You did not enter a valid license number (ABC123) or the car does not exist in the garage. Please try again")

def size_input(message : str, convert_type = int):
    """Asks the user for input. If the program is unable to find 1, 2 or 3 as the input, the program will ask the user again.
    Args:
        message (string): Message displayed to user
    Returns:
        user_input: Input that is 1, 2 or 3
    """
    while True:
        user_input = input_type(message, convert_type)
        if (user_input == 1 or user_input == 2 or user_input == 3):
            return user_input
        else:
            print(f"You did not enter 1, 2 or 3. Please try again")

def input_file(message : str):
    """Asks the user to input a filename. If the program cannot find the file specified by the user, the program will ask the user again.
    Args:
        message (string): Message displayed to user
    Returns:
        TextIOWrapper: Object representing the file with data.
    """
    while True:
        user_input = input(message)
        try:
            return open(user_input, "r", encoding="utf-8")
        except:
            print(f"There is no file named {user_input}. Please enter a new file: \n")