class Employee:
    '员工类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : %s ,Salary : %d" % (self.name, self.salary))


emp1 = Employee("Tom", 1000)
emp2 = Employee("Jerry", 1500)
emp1.display_employee()
emp2.display_employee()
print("Total Employee : %d" % Employee.empCount)
emp2.display_count()
print(Employee.__doc__)
