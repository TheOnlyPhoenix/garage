import sys
import os
import platform
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from typed_input import *
from collections import defaultdict
from itertools import chain

class Car():
    def __init__(self, license_num, size, owner, parked = False, park = "", exit = "", debt = 0, park_day = "", exit_day = ""):
        self.license_num = license_num
        self.size = size
        self.owner = owner
        self.parked = parked
        self.park_time = park
        self.exit_time = exit
        self.debt = debt
        self.park_day = park_day
        self.exit_day = exit_day
    
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

    def account(self, entry_dict, exit_dict, day):
        entry_list = list(entry_dict[self.license_num])
        exit_list = list(exit_dict[self.license_num]) 
        self.calc_debt(entry_list, exit_list, day)
        print("1. Check debts")
        print("2. Pay debts")
        print("3. Go back")
        choice = size_input("What would you like to do? (1/2/3)", int)
        match choice:
            case 1:
                self.check_debt(entry_dict, exit_dict, day)
            case 2:
                self.pay_debt(entry_list, exit_list, day)
            case 3:
                pass
                
    
    def check_debt(self, entry_dict, exit_dict):
        pass
        
        
    def pay_debt(self, entry_list, exit_list, day):
        self.calc_debt(entry_list, exit_list, day)

    def calc_debt(self, entry_list, exit_list, day):
        print("hi1")
        if len(exit_list) == len(entry_list):
            for entry_time, exit_time in zip(entry_list, exit_list):
                print("hi2")
                time1 = int(entry_time.split(":"))
                time2 = int(exit_time.split(":"))
                print(time1)
                input
                if time1[1] > time2[1]:
                    diff_hours = time1[1] - time2[1]
                    diff_hours = 24 - diff_hours
                else:
                    diff_hours = time1[1] - time2[1]
            
                time_parked = diff_hours +  time1[0] * 24   
        else:
            for entry_time in entry_list:
                time1 = int(entry_time.split[":"])
                time2 = time_input("What time is it now? (HH:MM)")
                if time1[1] > time2:
                    diff_hours = time1[1] - time2
                    diff_hours = 24 - diff_hours
                else:
                    diff_hours = time1 - time2
                time_parked = diff_hours +  time1[0] * 24
            
                
            
                
        
    
    
def write_history_file(parking_dict, unparked_dict, entry_dict, exit_dict, day):
    history_file = "history.csv"
    cur_day = day
    
    time_list = []
    
    file2 = open(history_file, "w", encoding="utf-8")
    file = input_file("Which file do you want to save to (.csv)? ", "w")
    

    for num_to_check in set(chain(parking_dict.keys(), unparked_dict.keys())):
        if num_to_check in parking_dict:
            car = parking_dict[num_to_check]
        elif num_to_check in unparked_dict:
            car = unparked_dict[num_to_check]
        e = True
        lines = re.sub(r"[\([{})\]]", "", repr(car).strip()).split("\n")
        lines.pop()
        file.write(",".join(lines) + "\n")
        for value in entry_dict[car.license_num]:
          time_list.append(value)
        for i in range(len(time_list)):
            lines = re.sub(r"[\([{})\]]", "", time_list[i])
            while e == True:
                file2.write(car.license_num + ",")
                e = False
            print(lines)
            file2.write(lines + ",")
        file2.write("\n")
            

def read_from_file(parked_dict, unparked_dict, entry_dict, exit_dict):   
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
            parked_dict.update({license_num : car})
        elif (parked_bool == False):
            exit_time = split_line[6][len("Exit time: ")]
            car = Car(license_num, size, owner, parked_bool, park_time, exit_time, debt)
            unparked_dict.update({license_num : car})
    
    return parked_dict,unparked_dict,entry_dict,exit_dict
        
