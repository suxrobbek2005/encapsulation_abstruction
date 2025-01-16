from colorama import Style, Fore


class Animal:

    def __init__(self, kind, age):

        self.kind = kind
        self.age = age

    def general_information(self):
        """Hayvonlarni umumiy malumotlarni aniqalab beradi"""

        return f"{Fore.LIGHTCYAN_EX}Turi: {self.kind}, Yoshi: {self.age} yil{Style.RESET_ALL}"
    
class Beast(Animal):

    def __init__(self, kind, age, hunting_method):
        super().__init__(kind, age)

        self.hunting_method = hunting_method

    def Hunt(self):
        """Yirqich hayvonlarning ov turini qaytarib beradi"""

        return f"{Style.DIM},{Fore.LIGHTRED_EX},{self.kind},Hayvoning ov turi -->{self.hunting_method},{Style.RESET_ALL}"

class Herbivore(Animal):

    def __init__(self, kind, age, feed_type):
        super().__init__(kind, age)

        self.feed_type = feed_type

    def Feeds(self):
        """O'txo'r hayvonlarning ozuqa turini qaytaradi"""

        return f"{Fore.LIGHTRED_EX},{self.kind},Hayvoning ozuqa turi --> {self.feed_type}, {Fore.RESET}"
    
if __name__ == "__main__":
    animals = []

while True:

    print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}== Xizmat turalari == {Style.RESET_ALL}\n")
    print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}1 --> Yirtqich hayvonlar qo'shish:{Style.RESET_ALL}")
    print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}2 --> O'txo'r hayvonlar qo'shish:{Style.RESET_ALL}")
    print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}3 --> Barcha hayvonlarni ko'rish:{Style.RESET_ALL}")
    print(f"{Style.DIM},{Fore.LIGHTGREEN_EX}4 --> Dasturdan chiqish:{Style.RESET_ALL}")

    choise_menu = int(input(f"{Style.DIM},{Fore.MAGENTA}Xizamt turlarini tanlang (1-4){Style.RESET_ALL}"))

    if choise_menu == 1:

        kind = input(f"{Style.DIM},{Fore.RED}Hayvoning turini kiriting{Style.RESET_ALL} ").title()
        age = int(input(f"{Style.DIM},{Fore.RED}Hayvoning turini kiriting{Style.RESET_ALL} "))
        hunt = input(f"{Style.DIM},{Fore.RED}Hayvoning ov qilish turi kiriting{Style.RESET_ALL} ").capitalize()

        animals.append(Herbivore(kind, age, hunt))

        print(f"{Style.DIM},{Fore.LIGHTGREEN_EX} {kind}Muvaffaqiyatli qo'shildi:{Style.RESET_ALL}")

    elif choise_menu == 2:

        kind = input(f"{Style.DIM},{Fore.RED}Hayvoning turini kiriting{Style.RESET_ALL} ").title()
        age = int(input(f"{Style.DIM},{Fore.RED}Hayvoning turini kiriting{Style.RESET_ALL} "))
        feed = input(f"{Style.DIM},{Fore.RED}Hayvoning ov qilish turi kiriting{Style.RESET_ALL} ").capitalize()

        animals.append(Herbivore(kind, age, feed))

        print(f"{Style.DIM},{Fore.LIGHTGREEN_EX} {kind}Muvaffaqiyatli qo'shildi:{Style.RESET_ALL}")

    elif choise_menu == 3:

        if not animals:

            print(f"{Style.DIM},{Fore.LIGHTCYAN_EX} {kind}Birorta ham hayvon qo'shilmagan:{Style.RESET_ALL}")

        else:
            print(f"{Fore.LIGHTMAGENTA_EX}== Barcha hayvonlar =={Style.RESET_ALL}")

            for hayvon in animals:
                print(hayvon.umumiy_malumot())
                if isinstance(hayvon, Beast()):
                        print(hayvon, Herbivore())
                elif isinstance(hayvon, hunt):
                        print(hayvon, feed)
    
    elif choise_menu == 4:

        print(f"{Fore.LIGHTRED_EX}Dasturdan chiqildi!{Style.RESET_ALL}")
        break

    else:
        print(f"{Fore.RED}Noto'g'ri tanlov! Qayta urinib ko'ring.{Style.RESET_ALL}")



