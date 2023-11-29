import sys
import os
import time
import datetime as dt
import platform
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from typed_input import *

class Car():
    def __init__(self, license_num, size, owner, parked = False, park = "", exit = "", debt = "0"):
        self.license_num = license_num
        self.size = size
        self.owner = owner
        self.parked = parked
        self.park_time = park
        self.exit_time = exit
    
    def __repr__(self):
        str_license = "License number: " + self.license_num + "\n"
        str_size = "Size: " + str(self.size) + "\n"
        str_own = "Owner: " + self.owner + "\n"
        
        if (self.parked == True):
            str_parked = "Parked: Yes\n"
        else:
            str_parked = "Parked: No\n"
        
        str_park_time = "Park time: " + self.park_time + "\n"
        
        if (self.exit_time != ""):
            str_exit_time = "Exit time: " + self.exit_time + "\n"
            current_time = ""
            delta = relativedelta(parse(self.exit_time), parse(self.park_time))
            time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes.")
            
        else:
            str_exit_time = ""
            current_timestamp = dt.datetime.now().isoformat()
            current_time = (f"Current time: {current_timestamp}\n")
            delta = relativedelta(parse(current_timestamp), parse(self.park_time))
            time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes.")

        return (str_license + str_size + str_own + str_parked + str_park_time + str_exit_time + current_time + time_parked + "\n")

def write_history_file(garage):
    parking_garage = list(garage.values())
    file = input_file("Which file do you want to save to (.csv)? ", "w")
    for car in parking_garage:
        lines = re.sub(r"[\([{})\]]", "", repr(car).strip()).split("\n")
        lines.pop()
        file.write(",".join(lines) + "\n")

def read_from_file(parked_list, unparked_list):
    parked_cars = parked_list
    unparked_cars= unparked_list
    
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
        car = Car(license_num, size, owner, parked_bool, park_time)
        if (parked_bool == True):
            parked_cars.update({license_num : car})
        elif (parked_bool == False):
            unparked_cars.update({license_num : car})
    
    return parked_cars,unparked_cars
        
def park(unparked_list):
    unparked_cars = unparked_list
    
    status = input_type("Have you been parked before? (Yes/No) ", str)
    if (status == "Yes"):
        license_num = license_input("Enter the license number of the car: ")
        park_timestamp = dt.datetime.now().isoformat()
        if (license_num in unparked_cars):
            car = unparked_cars.get(license_num)
            car.parked= True
            car.park = park_timestamp
            car.exit = ""
            return car
    elif (status == "No"):
        license_num = license_input("Enter the license number of the car: ")
        size = size_input("Enter the size of the car (1/2/3): ")
        owner = input_type("Enter the name of the owner of the car: ", str)
        park_timestamp = dt.datetime.now().isoformat()
        
        return Car(license_num, size, owner, True, park_timestamp)

def unpark(parked_list, unparked_list):
    parked_cars = parked_list
    unparked_cars= unparked_list
    
    num = exit_input("Enter the license number of your car: ", parked_cars)
    car = parked_cars[num]
    car.parked = False
    car.exit_time = dt.datetime.now().isoformat()
    
    unparked_list.update({num : car})
    del parked_cars[num]
    print("Thank you for parking!")
    
    return parked_cars,unparked_cars

def append_to_list(parked_list, unparked_list):    
    parked_cars = parked_list
    unparked_cars= unparked_list
    
    car = park(unparked_cars)
    num = car.license_num
    
    parked_cars.update({num : car})
    print(re.sub(r"[\([{})\]]", "", repr(parked_cars.get(num))))
    
    return parked_cars,unparked_cars

def account(parked_list, unparked_list):
    parked_cars = parked_list
    unparked_cars= unparked_list
    

def clear_terminal():
    if (platform.system() == "Linux"):
        os.system('clear')
    elif (platform.system() == "Windows"):
        os.system('cls')

def main():
    parking_garage = {}
    unparked_cars = {}
    
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
                parking_garage,unparked_cars = append_to_list(parking_garage, unparked_cars)
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
                pass
            case "4":
                parking_garage,unparked_cars = read_from_file(parking_garage, unparked_cars)
            case "5":
                parking_garage,unparked_cars = unpark(parking_garage, unparked_cars)
                input("Press Enter to go back")
            case "6":
                write_history_file(parking_garage)
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