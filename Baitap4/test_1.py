import pickle
from ThongTin import Person, Student, Professor

def NhapN(name):
    n = "Nhập số" + str(name)
    x = int(input(n))
    while (x <= 0):
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

def NhapSV(x, a):
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
        t = Student(j, k, l, m, n)
        print(t.outputStudent())

def XuatGV(x, a):
    for i in range(x):
        j, k, l, m = tuple(a[i])
        t = Professor(j, k, l, m)
        print(t.outputProfessor())

def XuatPS(x, a):
    for i in range(x):
        tuple(a[i])
        j, k, l = a[i][1], a[i][2], a[i][3]
        t = Person(j, k, l)
        print(j.outputPerson())

def InVaoFilePS(x, a):
    with  open("person.obj", "wb+") as f:
        for i in range(x):
            tuple(a[i])
            j, k, l = a[i][1], a[i][2], a[i][3]
            t = Person(j, k, l)
            pickle.dump(t.outputPerson(), f)

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

def DocFile(tenfile, x, name):
    with  open(tenfile, "rb+") as sf:
        for i in range(x):
            print(name, "thứ", i+1, ":")
            j = pickle.load(sf)
            print(j)

def SapxepPS(a):
    for i in range (0, len(a)):
        tuple(a[i])
        j, k, l = a[i][1], a[i][2], a[i][3]
        t = Person(j, k, l)
        for j in range (i+1, len(a)):
            tuple(a[j])
            j1, k1, l1 = a[j][1], a[j][2], a[j][3]
            t1 = Person(j1, k1, l1)
            if(t.name < t1.name):
                a[i], a[j] = a[j], a[i]
    return a

def SapxepSV(a):
    for i in range (0, len(a)):
        for j in range (i+1, len(a)):
            if(a[i].Student.averagerank < a[j].Student.averagerank):
                tuple(a[i])
                tuple(a[j])
                a[i], a[j] = a[j], a[i]
    return a

def SapxepGV(a):
    for i in range (0, len(a)):
        for j in range (i+1, len(a)):
            tuple(a[i])
            tuple(a[j])
            if(a[i].Professor.salary < a[j].Professor.salary):
                a[i], a[j] = a[j], a[i]
    return a

#Hàm chính
def main():
    dssv = []
    dsgv = []
    ssv = NhapN(" sinh viên: ")
    sgv = NhapN(" giảng viên: ")

    # Sinh Viên
    NhapSV(ssv, dssv)
    # XuatSV(ssv, dssv)

    # Giảng Viên
    NhapGV(sgv, dsgv)
    # XuatGV(sgv,dsgv)

    # Người
    sps = ssv + sgv
    dsps = dssv + dsgv
    #XuatPS(sps, dsps)

    #dsps = SapxepPS(dsps)
    print(SapxepPS(dsps))
    #dssv = SapxepSV(dssv)
    #dsgv = SapxepGV(dsgv)

    # InFile
    #InVaoFilePS(sps, dsps)
    #InVaoFileSV(ssv, dssv)
    #InVaoFileGV(sgv, dsgv)

    # Docfile
    #DocFile("person.obj", sps, "Người")
    #DocFile("sinhvien.obj", ssv, "Sinh viên")
    #DocFile("giangvien.obj", sgv, "Giảng viên")

if __name__ == "__main__":
    main()