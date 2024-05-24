from dataclasses import dataclass


@dataclass
class Employee1:
    name: str
    dept: str
    salary: int


john = Employee1("john", "computer lab", 1000)

print(f"Nom: {john.name}, Salaire: ${john.salary}")


class Employee:
    salary = 7

    def __init__(self, name, dept, salary=salary):
        self.name = name
        self.dept = dept
        self.salary = salary


johnny = Employee("johnny", "labo", 1500)

print(f"Nom: {johnny.name}, Salaire: ${johnny.salary}")
