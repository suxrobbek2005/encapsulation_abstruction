from colorama import Fore, Style


class Cars:

    def __init__(self, name, marka, price):
        
        self.__name = name
        self.__marka = marka
        self.__price = price

    def get_price(self):

        return self.__price
    
    def set__price(self, new_price):

        if new_price < 0:

            print(f"{Style.DIM},{Fore.LIGHTRED_EX},Narx manfiy bo'lishi mumkin emas! {Style.RESET_ALL}")

        else:

            self.__price = new_price
            print(f"{Style.DIM},{Fore.BLUE} Narx muvaffaqiyatli {self.__price} o'zgartiridi  {Style.RESET_ALL}")
    
    def general_information(self):

        print(f"{Style.DIM},{Fore.GREEN},Nomi: {self.__name} MOdeli: {self.__marka} Narxi: {self.set__price}, {Style.RESET_ALL}")
    
car = Cars("Cobalt", "Chevrolet", 12000)
car = Cars("Jentra", "Chevrolet", 20000)
car = Cars("Malibu", "Chevrolet", 45000)
car = Cars("K5", "Kia", 43000)
car = Cars("Sportage", "Kia", 38000)

car.general_information()
car.set__price(14000)
car.set__price(30000)
car.set__price(50000)
car.set__price(48000)
car.set__price(40000)
car.set__price(-34000)

print(f"{Style.DIM},{Fore.LIGHTYELLOW_EX} Yangi narx: {car.get_price}, {Style.RESET_ALL}")


        
