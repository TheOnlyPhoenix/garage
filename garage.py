import sys
import os
import platform
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from typed_input import *
from collections import defaultdict
from itertools import chain

class Car():
    def __init__(self, license_num, size, owner, parked = False, park = "", exit = "", debt = 0):
        self.license_num = license_num
        self.size = size
        self.owner = owner
        self.parked = parked
        self.park_time = park
        self.exit_time = exit
        self.debt = debt
    
    def __repr__(self):
        str_license = "License number: " + self.license_num + "\n"
        str_size = "Size: " + str(self.size) + "\n"
        str_own = "Owner: " + self.owner + "\n"
        str_debt = "Debt: " + str(self.debt) + "\n"
        if (self.parked == True):
            str_parked = "Parked: Yes\n"
        else:
            str_parked = "Parked: No\n"
        
        str_park_time = "Park time: " + self.park_time + "\n"
        
        if (self.exit_time != ""): # måste ändra så att om man parkerar igen ska exit_time rensas
            str_exit_time = "Exit time: " + self.exit_time + "\n"
            delta = relativedelta(parse(self.exit_time), parse(self.park_time))
            time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes.")
        else:
            str_exit_time = ""
            time_parked = ""
        return (str_license + str_size + str_own + str_parked + str_park_time + str_exit_time + time_parked + str_debt + "\n")

    def account(self, entry_list, exit_list):
        entry_dict = entry_list
        exit_dict = exit_list
        choice = size_input("What would you like to do? (1/2/3)", int)
        match choice:
            case 1:
                print("1. Check debts")
                self.check_debt(entry_dict, exit_dict)
            case 2:
                print("2. Pay debts")
                self.pay_debt()
            case 3:
                print("3. Go back")
    
    def check_debt(self):
        self.calc_debt()
        
    def pay_debt(self):
        self.calc_debt()

    def calc_debt(self):
        debt = self.debt
        self.exit_time
    
    
def write_history_file(parking_dict, unparked_dict, entry_dict, exit_dict):
    parked_cars = parking_dict
    unparked_cars = unparked_dict
    entry_times = entry_dict
    exit_times = exit_dict
    history_file = "history.csv"
    
    time_list = []
    
    file2 = open(history_file, "w", encoding="utf-8")
    file = input_file("Which file do you want to save to (.csv)? ", "w")
    

    for num_to_check in set(chain(parked_cars.keys(), unparked_cars.keys())):
        if num_to_check in parked_cars:
            car = parked_cars[num_to_check]
        elif num_to_check in unparked_cars:
            car = unparked_cars[num_to_check]
        e = True
        lines = re.sub(r"[\([{})\]]", "", repr(car).strip()).split("\n")
        lines.pop()
        file.write(",".join(lines) + "\n")
        for value in entry_times[car.license_num]:
          time_list.append(value)
        for i in range(len(time_list)):
            lines = re.sub(r"[\([{})\]]", "", time_list[i])
            while e == True:
                file2.write(car.license_num + ",")
                e = False
            print(lines)
            file2.write(lines + ",")
        file2.write("\n")
            

def read_from_file(parked_list, unparked_list, entry_dict, exit_dict):
    parked_cars = parked_list
    unparked_cars= unparked_list
    entry_times = entry_dict
    exit_times = entry_dict
    
    
    file = input_file("Which file do you want to load from (.csv)? ", "r")
    lines = file.readlines()
    
    for line in lines:
        split_line = line.split(",")
        license_num = split_line[0][len("License number: ")]
        size = split_line[1][len("Size: ")]
        owner = split_line[2][len("Owner: ")]
        parked = split_line[3][len("Parked: ")]
        if (parked == "Yes"):
            parked_bool = True
        elif (parked == "No"):
            parked_bool = False
        park_time = split_line[4][len("Park time: ")]
        debt = split_line[6][len("Debt: ")]
        if (parked_bool == True):
            car = Car(license_num, size, owner, parked_bool, park_time, None, debt)
            parked_cars.update({license_num : car})
        elif (parked_bool == False):
            exit_time = split_line[6][len("Exit time: ")]
            car = Car(license_num, size, owner, parked_bool, park_time, exit_time, debt)
            unparked_cars.update({license_num : car})
    
    return parked_cars,unparked_cars,entry_times,exit_times
        
