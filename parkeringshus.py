import sys
import os
import time
import datetime as dt
from typed_input import input_type, input_file, size_input

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
            str_parked = "Yes\n"
        else:
            str_parked = "No\n"
        str_park_time = "Park time: " + self.park_time + "\n"
        if self.exit_time != "":
            str_exit_time = self.exit_time + "\n"
        else:
            str_exit_time = ""
        return (str_license + str_size + str_own + str_parked + str_park_time + str_exit_time)
    
    def park(self, parked, park):
        """Parks the car in the garage, enters the time and changes the parking status

        Args:
            parked (bool): _description_
            park (_type_): _description_
        """
        
        pass
    
    def exit(self, parked, exit):
        pass

def read_from_file():
    pass

def park():
    license_num = input_type("Enter the license number of the car: ", str)
    size = size_input("Enter the size of the car (1/2/3): ", str)
    owner = input_type("Enter the name of the owner of the car: ", str)
    
    park_timestamp = dt.datetime.now().isoformat()
    
    return Car(license_num, size, owner, True, park_timestamp)

def append_to_list():    
    car = park()
    num = car.license_num
    garage = {}
    
    garage.update({num : car})
    print(garage)
    return garage

def menu():
    parking_garage = {}
    print("Welcome to the parking garage! Please choose one of the options below")

    while True:
        os.system('clear')
        print("Welcome to the parking garage! Please choose one of the options below")
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
            case "2":
                try:
                    print(parking_garage)
                    print("Press any key to go back")
                    os.system('read -n 1 -s')
                except:
                    print("There are currently no cars parked in the garage")        
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                exit()
        
        time.sleep(1)

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