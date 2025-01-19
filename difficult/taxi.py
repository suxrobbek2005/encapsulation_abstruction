from colorama import Fore, Style


class Taxi:

    def __init__(self, driver, car, price, direction, empty_place):

        self.driver = driver
        self.car = car
        self.__price = price
        self.__direction = direction 
        self.__empty_place = empty_place  

   
    def get_price(self):

        return f"price: {self.__price} so'm"

   
    def set_empty_place(self, new_place):

        if new_place < 0:

            print(f"{Fore.RED}Bo'sh joylar soni manfiy bo'lishi mumkin emas!{Style.RESET_ALL}")

        else:
            self.__empty_place = new_place

   
    def info(self):

        return (f"{Fore.GREEN}driver: {self.driver}, car: {self.car}, "
                f"{self.get_price()}, Yo'nalish: {self.__direction}, "
                f"Bo'sh joylar: {self.__empty_place}{Style.RESET_ALL}")


Taxi1 = Taxi("Ali", "Chevrolet Cobalt", 15000, "Toshkent-Samarqand", 3)
Taxi2 = Taxi("Vali", "Toyota Camry", 20000, "Toshkent-Farg'ona", 0)


print(Fore.YELLOW + "\n== Taxi haqida ma'lumotlar ==" + Style.RESET_ALL)
print(Taxi1.info())
print(Taxi2.info())


print(Fore.BLUE + "\n== Bo'sh joylarni yangilash ==" + Style.RESET_ALL)
Taxi1.set_empty_place(4)
Taxi2.set_empty_place(-1)  


print(Fore.YELLOW + "\n== Yangilangan Taxi malumotlari ==" + Style.RESET_ALL)
print(Taxi1.info())
print(Taxi2.info())
