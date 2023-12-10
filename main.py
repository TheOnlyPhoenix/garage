import sys
import os
import platform
from car import Car
from garage import Garage
from typed_input import *
from collections import defaultdict
from itertools import chain
            
def write_history_file(garage, day):
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
        del lines[len(lines) - 2]
        file.write(",".join(lines) + "\n")
        
        for value in garage.entry_dict[car.license_num]:
            entry_list.append(value)
        for value in garage.exit_dict[car.license_num]:
            exit_list.append(value)   
        while e == True:
            file2.write(car.license_num + ",")
            e = False
        for i in range(len(entry_list)):
            line1 = re.sub(r"[\([{})\]]", "", entry_list[i])
            line2 = re.sub(r"[\([{})\]]", "", exit_list[i])
            print(lines)
            file2.write(",".join([line1,line2]))
        file2.write("\n")
            
def read_from_file(garage):   
    license_num = ""
    file = input_file("Which file do you want to load from (.csv)? ", "r")
    try:
        file2 = open("history.csv", "r", encoding="utf-8")
    except:
        pass    
    
    lines = file.readlines()
    for line in lines:
        split_line = line.split(",")
        license_num = split_line[0][len("License number: "):]
        size = split_line[1][len("Size: "):]
        owner = split_line[2][len("Owner: "):]
        park_time = split_line[3][len("Park time: "):]
        exit_time = split_line[4][len("Exit time: "):]
        debt = split_line[5][len("Debt: "):].strip()
        car = Car(license_num, size, owner, park_time, exit_time, debt)
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
    for entry_combo, exit_time in zip(garage.entry_dict[num], garage.exit_dict[num]):
        print(garage.entry_dict[num])
        print(garage.exit_dict[num])
        input(entry_combo)
        day,entry_time = entry_combo.split(";")
        
        message = "Day parked: " + day + "\nEntry time: " + entry_time + "\nExit time :" + exit_time
        print(message)
        

def clear_terminal():
    if (platform.system() == "Linux"):
        os.system('clear')
    elif (platform.system() == "Windows"):
        os.system('cls')

def menu(garage):
    day = str(input_type("What day of the month is it? ", int))
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
                garage.append_to_dict(day)
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
                car = garage.parked_dict.get(license_num)
                while True:
                    if (len(list(garage.parked_dict)) > 0 and license_num in garage.parked_dict):
                        car = garage.parked_dict.get(license_num)
                        car.account(garage.entry_dict, garage.exit_dict)
                        break
                    else:
                        if (len(list(garage.unparked_dict)) > 0 and license_num in garage.unparked_dict):
                            car = garage.unparked_dict.get(license_num)
                            car.account(garage.entry_dict, garage.exit_dict)
                            break
                        else:
                            print("Your car isn't currently parked and has never been parked in the garage. Please try again.")
                            continue
            case "5":
                garage = read_from_file(garage)
            case "6":
                write_history_file(garage, day)
                exit()

def main():
    garage = Garage()
    day_list = []
    
    menu(garage)
    

    

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