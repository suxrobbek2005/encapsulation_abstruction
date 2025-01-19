from colorama import Fore, Style


class Developer:

    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer):

    def __init__(self, surname, position, salary, bonus, department):

        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department

  
    def total_salary(self):

        return self.salary + self.bonus

   
    def info(self):

        return (f"{Fore.CYAN}Familiya: {self.surname}, Lavozim: {self.position}, "
                f"Bo'lim: {self.department}, Asosiy oylik: {self.salary} USD, "
                f"Ustama: {self.bonus} USD, Umumiy maosh: {self.total_salary()} USD{Style.RESET_ALL}")


employees = []

length = int(input("Nechta xodimning malumotlarini kiritmoqchisiz "))

for i in range(length):

    print(Fore.YELLOW + f"\n{i+1} - xodimning ma'lumotlarini kiriting:" + Style.RESET_ALL)
    surname = input("Familiyasi: ")
    position = input("Lavozimi (Junior/Middle/Senior): ")
    salary = int(input("Asosiy oyligi (USD): "))
    bonus = int(input("Ustama haqi (USD): "))
    department = input("Bo'lim (1-bo'lim, 2-bo'lim yoki 3-bo'lim): ")
    employees.append(SoftwareEngineer(surname, position, salary, bonus, department))


department_salaries = {}

for emp in employees:

    if emp.department not in department_salaries:

        department_salaries[emp.department] = 0
    department_salaries[emp.department] += emp.total_salary()


print(Fore.GREEN + "\n== Xodimlar haqida ma'lumot ==" + Style.RESET_ALL)

for emp in employees:
    print(emp.info())

print(Fore.MAGENTA + "\n== Bo'limlar bo'yicha umumiy maoshlar ==" + Style.RESET_ALL)

for department, total in department_salaries.items():
    print(f"Bo'lim {department}: {total} USD")
