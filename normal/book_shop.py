from colorama import Fore, Style


class BookShop:

    def __init__(self, name, location, book_list):

        self.name = name
        self.locaton = location
        self.book_list = book_list

    def CientificBooks(self):

        scientific_books = [book for book in self.book_list if "ilmiy" in book.lower()]

        if scientific_books:

            print(Fore.BLUE + f"{self.name} Do‘konida ilmiy kitoblar mavjud:" + Style.RESET_ALL)

            for kitob in scientific_books:

                print(Fore.GREEN + f"- {kitob}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{self.name} Dokonida ilmiy kitoblar yoq." + Style.RESET_ALL)


dokon1 = BookShop("Ziyo", "Toshkent", ["ilmiy Fizika", "Adabiyot", "Matematika Asoslari"])
dokon2 = BookShop("Bilim", "Samarqand", ["Tarix", "She'riyat", "Kimyo"])
dokon3 = BookShop("Fan", "Buxoro", ["Geografiya", "ilmiy Biologiya", "Psixologiya"])


dokon1.CientificBooks()
dokon2.CientificBooks()
dokon3.CientificBooks()
