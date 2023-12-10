import re
from car import Car
from collections import defaultdict
from typed_input import *

class Garage:
    def __init__(self):
        self.parked_dict = {}
        self.entry_dict = defaultdict(list)
        self.exit_dict = defaultdict(list)
    
    def park(self):    
        print("Note: You can only park from 00:00 until 23:59, and for a maximum of 24 Hours")
        status = input_type("Have you been parked before? (Yes/No) ", str)
        while True:
            if (status == "Yes"):
                license_num = license_input("Enter the license number of the car (ABC123): ")
                entry_time = time_input("Which time did you enter the garage? (HH:MM)")
                exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
                entry_time, exit_time = self.round_times(entry_time, exit_time)
                if (license_num in self.parked_dict):
                    car = self.parked_dict.get(license_num)
                    car.park = entry_time
                    car.exit = exit_time
                    return car
                else:
                    print("The license number you entered has never been parked here. Please try again. ")
                    continue
            elif (status == "No"):
                license_num = license_input("Enter the license number of the car (ABC123): ")
                size = size_input("Enter the size of the car (Small - 1 | Medium - 2 | Large - 3): ")
                owner = input_type("Enter the name of the owner of the car: ", str)
                entry_time = time_input("Which time did you enter the garage? (HH:MM) ")
                exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
                entry_time, exit_time = self.check_times(entry_time, exit_time)
                return Car(license_num, size, owner, entry_time, exit_time)
            else:
                status = input("You did not enter \"Yes\" or \"No\". Please try again: ")

    def append_to_dict(self, day):    
        car = self.park()
        num = car.license_num
        day_and_entry_time = day + ";" + car.park_time
        exit_time = car.exit_time
        self.entry_dict[num].append(day_and_entry_time)
        self.exit_dict[num].append(exit_time)
        self.parked_dict.update({num : car})
        print(re.sub(r"[\([{})\]]", "", repr(self.parked_dict.get(num))))
        
    def check_times(self, entry_time, exit_time):
        entry_split = entry_time.split(":")
        exit_split = exit_time.split(":")
        entry_minutes = int(entry_split[1])
        exit_minutes = int(exit_split[1])
        entry_hour = entry_split[0]
        exit_hour = exit_split[0]

        
        if entry_minutes > 30 and entry_minutes <= 60:
            entry_minutes = "00"
            entry_hour = str(int(entry_hour) + 1)
            return_entry = entry_hour + ":" + entry_minutes
        elif entry_minutes > 00 and entry_minutes <= 30:
            entry_minutes = "30"
            entry_hour = str(int(entry_hour) + 1)
            return_entry = entry_hour + ":" + entry_minutes
            
        if exit_minutes > 30 and exit_minutes <= 60:
            exit_minutes = "00"
            exit_hour = str(int(exit_hour) + 1)
            return_exit = exit_hour + ":" + exit_minutes
        elif exit_minutes > 00 and exit_minutes <= 30:
            exit_minutes = "30"
            exit_hour = str(int(exit_hour) + 1)
            return_exit = exit_hour + ":" + exit_minutes
        
        max_parking_minutes = 24 * 60
        entry_time_minutes = entry_minutes + entry_hour * 60
        exit_time_minutes = exit_minutes + exit_hour * 60
        
        total_parking_minutes = exit_time_minutes - entry_time_minutes
        while True:
            if total_parking_minutes > max_parking_minutes:
                print("The parking time exceeds 24 hours. Please enter a valid time.")
                entry_time = time_input("Which time did you enter the garage? (HH:MM)")
                exit_time = time_input("Which time did you exit the garage? (HH:MM) ")
            else:
                return return_entry, return_exit