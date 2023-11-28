import sys
import os
import time
import datetime as dt
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from typed_input import input_type, input_file, size_input, license_input, exit_input

class Car():
    def __init__(self, license_num, size, owner, parked = False, park = "", exit = ""):
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
        
        if self.parked == True:
            str_parked = "Parked: Yes\n"
        else:
            str_parked = "Parked: No\n"
        
        str_park_time = "Park time: " + self.park_time + "\n"
        
        if self.exit_time != "":
            str_exit_time = "Exit time: " + self.exit_time + "\n"
            current_time = ""
            delta = relativedelta(parse(self.exit_time), parse(self.park_time))
            time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes.")
            
        else:
            str_exit_time = ""
            current_timestamp = dt.datetime.now().isoformat()
            current_time = (f"Current time: {current_timestamp} \n")
            delta = relativedelta(parse(current_timestamp), parse(self.park_time))
            time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes.")

        return (str_license + str_size + str_own + str_parked + str_park_time + str_exit_time + current_time + time_parked)

def write_history_file(garage):
    parking_garage = garage
    filename = "garage.csv"

    with open(filename, "w", encoding="utf-8") as file:
        for bil in parking_garage.items():
            file.write(str(bil))

        

def read_from_file():
    file = input_file("Input the filename: ", str)

def park():
    license_num = license_input("Enter the license number of the car: ")
    size = size_input("Enter the size of the car (1/2/3): ", str)
    owner = input_type("Enter the name of the owner of the car: ", str)
    
    park_timestamp = dt.datetime.now().isoformat()
    
    return Car(license_num, size, owner, True, park_timestamp)

def unpark(parked_cars, unparked_cars):
    parking_list = parked_cars
    unparked_list = unparked_cars
    num = exit_input("Enter the license number of your car: ", parking_list)
    car = parking_list[num]
    car.parked = False
    car.exit_time = dt.datetime.now().isoformat()
    
    unparked_list.update({num : car})
    del parking_list[num]
    print("Thank you for parking!")
    return parking_list,unparked_list
    

def append_to_list():    
    car = park()
    num = car.license_num
    garage = {}
    
    garage.update({num : car})
    print(garage)
    return garage

def menu():
    parking_garage = {}
    unparked_cars = {}
    
    print("Welcome to the parking garage! Please choose one of the options below")
    while True:
        os.system('clear')
        print("1. Enter the garage")
        print("2. View car information")
        print("3. View account")
        print("4. Load file")
        print("5. Exit the garage")
        print("6. Exit the program")
        
        answer = input()
        
        match answer:
            case "1":
                parking_garage = append_to_list()
                print("Press any key to go back")
                os.system('read -n 1 -s')
            case "2":
                try:
                    license_num = license_input("Enter the license number of the car: \n")
                    if len(list(parking_garage)) > 0 and license_num in parking_garage:
                        print(parking_garage[license_num])
                    else:
                        if len(list(unparked_cars)) > 0 and license_num in unparked_cars:
                            print(unparked_cars[license_num])
                        else:
                            raise Exception
                except:
                    print("There are currently no cars parked in the garage and your car has never been parked in the garage")  
                
                print("Press any key to go back")
                os.system('read -n 1 -s')
            case "3":
                pass
            case "4":
                read_from_file()
            case "5":
                parking_garage,unparked_cars = unpark(parking_garage, unparked_cars)
                print("Press any key to go back")
                os.system('read -n 1 -s')
            case "6":
                write_history_file(parking_garage)
                exit()

def main():
    menu()

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