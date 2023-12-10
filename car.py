from typed_input import *
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
class Car():
    def __init__(self, license_num, size, owner, park_time, exit_time, debt = 0):
        self.license_num = license_num
        self.size = size
        self.owner = owner
        self.park_time = park_time
        self.exit_time = exit_time
        self.debt = debt
    
    def __repr__(self):
        str_license = "License number: " + self.license_num + "\n"
        str_size = "Size: " + str(self.size) + "\n"
        str_own = "Owner: " + self.owner + "\n"
        str_debt = "Debt: " + str(self.debt) 
        str_park_time = "Park time: " + self.park_time + "\n"        
        str_exit_time = "Exit time: " + self.exit_time + "\n"
        delta = relativedelta(parse(self.exit_time), parse(self.park_time))
        time_parked = (f"The car has been parked for {delta.years} year(s), {delta.months} months, {delta.days} days, {delta.hours} hours, {delta.minutes} minutes. \n")
        return (str_license + str_size + str_own + str_park_time + str_exit_time + time_parked + str_debt)

    def account(self, entry_dict, exit_dict):
        entry_list = list(entry_dict[self.license_num])
        exit_list = list(exit_dict[self.license_num]) 
        self.calc_debt(entry_list, exit_list)
        print("1. Check debts")
        print("2. Pay debts")
        print("3. Go back")
        choice = size_input("What would you like to do? (1/2/3)", int)
        match choice:
            case 1:
                self.check_debt(entry_dict, exit_dict)
            case 2:
                self.pay_debt(entry_list, exit_list)
            case 3:
                pass
                
    
    def check_debt(self, entry_dict, exit_dict):
        pass
        
        
    def pay_debt(self, entry_list, exit_list):
        self.calc_debt(entry_list, exit_list)

    def calc_debt(self, entry_list, exit_list):
        # Needs changing to be absolute (modulo) not hardcoded 1/0
        if len(exit_list) == len(entry_list):
            for entry_time, exit_time in zip(entry_list, exit_list):
                time = entry_time.split(";")[1]
                time1 = time.split(":")
                input(time1)
                time2 = exit_time.split(":")
                if time1[1] > time2[1]:
                    diff_hours = int(time1[1]) - (time2[1])
                    diff_hours = 24 - diff_hours
                else:
                    diff_hours = time1[1] - time2[1]
            
                time_parked = diff_hours +  time1[0] * 24   
        else:
            for entry_time in entry_list:
                time1 = entry_time.split[":"]
                time2 = time_input("What time is it now? (HH:MM)")
                if time1[1] > time2:
                    diff_hours = time1[1] - time2
                    diff_hours = 24 - diff_hours
                else:
                    diff_hours = time1 - time2
                time_parked = diff_hours +  time1[0] * 24