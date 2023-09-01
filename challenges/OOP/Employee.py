class Employee:
    emp_count = 100

    def __init__(self, name, salary, designation):
        Employee.emp_count += 1
        self.name = name
        self.emp_id = 'e' + str(Employee.emp_count)
        self.salary = salary
        self.designation = designation

    def show_details(self):
        print('Id:', str(self.emp_id) +
              '\nName:', self.name +
              '\nSalary:', str(self.salary) +
              '\nDesignation:', self.designation)

    @classmethod
    def total_employees(cls):
        return 'Total employees: ' + str(cls.emp_count - 100)


e1 = Employee('Juan', 100, 'Programmer')
e2 = Employee('Juana', 100, 'Programmer')
e1.show_details()
print(Employee.total_employees())
