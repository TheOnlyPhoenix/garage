"""Main file in the program.
"""
import sys
import os
import platform
from car import Car
from garage import Garage
from typed_input import *
from collections import defaultdict
from itertools import chain

def write_history_file(garage):
    """Function that extracts car info and times from various dictionaries in the program, 
    and writes them to two separate files. One file is decided by the user, the other is decided by the program.
    """
    history_file = "history.csv"
    entry_list = []
    exit_list = []
    
    file2 = open(history_file, "w", encoding="utf-8")
    file = input_file("Which file do you want to save to? (.csv) ", "w")
    
    for num_to_check in set(chain(garage.parked_dict.keys())):
        if num_to_check in garage.parked_dict:
            car = garage.parked_dict[num_to_check]
        e = True
        lines = re.sub(r"[\([{})\]]", "", repr(car).strip()).split("\n")
        file.write(",".join(lines) + "\n")
        
        entry_list = list(garage.entry_dict[car.license_num])
        exit_list = list(garage.exit_dict[car.license_num]) 
        while e == True:
            file2.write(car.license_num + ",")
            e = False
        for i in range(len(entry_list)):
            line1 = re.sub(r"[\([{})\]]", "", entry_list[i])
            line2 = re.sub(r"[\([{})\]]", "", exit_list[i])
            joined_lines = ",".join([line1,line2]) + ","
            file2.write(joined_lines)
        file2.write("\n")
            
def read_from_file(garage):   
    """Function that reads data from the file specified by the user 
    and one file that is permanently specified by the program
    """
    license_num = ""
    file = input_file("Which file do you want to load from (.csv)? ", "r")
    try:
        file2 = open("history.csv", "r", encoding="utf-8")
    except:
        pass    
    
    lines = file.readlines()
    for line in lines:
        input(line)
        split_line = line.split(",")
        license_num = split_line[0][len("License number: "):]
        size = split_line[1][len("Size: "):]
        owner = split_line[2][len("Owner: "):]
        debt = split_line[3][len("Debt: "):].strip()
        car = Car(license_num, size, owner, debt)
        garage.parked_dict.update({license_num : car})
    
    time_lines = file2.readlines()
    for time_line in time_lines:
        times = time_line.split(",")
        for i in range(1, len(times)):
            if i % 2 == 1:
                garage.entry_dict[license_num].append(times[i])
            elif i % 2 == 0:
                exit_time = times[i].strip()
                garage.exit_dict[license_num].append(exit_time)
        
    return garage

def view_history(garage, num):
    """Shows the user the parking history and dates of a specific car"""
    for entry_combo, exit_time in zip(garage.entry_dict[num], garage.exit_dict[num]):
        day,entry_time = entry_combo.split(";")
        
        message = "Day parked: " + day + "\nEntry time: " + entry_time + "\nExit time: " + exit_time
        print(message)
        input("Press enter to see the next time") #ändra så att den körs bara när det finns en till efter
            

def clear_terminal():
    """Function that clears the terminal"""
    if (platform.system() == "Linux"):
        os.system('clear')
    elif (platform.system() == "Windows"):
        os.system('cls')

def menu(garage):
    """Menu function that takes in a date and handles the navigation through the program."""
    date = input_date("Enter the date (YYYY-MM-DD) ")
    print("Welcome to the parking garage! Please choose one of the options below:")

    while True:
        clear_terminal()
        
        print("1. Park/Unpark")
        print("2. View car information")
        print("3. View car parking history")
        print("4. View account")
        print("5. Load file")
        print("6. Exit the program")
        
        answer = input()
        match answer:
            case "1":
                garage.append_to_dict(date)
                input("Press Enter to go back")
            case "2":
                license_num = license_input("Enter the license number of the car (ABC123): \n")
                if (len(list(garage.parked_dict)) > 0 and license_num in garage.parked_dict):
                    print(re.sub(r"[\([{})\]]", "", repr(garage.parked_dict.get(license_num))))
                else:
                    print("There are currently no cars parked in the garage and your car has never been parked in the garage")  
                
                input("Press Enter to go back")
            case "3":
                license_num = license_input("Enter the license number of the car (ABC123): \n")
                if (len(list(garage.parked_dict)) > 0 and license_num in garage.parked_dict):
                    view_history(garage, license_num)
                else:
                    print("There are currently no cars parked in the garage and your car has never been parked in the garage")  
                
                input("Press Enter to go back")
            case "4":
                license_num = license_input("Enter the license number of the car (ABC123): \n")
                while True:
                    if (len(list(garage.parked_dict)) > 0 and license_num in garage.parked_dict):
                        car = garage.parked_dict.get(license_num)
                        car.account(garage.entry_dict, garage.exit_dict)
                        break
                    
                    else:
                        print("Your car isn't currently parked and has never been parked in the garage. Please try again.")
                        license_num = license_input("Enter the license number of the car (ABC123): \n")
                        continue
            case "5":
                garage = read_from_file(garage)
            case "6":
                write_history_file(garage)
                exit()

def main():
    garage = Garage()
        
    menu(garage)

def input_date(message : str):
    """Asks the user to input a date in the form YYYY-MM-DD. If the program cannot match the time to the regex ('^\d{4}-\d{2}-\d{2}$'), it will ask the user again"""
    while True:
        user_input = input(message)
        if (re.match(r'^\d{4}-\d{2}-\d{2}$', user_input)):
            return user_input
        else: 
            print("You did not enter a date in the form YYYY-MM-DD. Please try again")

if __name__ == '__main__':
    main()


