class Computer:
    def __init__(self, name, cpu, os):
        self.name = name
        self.cpu = self.CPU(cpu)
        self.os = self.OS(os)

    def __str__(self):
        return 'Computer Info: \nName: ' + self.name + '\nCPU: ' + self.cpu.get_make() + '\nOS: ' + self.os.get_name()

    class CPU:
        def __init__(self, make):
            self.make = make

        def get_make(self):
            return self.make

    class OS:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name


c = Computer('Dell 23HGA5', 'Intel', 'Windows')
print(c)
