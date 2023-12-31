import re
"""Module to retrieve inputs from user"""

def input_type(message : str, convert_type = str):
    """Asks the user for input. If the program is unable to convert to the type 'convert_type', the program will ask the user again.
    """
    while True:
        user_input = input(message)
        try:
            return convert_type(user_input)
        except:
            print(f"That was not of the type {convert_type.__name__}. Please enter again")

def license_input(message : str):
    """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$', the program will ask the user again.
    """
    while True:
        user_input = input_type(message, str)
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input)):
            return user_input
        else:
            print(f"You did not enter a valid license number (ABC123). Please try again")

def exit_input(message : str, parking_list : dict):
    """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$' and find the input in a list, the program will ask the user again.
    """
    while True:
        user_input = input_type(message, str)   
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input) and user_input in parking_list):
            return user_input
        else:
            print(f"You did not enter a valid license number (ABC123) or the car does not exist in the garage. Please try again")

def size_input(message : str, convert_type = int):
    """Asks the user for input. If the program is unable to find 1, 2 or 3 as the input, the program will ask the user again.
    """
    while True:
        user_input = input_type(message, convert_type)
        if (user_input == 1 or user_input == 2 or user_input == 3):
            return user_input
        else:
            print(f"You did not enter 1, 2 or 3. Please try again")

def input_file(message : str, action = "r"):
    """Asks the user to input a filename. If the program cannot find the file specified by the user, the program will ask the user again.
    """
    while True:
        user_input = input(message)
        try:
            return open(user_input, action, encoding="utf-8")
        except:
            print(f"There is no file named {user_input}. Please enter a new file: \n")
            
def time_input(message : str):
    """Asks the user to input a time. If the program cannot match the time to HH:MM, the program will ask the user again.
    """
    while True:
        user_input = input(message)
        if (re.match(r'^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', user_input)):
            return user_input
        else:
            print("You did not enter a time in the format HH:MM. Please enter a new time.")