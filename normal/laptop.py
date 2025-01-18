from colorama import Fore, Style


class Education:

    def __init__(self):
        pass

    def course(self):
        print(f"{Fore.LIGHTRED_EX} Dars o'tkazish metodi hali aniqlanmagan {Fore.RESET}")

class IT_center(Education):

    def course(self):
        print(f"{Fore.LIGHTRED_EX},Dasturlash darslari o'tkazilmoqda {Fore.RESET}")

class Lenguage_center(Education):

    def course(self):
        print(f"{Fore.LIGHTYELLOW_EX},Xorijiy til darslari o'tkazilmoqda.{Fore.RESET}")


it_center = IT_center()
l_cource = Lenguage_center()


print(f"{Fore.BLUE} IT markazi: {it_center.course}, {Style.RESET_ALL}")
it_center.course

print(f"{Fore.GREEN} Til markazi: {l_cource.course}, {Style.RESET_ALL}")
l_cource.course