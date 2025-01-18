from colorama import Fore, Style

class Education:

    def __init__(self):
        pass

    def course(self):
        print(f"{Fore.LIGHTRED_EX}Dars o'tkazish metodi hali aniqlanmagan.{Style.RESET_ALL}")

class IT_center(Education):

    def course(self):
        print(f"{Fore.LIGHTRED_EX}Dasturlash darslari o'tkazilmoqda.{Style.RESET_ALL}")

class Lenguage_center(Education):

    def course(self):
        print(f"{Fore.LIGHTYELLOW_EX}Xorijiy til darslari o'tkazilmoqda.{Style.RESET_ALL}")

it_center = IT_center()
l_center = Lenguage_center()

print(f"{Fore.BLUE}IT markazi: ", end="")
it_center.course()

print(f"{Fore.GREEN}Til markazi: ", end="")
l_center.course()
