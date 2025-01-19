from colorama import Fore, Style

class Laptop:

    def __init__(self, brand, price, battery_life):

        self.brand = brand
        self.price = price
        self.battery_life = battery_life

   
    def apply_discount(self, percent):

        self.price -= self.price * (percent / 100)

    
    def check_battery_and_discount(self):

        if self.battery_life < 5:
            self.apply_discount(10)

    
    def info(self):

        return (f"{Fore.GREEN}Brand: {self.brand}, Narx: {self.price} USD, "
                f"Batareya vaqti: {self.battery_life} soat{Style.RESET_ALL}")


laptop1 = Laptop("Dell", 800, 6)
laptop2 = Laptop("HP", 600, 4)
laptop3 = Laptop("Apple", 1200, 3)
laptop4 = Laptop("Asus", 700, 5)
laptop5 = Laptop("Lenovo", 500, 2)


laptops = [laptop1, laptop2, laptop3, laptop4, laptop5]


for laptop in laptops:

    laptop.check_battery_and_discount()


print(Fore.YELLOW + "\n== Laptoplar haqida ma'lumotlar ==" + Style.RESET_ALL)

for laptop in laptops:
    print(laptop.info())
