from Person import Person, Student, Lecturer

def main():
    minh = Student("Nhật Minh", "Nam", "09481297812","21E122", 1)
    trung = Student("Quang Trung", "Nam", "0982983712","21E129", 2)
    thayCuong = Lecturer("Hoa Cương", "Nam", "0982983213","98219312",20)

    print(minh.outputStudent())
    print(trung.outputStudent())
    print(thayCuong.outputLecturer())
if __name__ == "__main__":
    main()