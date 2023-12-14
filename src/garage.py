import re
from car import Car
from collections import defaultdict
from gui_input import *

class Garage:
    def __init__(self):
        self.parked_dict = {}
        self.entry_dict = defaultdict(list)
        self.exit_dict = defaultdict(list)
    
    # def park(self, date):    
    #     print("Note: You can only park from 00:00 until 23:59, and for a maximum of 24 Hours")
    #     status = input_type("Have you been parked before? (Yes/No) ", str)
    #     while True:
    #         if (status == "Yes"):
    #             license_num = license_input("Enter the license number of the car (ABC123): ")
    #             entry_time = time_input("Which time did you enter the garage? (HH:MM) ")
    #             exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
    #             entry_time, exit_time = self.check_times(entry_time, exit_time)
    #             if (license_num in self.parked_dict):
    #                 car = self.parked_dict[license_num]
    #                 date_and_entry_time = date + ";" + entry_time
    #                 self.entry_dict[license_num].append(date_and_entry_time)
    #                 self.exit_dict[license_num].append(exit_time)
    #                 return car, entry_time, exit_time
    #             else:
    #                 print("The license number you entered has never been parked here. Please try again. ")
    #                 continue
    #         elif (status == "No"):
    #             license_num = license_input("Enter the license number of the car (ABC123): ")
    #             #size = size_input("Enter the size of the car (Small - 1 | Medium - 2 | Large - 3): ")
    #             owner = input_type("Enter the name of the owner of the car: ", str)
    #             entry_time = time_input("Which time did you enter the garage? (HH:MM) ")
    #             exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
    #             entry_time, exit_time = self.check_times(entry_time, exit_time)
    #             date_and_entry_time = date + ";" + entry_time
    #             self.entry_dict[license_num].append(date_and_entry_time)
    #             self.exit_dict[license_num].append(exit_time)
    #             return Car(license_num, 1, owner), entry_time, exit_time
    #         else:
    #             status = input("You did not enter \"Yes\" or \"No\". Please try again: ")

    def append_to_dict(self, num, entry_time, exit_time):    
        car, entry_time, exit_time = self.park(1)
        num = car.license_num
        self.parked_dict.update({num : car})
        park_hours, park_minutes = car.calc_debt(entry_time, exit_time, True)
        print(re.sub(r"[\([{})\]]", "", repr(self.parked_dict.get(num))))
        car.park_time = park_hours + ":" + park_minutes
        print("Time parked: " + car.park_time)
        
    def check_times(self, entry_time, exit_time):
        entry_split = entry_time.split(":")
        exit_split = exit_time.split(":")
        entry_minutes = entry_split[1]
        exit_minutes = exit_split[1]
        entry_hour = entry_split[0]
        exit_hour = exit_split[0]

        
        if int(entry_minutes) > 30 and int(entry_minutes) <= 59 and entry_hour == "23":
            entry_minutes = "59"
            entry_hour = "23"
            return_entry = entry_hour + ":" + entry_minutes 
        elif int(entry_minutes) > 30 and int(entry_minutes) <= 60:
            entry_minutes = "00"
            entry_hour = str(int(entry_hour) + 1)
            return_entry = entry_hour + ":" + entry_minutes
        elif int(entry_minutes) > 00 and int(entry_minutes) <= 30:
            entry_minutes = "30"
            entry_hour = entry_hour
            return_entry = entry_hour + ":" + entry_minutes
        elif entry_minutes == "00":
            return_entry = entry_hour + ":" + entry_minutes 
            
        if int(exit_minutes) > 30 and int(exit_minutes) <= 59 and exit_hour == "23":
            exit_minutes = "59"
            exit_hour = "23"
            return_exit = exit_hour + ":" + exit_minutes
        elif int(exit_minutes) > 30 and int(exit_minutes) <= 60:
            exit_minutes = "00"
            exit_hour = str(int(exit_hour) + 1)
            return_exit = exit_hour + ":" + exit_minutes
        elif int(exit_minutes) > 00 and int(exit_minutes) <= 30:
            exit_minutes = "30"
            exit_hour = exit_hour
            return_exit = exit_hour + ":" + exit_minutes
        elif exit_minutes == "00":
            return_exit = exit_hour + ":" + exit_minutes
        
        max_parking_minutes = 24 * 60
        entry_time_minutes = int(entry_minutes) + int(entry_hour) * 60
        exit_time_minutes = int(exit_minutes) + int(exit_hour) * 60
        
        total_parking_minutes = exit_time_minutes - entry_time_minutes
        while True:
            if total_parking_minutes > max_parking_minutes:
                print("The parking time exceeds 24 hours. Please enter a valid time.")
                entry_time = time_input("Which time did you enter the garage? (HH:MM)")
                exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
            else:
                return return_entry, return_exit