class person:
    def __init__(self):
        self.name = None
        self.age = None
        self.nationality = None

class student(person):
    def __init__(self):
        super().__init__()
        self.grade = None

class slavetrader(person):
    def __init__(self):
        self.slave = (person)


James = person()
Jean = person()

James.name = 'James'