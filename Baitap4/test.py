import pickle
from ThongTin import Person, Student, Professor

def NhapN(name):
    n = "Nhập số" + str(name)
    x = int(input(n))
    while(x <= 0):
        print("Nhập sai, xin nhập lại!")
        x = int(input("Nhập số lượng: "))
    return x

def Nhap1SV():
    tt = []
    tt.append(input("Nhập tên: "))
    tt.append(input("Nhập email: "))
    tt.append(input("Nhập sđt: "))
    tt.append(input("Nhập ID: "))
    tt.append(input("Nhập điểm trung bình: "))
    return tt

def Nhap1GV():
    tt = []
    tt.append(input("Nhập tên: "))
    tt.append(input("Nhập email: "))
    tt.append(input("Nhập sđt: "))
    tt.append(input("Nhập lương: "))
    return tt

def NhapSV(x,a):
    for i in range(x):
        print("Nhập thông tin sinh viên", i + 1)
        a.append(Nhap1SV())

def NhapGV(x, a):
    for i in range(x):
        print("Nhập thông tin giảng viên", i + 1)
        a.append(Nhap1GV())

def XuatSV(x, a):
    for i in range(x):
        j, k, l, m, n = tuple(a[i])
        j = Student(j, k, l, m, n)
        print(j.outputStudent())

def XuatGV(x, a):
    for i in range(x):
        j, k, l, m = tuple(a[i])
        j = Professor(j, k, l, m)
        print(j.outputProfessor())

def XuatPS(x, a):
    for i in range(x):
        print(a[i])
        #j, k, l = tuple(a[i])
        #j = Professor(j, k, l)
        #print(j.outputPerson())

def InVaoFilePS(x, a):
    with  open("person.obj", "wb+") as f:
        for i in range(x):
            j, k, l = tuple(a[i])
            j = Person(j, k, l)
            pickle.dump(j.outputPerson(), f)

def InVaoFileSV(x, a):
    with  open("sinhvien.obj", "wb+") as f:
        for i in range(x):
            j, k, l, m, n = tuple(a[i])
            j = Student(j, k, l, m, n)
            pickle.dump(j.outputStudent(), f)

def InVaoFileGV(x, a):
    with  open("giangvien.obj", "wb+") as f:
        for i in range(x):
            j, k, l, m = tuple(a[i])
            j = Professor(j, k, l, m)
            pickle.dump(j.outputProfessor(), f)

def DocFile(tenfile,x):
    with  open(tenfile, "rb+") as sf:
        for i in range(x):
            j = pickle.load(sf)
            print(j)

def main():
    dssv = []
    dsgv = []
    ssv = NhapN(" sinh viên: ")
    sgv = NhapN(" giảng viên: ")

    #SV
    NhapSV(ssv, dssv)
    #XuatSV(ssv, dssv)

    #GV
    NhapGV(sgv, dsgv)
    #XuatGV(sgv,dsgv)

    #InFile
    InVaoFilePS((ssv + sgv), dssv + dsgv)
    InVaoFileSV(ssv,dssv)
    InVaoFileGV(sgv, dsgv)

    #Docfile
    DocFile("person.obj", ssv+sgv)
    DocFile("sinhvien.obj", ssv)
    DocFile("giangvien.obj", sgv)

if __name__== "__main__":
    main()