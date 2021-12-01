import pickle
from ThongTin import Person, Student, Professor

def main():
    minh = Student("Nhật Minh", "minh92dd@gmail.com", "09481297812","21E122", "1")
    trung = Student("Quang Trung", "trungcuteo@gmail.com", "0982983712","21E129", "2")
    thayCuong = Professor("Hoa Cương", "Nam", "0982983213",20000000)

    with  open ("data.obj", "wb+") as f:
        pickle.dump(minh.outputStudent(), f)
        pickle.dump(trung.outputStudent(), f)
        pickle.dump(thayCuong.outputProfessor(), f)

    with  open ("data.obj", "rb+") as sf:
        object_pi1 = pickle.load(sf)
        object_pi2 = pickle.load(sf)
        object_pi3 = pickle.load(sf)

    print(object_pi1)
    print(object_pi2)
    print(object_pi3)

if __name__ == "__main__":
    main()