def park(unparked_list):
    unparked_cars = unparked_list
    
    status = input_type("Have you been parked before? (Yes/No) ", str)
    while True: ## behöver fixa felhantering ## ska funka nu
        if (status == "Yes"):
            license_num = license_input("Enter the license number of the car: ")
            park_timestamp = time_input("Which time did you park your car? (HH:MM)")
            if (license_num in unparked_cars):
                car = unparked_cars.get(license_num)
                car.parked= True
                car.park = park_timestamp
                car.exit = ""
                return car
            else:
                print("The license number you entered has never been parked here. Please try again. ")
                continue
        elif (status == "No"):
            license_num = license_input("Enter the license number of the car: ")
            size = size_input("Enter the size of the car (1/2/3): ")
            owner = input_type("Enter the name of the owner of the car: ", str)
            park_timestamp = time_input("Which time did you park your car? (HH:MM) ")
            return Car(license_num, size, owner, True, park_timestamp)
        else:
            status = input("You did not enter \"Yes\" or \"No\". Please try again: ")

def unpark(parked_list, unparked_list):
    parked_cars = parked_list
    unparked_cars= unparked_list
    
    num = exit_input("Enter the license number of your car: ", parked_cars)
    car = parked_cars[num]
    car.parked = False
    car.exit_time = time_input("Which time did you exit the garage? (HH:MM)")
    
    unparked_list.update({num : car})
    del parked_cars[num]
    print("Thank you for parking!")
    
    return parked_cars,unparked_cars

def append_to_dict(parked_dict, unparked_dict, entry_dict, exit_dict):    
    parked_cars = parked_dict
    unparked_cars = unparked_dict
    entry_times = entry_dict
    exit_times = exit_dict
    
    car = park(unparked_cars)
    num = car.license_num

    entry_times[num].append(car.park_time)

    parked_cars.update({num : car})
    print(re.sub(r"[\([{})\]]", "", repr(parked_cars.get(num))))
    
    return parked_cars,unparked_cars,entry_times,exit_times
    

def clear_terminal():
    if (platform.system() == "Linux"):
        os.system('clear')
    elif (platform.system() == "Windows"):
        os.system('cls')

def main():
    parking_garage = {}
    unparked_cars = {}
    entry_dict = defaultdict(list)
    exit_dict = defaultdict(list)
    
    
    print("Welcome to the parking garage! Please choose one of the options below")
    while True:
        clear_terminal()
        
        print("1. Enter the garage")
        print("2. View car information")
        print("3. View account")
        print("4. Load file")
        print("5. Exit the garage")
        print("6. Exit the program")
        
        answer = input()
        match answer:
            case "1":
                parking_garage, unparked_cars, entry_dict, exit_dict = append_to_dict(parking_garage, unparked_cars, entry_dict, exit_dict)
                input("Press Enter to go back")
            case "2":
                license_num = license_input("Enter the license number of the car: \n")
                if (len(list(parking_garage)) > 0 and license_num in parking_garage):
                    print(re.sub(r"[\([{})\]]", "", repr(parking_garage.get(license_num))))
                else:
                    if (len(list(unparked_cars)) > 0 and license_num in unparked_cars):
                        print(re.sub(r"[\([{})\]]", "", repr(unparked_cars.get(license_num))))
                    else:
                        print("There are currently no cars parked in the garage and your car has never been parked in the garage")  
                
                input("Press Enter to go back")
            case "3":
                license_num = license_input("Enter the license number of the car: \n")
                while True:
                    if (len(list(parking_garage)) > 0 and license_num in parking_garage):
                        car = parking_garage.get(license_num)
                        car.account(entry_dict, exit_dict)
                        break
                    else:
                        if (len(list(unparked_cars)) > 0 and license_num in unparked_cars):
                            car = unparked_cars.get(license_num)
                            car.account(entry_dict, exit_dict)
                            break
                        else:
                            print("Your car isn't currently parked and has never been parked in the garage. Please try again.")
            case "4":
                parking_garage, unparked_cars, entry_dict, exit_dict = read_from_file(parking_garage, unparked_cars, entry_dict, exit_dict)
            case "5":
                parking_garage, unparked_cars = unpark(parking_garage, unparked_cars)
                input("Press Enter to go back")
            case "6":
                #parking_garage,unparked_cars = calc_debts(parking_garage, unparked_cars)
                write_history_file(parking_garage, unparked_cars, entry_dict, exit_dict)
                exit()

if __name__ == '__main__':
    main()


"""from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Garage")
        self.setWindowTitle("Garage")
        #self.centralwidget(QtWidgets.QWidget(parent=self))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.setFixedSize(QtCore.QSize(400, 300))
        button = QPushButton("press.")
        button.setFixedSize(QtCore.QSize(100, 50))
        self.setCentralWidget(button)
        button.pressed.connect(self.close)

# Create the app, the main window, and run the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()"""