from colorama import Style, Fore


class Cars:

    def __init__(self, marka, color, price, model, year_of_issue):

        self.marka = marka
        self.color = color
        self.__price = price
        self.__model = model
        self.__year_of_issue = year_of_issue

    def get_price_and_year_issue(self):

        return self.__price, self.__year_of_issue
    
    def set_price(self, new_price):

        if new_price < 0:

            print(f"{Style.DIM},{Fore.GREEN}Narx manfiy bo'lishi mumkin emas! {Style.RESET_ALL}")

        else:
            
            self.__price = new_price
            print(f"{Style.DIM},{Fore.LIGHTMAGENTA_EX}Narx muvaffaqiyatli {self.__price} qo'shildi")

    def set_year_of_issues(self, new_year_issues):

        self.__year_of_issue = new_year_issues
        print(f"{Style.DIM},{Fore.LIGHTRED_EX},{self.__year_of_issue} - yil muvaffaqiyatli qo'shildi {Style.RESET_ALL}")

    def general_information(self):

        print(f"{Style.DIM},{Fore.LIGHTRED_EX}Nomi: {self.marka} Modeli: {self.__model} Rangi: {self.color} Narxi: {self.__price} Ishlab chiqarilgan yili: {self.__year_of_issue}, {Style.RESET_ALL}")


car = Cars("Cobalt", "Qora", 12000, "Chevrolet", 2022)
car = Cars("Jentra", "Oq", 22000, "Chevrolet", 2021)
car = Cars("Malibu", "Mokriy asfalt", 45000, "Chevrolet", 2024)
car = Cars("k5", "Qora", 43000, "Kia", 2024)
car = Cars("Matiz", "Metalika", 3000, "", 2009)
car = Cars("Tiko", "Kuk", 1000, "Chevrolet", 2003)

print(f"{Style.DIM},{Fore.LIGHTRED_EX}== Yangilangan narxlar =={Style.RESET_ALL}")
car.general_information
car.set_price(14000)
car.set_price(24000)
car.set_price(47000)
car.set_price(45000)
car.set_price(-2000)

print(f"{Fore.LIGHTMAGENTA_EX}== Yangilangan yillar == {Fore.RESET}")
car.set_year_of_issues(2023)
car.set_year_of_issues(2022)
car.set_year_of_issues(2025)
car.set_year_of_issues(2025)
car.set_year_of_issues(2005)
car.set_year_of_issues(2001)
