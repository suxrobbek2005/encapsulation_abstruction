from colorama import Fore, Style


class Robot:

    def __init__(self, model, area):

        self.model = model
        self.area = area
        self.__charge_level = 100  
        self.__max_work_time = 8  
        self.__status = "Kutmoqda"  

    
    def get_charge_level(self):

        if self.__charge_level < 20:

            return f"{Fore.RED}Zaryadlash kerak! ({self.__charge_level}%)" + Style.RESET_ALL
        
        return f"Zaryad darajasi: {self.__charge_level}%"

   
    def set_work_time(self, new_time):

        if new_time > 12:

            print(f"{Fore.RED}Xatolik: Maksimal ish vaqti 12 soatdan oshmasligi kerak!{Style.RESET_ALL}")

        else:
            self.__max_work_time = new_time

    
    def get_status(self):

        if self.__status == "Kutmoqda":

            self.__charge_level = 100
            print(f"{Fore.BLUE}Status: {self.__status}. Zaryad darajasi avtomatik 100% ga o‘rnatildi.{Style.RESET_ALL}")

        return f"Status: {self.__status}"


robot = Robot("RBT-2025", "Toshkent")


print(Fore.YELLOW + "\nRobot haqida ma'lumot:" + Style.RESET_ALL)
print(f"Model: {robot.model}")
print(f"Hudud: {robot.area}")
print(robot.get_charge_level())
robot.set_work_time(10)
print(robot.get_status())
robot.set_work_time(14)  
