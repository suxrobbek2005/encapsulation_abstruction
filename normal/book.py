from colorama import Fore, Style


class Book:

    def __init__(self, name, page_count, price):

        self.name = name
        self.page_count = page_count
        self.price = price

    def page_increase(self):

        self.page_count += 10

    def page_reduce(self):

        if self.page_count > 100:
            self.price /= 2

    def info(self):

        return (f"{Fore.CYAN}Kitob: {self.name}, Sahifalar: {self.page_count}, Narxi: {self.price} so'm{Style.RESET_ALL}")


books = []

length = int(input("Nechta kitobni narxini kiritmoqchisiz "))

for i in range(length):

    print(Fore.YELLOW + f"{i + 1}-kitob ma'lumotlarini kiriting:" + Style.RESET_ALL)
    name = input("Kitob nomi: ")
    page_count = int(input("Sahifalar soni: "))
    price = float(input("Narxi: "))
    books.append(Book(name, page_count, price))


for book in books:

    book.page_increase()
    book.page_reduce()


print(Fore.GREEN + "\nYangilangan kitob ma'lumotlari:" + Style.RESET_ALL)

for book in books:
    
    print(book.info())
