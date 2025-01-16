from colorama import Fore, Style

class Staff:

    def __init__(self, staff_name, staff_surname, staff_age, staff_rank):
        
        self.__staff_name = staff_name
        self.__staff_surname = staff_surname
        self.__staff_age = staff_age
        self.__staff_rank = staff_rank

   
    def get_staff_name(self):
        return self.__staff_name

    def get_staff_surname(self):
        return self.__staff_surname

    def get_staff_age(self):
        return self.__staff_age

    def get_staff_rank(self):
        return self.__staff_rank

    
    def set_staff_name(self, new_staff_name):
        if new_staff_name.strip():
            self.__staff_name = new_staff_name
        else:
            print(f"{Fore.RED}Ism bo'sh bo'lmasligi kerak!{Style.RESET_ALL}")

    def set_staff_surname(self, new_staff_surname):
        if new_staff_surname.strip():
            self.__staff_surname = new_staff_surname
        else:
            print(f"{Fore.RED}Familiya bo'sh bo'lmasligi kerak!{Style.RESET_ALL}")

    def set_staff_age(self, new_staff_age):
        if new_staff_age > 0:
            self.__staff_age = new_staff_age
        else:
            print(f"{Fore.RED}Yosh musbat bo'lishi kerak!{Style.RESET_ALL}")

    def set_staff_rank(self, staff_new_rank):
        if staff_new_rank.strip():
            self.__staff_rank = staff_new_rank
        else:
            print(f"{Fore.RED}Lavozim bo'sh bo'lmasligi kerak!{Style.RESET_ALL}")


print(f"\n{Fore.CYAN}== Xodim ma'lumotlarini kiriting =={Fore.RESET}")
name = input(f"{Fore.YELLOW}Ism kiriting: {Fore.RESET}")
surname = input(f"{Fore.YELLOW}Familiya kiriting: {Fore.RESET}")
age = int(input(f"{Fore.YELLOW}Yosh kiriting: {Fore.RESET}"))
rank = input(f"{Fore.YELLOW}Lavozim kiriting: {Fore.RESET}")


employe = Staff(name, surname, age, rank)


print(f"{Fore.LIGHTYELLOW_EX}\n== Kiritilgan xodim ma'lumotlari =={Style.RESET_ALL}")
print(f"{Fore.MAGENTA}Ism: {employe.get_staff_name()}")
print(f"Familiya: {employe.get_staff_surname()}")
print(f"Yosh: {employe.get_staff_age()}")
print(f"Lavozim: {employe.get_staff_rank()}")


print(f"{Fore.LIGHTYELLOW_EX}\n== Ma'lumotlarni yangilash =={Fore.RESET}")
new_name = input(f"{Fore.GREEN}Yangi ism kiriting: {Fore.RESET}")
employe.set_staff_name(new_name)

new_surname = input(f"{Fore.GREEN}Yangi familiya kiriting: {Fore.RESET}")
employe.set_staff_surname(new_surname)

new_age = int(input(f"{Fore.GREEN}Yangi yosh kiriting: {Fore.RESET}"))
employe.set_staff_age(new_age)

new_rank = input(f"{Fore.GREEN}Yangi lavozim kiriting: {Fore.RESET}")
employe.set_staff_rank(new_rank)


print(f"{Fore.LIGHTYELLOW_EX}\n== Yangilangan ma'lumotlar =={Fore.RESET}")
print(f"{Fore.MAGENTA}Ism: {employe.get_staff_name()}")
print(f"Familiya: {employe.get_staff_surname()}")
print(f"Yosh: {employe.get_staff_age()}")
print(f"Lavozim: {employe.get_staff_rank()}")
