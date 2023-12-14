import re
"""Module to retrieve inputs from user"""

def input_type(user_input, convert_type = str):
    """Asks the user for input. If the program is unable to convert to the type 'convert_type', the program will ask the user again.
    """
    while True:
        try:
            return convert_type(user_input)
        except:
            print(f"That was not of the type {convert_type.__name__}. Please enter again")



def exit_input(user_input : str, parking_list : dict):
    """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$' and find the input in a list, the program will ask the user again.
    """
    while True:  
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input) and user_input in parking_list):
            return user_input
        else:
            print(f"You did not enter a valid license number (ABC123) or the car does not exist in the garage. Please try again")
            
def time_input(user_input : str):
    """Asks the user to input a time. If the program cannot match the time to HH:MM, the program will ask the user again.
    """
    while True:

        if (re.match(r'^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', user_input)):
            return user_input
        else:
            print("You did not enter a time in the format HH:MM. Please enter a new time.")