
class Employee:
    def __init__(self, id, name, manager):
        self.__id = id
        self.__name = name
        self.__manager = manager

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_manager(self):
        return self.__manager
    
    def is_manager(self):
        return self.__manager == None
    
    def __str__(self):
        s = f"{self.__id}, {self.__name}"
        if self.__manager != None:
            s = s + f", {self.__manager.__name}"
        return s


employee1 = Employee(1, "Park Jung Seok", None)
employee2 = Employee(2, "Sung Young Ho", employee1)
employee3 = Employee(3, "Sim Sung Suk", employee1)
employee4 = Employee(4, "Choi Su Gil", employee2)

employees = [employee1, employee2, employee3, employee4]

for employee in employees:
    s = f"{employee.get_id()}, {employee.get_name()}"
    if not employee.is_manager():
        s = s + f", {employee.get_manager().get_name()}"
    print(s)


for employee in employees:
    print(employee)

