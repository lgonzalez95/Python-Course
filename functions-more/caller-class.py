class Department:
    def __init__(self):
        self.depts = {
            'HR': 'Human Resources',
            'SM': 'Sales and Marketing',
            'TI': 'Technology Information'
        }

    def __call__(self, dept):
        return self.depts[dept]


d = Department()
s = d('TI')
print(s)
print(d('HR'))
