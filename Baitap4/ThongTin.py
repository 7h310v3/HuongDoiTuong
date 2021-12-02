class Person:
    name : str
    mail : str
    phone : str

    def __init__(self, ten, mail, sdt) -> None:
        super().__init__()
        self.name= ten
        self.mail = mail
        self.phone = sdt

    def outputPerson(self) -> str:
        result = "Tên:" + self.name + "\tĐịa chỉ mail:" + self.mail + "\tSố điện thoại:" + self.phone
        return result

class Student(Person):
    studentID : str
    averagerank : int

    def __init__(self, ten, mail, sdt, studentID, averagerank ) -> None:
        Person.__init__(self, ten, mail, sdt)
        self.studentID = studentID
        self.averagerank = averagerank

    def outputStudent(self) -> str:
        result = self.outputPerson() + "\tMSSV:" + self.studentID + "\tĐiểm trung bình:" + str(self.averagerank)
        return result

class Professor(Person):
    salary : int
    def __init__(self, ten, mail, sdt,luong) -> None:
        Person.__init__(self, ten, mail, sdt)
        self.salary = luong

    def outputProfessor(self) -> str:
        result = self.outputPerson() + "\tLương:" + str(self.salary)
        return result
