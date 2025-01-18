from colorama import Fore, Style


class Hayvon:
    def __init__(self, turi, vazni):
        self.turi = turi
        self.vazni = vazni

    def ovoz_chiqarish(self):
        return "Ovoz chiqarish metodi hali aniqlanmagan."

# Bola klasslar
class It(Hayvon):
    def ovoz_chiqarish(self):
        return "vov-vov"

class Mushuk(Hayvon):
    def ovoz_chiqarish(self):
        return "miyov-miyov"


it = It("Ovchi iti", 25)
mushuk = Mushuk("Uy mushugi", 5)


print(Fore.BLUE + f"It ovozi: {it.ovoz_chiqarish()}" + Style.RESET_ALL)
print(Fore.GREEN + f"Mushuk ovozi: {mushuk.ovoz_chiqarish()}" + Style.RESET_ALL)
