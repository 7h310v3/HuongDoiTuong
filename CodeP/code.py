import pickle

#Người
class Person:
    name : str
    mail : str
    phone : str

    def __init__(self, name, phonenumber, email) -> None:
        self.name = name
        self.phonenumber = phonenumber
        self.email = email

    def outputPerson(self) -> str:
        pr = 'Name: ' + self.name + '; Phone number: ' + self.phonenumber + '; Email address: ' + self.email + '\n'
        return pr

#Sinh viên
class Student(Person):
    studentID : str
    averagemark : float

    def __init__(self, name, phonenumber, email, studentnumber, averagemark) -> None:
        Person.__init__(self, name, phonenumber, email)
        self.studentnumber = studentnumber
        self.averagemark = averagemark

    def outputStudent(self) -> str:
        pr = self.outputPerson() + 'Student Number: ' + self.studentnumber + 'Average Mark: ' + str(self.averagemark) + '\n'
        return pr

#Giảng viên
class Professor(Person):
    salary : float

    def __init__(self, name, phonenumber, email, salary) -> None:
        Person.__init__(self, name, phonenumber, email)
        self.salary = salary

    def outputProfessor(self) -> str:
        pr = self.outputPerson() + 'Salary: '+str(self.salary)+ '\n'
        return pr

#Nhập dữ liêu Person
per = []
count = 1
while count <= 3:
    print('Person',count)
    count+=1
    na = input('Name: ')
    e = na + '@gmail.com'
    per.append(Person(na, input('Phone: '),e))

#Sắp xếp dữ liệu Person
for i in range(3):
    for j in range(i+1,3):
        if per[i].name < per[j].name:
            per[i],per[j]=per[j],per[i]

#In dữ liệu Person vào file
with open('person.txt', 'wb+') as f:
    for i in per:
        pickle.dump(i.outputPerson(), f)

#Đọc dữ liệu từ file Person.txt và xuất ra MH
with  open('person.txt', 'rb+') as sf:
    for i in range(3):
        print('Person', i+1, ':')
        print(pickle.load(sf))

#Nhập dữ liệu cho sinh viên
stu = []
count = 1
while count <= 3:
    print('Student', count)
    count += 1
    na = input('Name: ')
    e = na + '@gmail.com'
    stu.append(Student(na, input('Phone: '), e, input('studentnumber: '), input('Average mark: ')))

#Sắp xếp dữ liệu sinh viên
for i in range(3):
    for j in range(i + 1, 3):
        if stu[i].averagemark < stu[j].averagemark:
            stu[i], stu[j] = stu[j], stu[i]

#In dữ liệu Student vào file
with open('student.txt', 'wb+') as f:
    for i in stu:
        pickle.dump(i.outputPerson(), f)

#Đọc dữ liệu từ file student.txt và xuất ra MH
with  open('student.txt', 'rb+') as sf:
    for i in range(3):
        print('Student', i+1, ':')
        print(pickle.load(sf))

#Nhập dữ liệu cho giảng viên
prof = []
count = 1

while count <= 3:
    print('Professor ', count)
    count += 1
    na = input('Name: ')
    e = na + '@gmail.com'
    prof.append(Professor(na, input('Phone: '), e, float(input('Salary: '))))

#Sắp xếp dữ liệu giảng viên
for i in range(3):
    for j in range(i + 1, 3):
        if prof[i].salary > prof[j].salary:
            prof[i], prof[j] = prof[j], prof[i]

#In dữ liệu Professor vào file
with open('professor.txt', 'wb+') as f:
    for i in prof:
        pickle.dump(i.outputPerson(), f)

#Đọc dữ liệu từ file Professor.txt và xuất ra MH
with  open('professor.txt', 'rb+') as sf:
    for i in range(3):
        print('Professor ', i+1, ':')
        print(pickle.load(sf))
