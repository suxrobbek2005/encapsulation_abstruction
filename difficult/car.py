from colorama import Fore, Style


class Car:

    def __init__(self, model, color, speed, price, fuel_type):

        self.model = model
        self.color = color
        self.__speed = speed  # Private
        self.__price = price  # Private
        self.__fuel_type = fuel_type  # Private

   
    def get_speed(self):

        return f"speed: {self.__speed} km/soat"

    
    def set_fuel_type(self, yangi_yoqilgi):

        self.__fuel_type = yangi_yoqilgi

    
    def info(self):

        return (f"{Fore.CYAN}Model: {self.model}, color: {self.color}, "
                f"{self.get_speed()}, price: {self.__price} so'm, "
                f"Yoqilg'i turi: {self.__fuel_type}{Style.RESET_ALL}")


Car1 = Car("Chevrolet Malibu", "Oq", 240, 30000, "Benzin")
Car2 = Car("Toyota Corolla", "Qora", 220, 25000, "Dizel")


print(Fore.YELLOW + "\n== Car haqida ma'lumotlar ==" + Style.RESET_ALL)
print(Car1.info())
print(Car2.info())


print(Fore.BLUE + "\nYoqilg'i turini yangilash:" + Style.RESET_ALL)
Car1.set_fuel_type("Gaz")
Car2.set_fuel_type("Elektr")


print(Fore.YELLOW + "\n== Yangilangan Car ma'lumotlari ==" + Style.RESET_ALL)
print(Car1.info())
print(Car2.info())
