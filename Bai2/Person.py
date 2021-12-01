class Person:
    name : str
    gender : str
    phone : int

    def __init__(self, ten, gioitinh, sdt) -> None:
        super().__init__()
        self.name= ten
        self.gender = gioitinh
        self.phone = sdt

    def outputPerson(self) -> str:
        result = "Tên: " + self.name + "\nGiới tính: " + self.gender + "\nSố điện thoại: " + str(self.phone)
        return result

class Student(Person):
    studentID : str
    rank : int

    def __init__(self, ten, gioitinh, sdt, studentID, rank ) -> None:
        Person.__init__(self, ten, gioitinh, sdt)
        self.studentID = studentID
        self.rank = rank

    def outputStudent(self) -> str:
        result = self.outputPerson() + "\nMSSV: " + self.studentID + "\nSV Năm: " + str(self.rank)
        return result

class Lecturer(Person):
    lecturerID : str
    yearsOfExperience : int
    def __init__(self, ten, gioitinh, sdt,lecturerID, yearsOfExperience) -> None:
        Person.__init__(self, ten, gioitinh, sdt)
        self.lecturerID = lecturerID
        self.yearsOfExperience = yearsOfExperience

    def outputLecturer(self) -> str:
        result = self.outputPerson() + "\nMSGV: " + self.lecturerID + "\nSố năm kinh nghiệm: " + str(self.yearsOfExperience)
        return result
