import os
import platform
from typed_input import *
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

class Car():
    def __init__(self, license_num, size, owner, park_time = "", debt = 0):
        self.license_num = license_num
        self.size = size
        self.owner = owner
        self.park_time = park_time
        self.debt = debt
    
    def pay_debt(self):
        choice = input(f"Your total debt is {self.debt}. Do you wish to pay it now? (Yes/No)")
        match choice:
            case "Yes":
                amount = input_type("How much do you wish to pay?", int)
                self.debt = self.debt - amount
                self.park_time = ""
                print(f"Thank you for paying! Your remaining debt is {self.debt}")
            case "No":
                print("Okay. Beware of dangers on the roads :)")
            case _:
                print("You did not enter a valid answer. Please try again.")
                self.pay_debt()
        clear_terminal()
    def __repr__(self):
        str_license = "License number: " + self.license_num + "\n"
        str_size = "Size: " + str(self.size) + "\n"
        str_own = "Owner: " + self.owner + "\n"
        str_debt = "Debt: " + str(self.debt) 
        #delta = relativedelta(parse(self.exit_time), parse(self.park_time))
        #time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes. \n")
        return (str_license + str_size + str_own + str_debt)

    def account(self, entry_dict, exit_dict):
        entry_list = list(entry_dict[self.license_num])
        exit_list = list(exit_dict[self.license_num]) 
        park_hours, park_minutes = self.calc_debt(entry_list, exit_list, False)
        print("1. Check debts")
        print("2. Pay debts")
        print("3. Go back")
        choice = size_input("What would you like to do? (1/2/3)", int)
        match choice:
            case 1:
                self.check_debt(park_hours, park_minutes)
            case 2:
                self.pay_debt()
            case 3:
                pass

    def check_debt(self, park_hours, park_minutes):
        print(f"You have parked for a total of {park_hours} hours and {park_minutes} minutes.")
        print(f"Your total debt is {self.debt}")
        input("Press Enter to go back")
        clear_terminal()
        

    def calc_debt(self, entry, exit, single_list_bool):
        if single_list_bool == False:
            for entry_time, exit_time in zip(entry, exit):
                time = entry_time.split(";")[1]
                time1 = time.split(":")
                time2 = exit_time.split(":")

                time1_hours = time1[0]
                time1_minutes = time1[1]
                time2_hours = time2[0]
                time2_minutes = time2[1]

                time1_total_minutes = int(time1_hours) * 60 + int(time1_minutes)
                time2_total_minutes = int(time2_hours) * 60 + int(time2_minutes)
                total_minutes = time2_total_minutes - time1_total_minutes
                park_time_hours = total_minutes // 60
                park_time_minutes = total_minutes % 60
                debt_calc_time = total_minutes // 30
                self.debt = self.debt + (15 + self.size * 5) * debt_calc_time 
                if len(str(park_time_hours)) == 1:
                    park_time_hours = "0" + str(park_time_hours)
                else:
                    park_time_hours = str(park_time_hours)
                if len(str(park_time_minutes)) == 1:
                    park_time_minutes = "0" + str(park_time_minutes)
                else:
                    park_time_minutes = str(park_time_minutes)
                return park_time_hours, park_time_minutes
        elif single_list_bool == True:
                time1 = entry.split(":")
                time2 = exit.split(":")

                time1_hours = time1[0]
                time1_minutes = time1[1]
                time2_hours = time2[0]
                time2_minutes = time2[1]

                time1_total_minutes = int(time1_hours) * 60 + int(time1_minutes)
                time2_total_minutes = int(time2_hours) * 60 + int(time2_minutes)
                total_minutes = time2_total_minutes - time1_total_minutes
                if self.park_time != "":
                    park_time_hours = total_minutes // 60 + int(self.park_time.split(":")[0])
                    park_time_minutes = total_minutes % 60 + int(self.park_time.split(":")[1])
                else:
                    park_time_hours = total_minutes // 60 
                    park_time_minutes = total_minutes % 60
                debt_calc_time = total_minutes // 30
                self.debt = self.debt + (15 + self.size * 5) * debt_calc_time 
                if len(str(park_time_hours)) == 1:
                    park_time_hours = "0" + str(park_time_hours)
                else:
                    park_time_hours = str(park_time_hours)
                if len(str(park_time_minutes)) == 1:
                    park_time_minutes = "0" + str(park_time_minutes)
                else:
                    park_time_minutes = str(park_time_minutes)
                return park_time_hours, park_time_minutes
def clear_terminal():
    if (platform.system() == "Linux"):
        os.system('clear')
    elif (platform.system() == "Windows"):
        os.system('cls')