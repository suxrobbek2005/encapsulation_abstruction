from colorama import Style, Fore


class Phones:

    def __init__(self):

        self.contact = {}

    def AddContact(self):
        "Yangi telefon raqam qo'shish"

        user_name = input(f"{Style.DIM},{Fore.LIGHTGREEN_EX}Ismingizni kiriting: {Style.RESET_ALL} ")
        user_number = int(input(f"{Style.DIM},{Fore.LIGHTGREEN_EX}Telefon raqamingizni kiriting: {Style.RESET_ALL} "))

        if user_name in self.contact:

            print(f"{Fore.RED},{user_name} allaqachon kontaktlar ro'yxatida mavjud!{Style.RESET_ALL}")
        else:

            self.contact[user_name] = user_number
            print(f"{Fore.LIGHTCYAN_EX}{user_name} muvaffaqiyatli qo'shildi!{Style.RESET_ALL}")

    def get_contact(self):
        "Telefon raqamlarni izlash va topib berish"

        name = input(f"{Style.DIM},{Fore.LIGHTGREEN_EX}Raqam egasini kiriting: {Style.RESET_ALL} ")

        if name in self.contact:

            user_number = self.contact[name]
            print(f"{Fore.LIGHTCYAN_EX}{name}: {user_number}{Style.RESET_ALL}")

        else:

            print(f"{Fore.RED}{name} kontaktlar ro'yxatida topilmadi!{Style.RESET_ALL}")

    def show_all_contacts(self):
        "Barcha kontaktlarni ko'rsatish"

        if not self.contact:

            print(f"{Fore.RED}Kontaktlar ro'yxati bo'sh!{Style.RESET_ALL}")

        else:

            print(f"{Fore.LIGHTMAGENTA_EX}Kontaktlar ro'yxati:{Style.RESET_ALL}")

            for name, phone in self.contact.items():

                print(f"{Fore.LIGHTYELLOW_EX}{name}: {phone}{Style.RESET_ALL}")



number = Phones()

while True:

    print(f"\n{Fore.LIGHTGREEN_EX}1. Yangi kontakt qo'shish\n"
          f"2. Kontaktni olish\n"
          f"3. Barcha kontaktlarni ko'rish\n"
          f"4. Chiqish{Style.RESET_ALL}")
    
    choise = input(f"{Fore.CYAN}Tanlovingizni kiriting (1-4): {Style.RESET_ALL} ")

    if choise == "1":

        number.AddContact()

    elif choise == "2":

        number.get_contact()

    elif choise == "3":

        number.show_all_contacts()

    elif choise == "4":

        print(f"{Fore.LIGHTRED_EX}Dasturdan chiqildi!{Style.RESET_ALL}")
        break

    else:

        print(f"{Fore.RED}Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.{Style.RESET_ALL}")