def park(unparked_dict):    
    status = input_type("Have you been parked before? (Yes/No) ", str)
    while True: ## behöver fixa felhantering ## ska funka nu
        if (status == "Yes"):
            license_num = license_input("Enter the license number of the car (ABC123): ")
            park_timestamp = time_input("Which time did you park your car? (HH:MM)")
            if (license_num in unparked_dict):
                car = unparked_dict.get(license_num)
                car.parked= True
                car.park = park_timestamp
                car.exit = ""
                return car
            else:
                print("The license number you entered has never been parked here. Please try again. ")
                continue
        elif (status == "No"):
            license_num = license_input("Enter the license number of the car (ABC123): ")
            size = size_input("Enter the size of the car (1/2/3): ")
            owner = input_type("Enter the name of the owner of the car: ", str)
            park_timestamp = time_input("Which time did you park your car? (HH:MM) ")
            return Car(license_num, size, owner, True, park_timestamp)
        else:
            status = input("You did not enter \"Yes\" or \"No\". Please try again: ")

def unpark(parked_dict, unparked_dict, exit_dict, day):
    num = exit_input("Enter the license number of your car (ABC123): ", parked_dict)
    car = parked_dict[num]
    car.parked = False
    car.exit_time = time_input("Which time did you exit the garage? (HH:MM)")
    day_and_time = day + ":" + car.exit_time
    exit_dict[num].append(day_and_time)
    unparked_dict.update({num : car})
    del parked_dict[num]
    print("Thank you for parking!")
    
    return parked_dict,unparked_dict,exit_dict

def append_to_dict(parked_dict, unparked_dict, entry_dict, day):    
    car = park(unparked_dict)
    num = car.license_num
    day_and_time = day + ":" + car.park_time
    entry_dict[num].append(day_and_time)
    parked_dict.update({num : car})
    print(re.sub(r"[\([{})\]]", "", repr(parked_dict.get(num))))
    
    return parked_dict,unparked_dict,entry_dict
    

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
    day_list = []
    
    day = str(input_type("What day of the month is it? ", int))
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
                parking_garage, unparked_cars, entry_dict = append_to_dict(parking_garage, unparked_cars, entry_dict, day)
                input("Press Enter to go back")
            case "2":
                license_num = license_input("Enter the license number of the car (ABC123): \n")
                if (len(list(parking_garage)) > 0 and license_num in parking_garage):
                    print(re.sub(r"[\([{})\]]", "", repr(parking_garage.get(license_num))))
                else:
                    if (len(list(unparked_cars)) > 0 and license_num in unparked_cars):
                        print(re.sub(r"[\([{})\]]", "", repr(unparked_cars.get(license_num))))
                    else:
                        print("There are currently no cars parked in the garage and your car has never been parked in the garage")  
                
                input("Press Enter to go back")
            case "3":
                license_num = license_input("Enter the license number of the car (ABC123): \n")
                car = parking_garage.get(license_num)
                #car.calc_debt(list(entry_dict[license_num]), list(exit_dict[license_num]), day)
                while True:
                    if (len(list(parking_garage)) > 0 and license_num in parking_garage):
                        car = parking_garage.get(license_num)
                        car.account(entry_dict, exit_dict, day)
                        break
                    else:
                        if (len(list(unparked_cars)) > 0 and license_num in unparked_cars):
                            car = unparked_cars.get(license_num)
                            car.account(entry_dict, exit_dict, day)
                            break
                        else:
                            print("Your car isn't currently parked and has never been parked in the garage. Please try again.")
            case "4":
                parking_garage, unparked_cars, entry_dict, exit_dict = read_from_file(parking_garage, unparked_cars, entry_dict, exit_dict)
            case "5":
                parking_garage, unparked_cars = unpark(parking_garage, unparked_cars, exit_dict, day)
                input("Press Enter to go back")
            case "6":
                #parking_garage,unparked_cars = calc_debts(parking_garage, unparked_cars)
                write_history_file(parking_garage, unparked_cars, entry_dict, exit_dict, day)
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