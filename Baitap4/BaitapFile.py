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
    name =  input("Nhập tên: ")
    sdt = input("Nhập sđt: ")
    mail = input("Nhập mail:")
    id = input("Nhập ID: ")
    dtb = input("Nhập điểm trung bình: ")
    x = Student(name, mail, sdt, id, dtb)
    return x #Nhap1SV() = x

def Nhap1GV():
    name =  input("Nhập tên: ")
    sdt = input("Nhập sđt: ")
    mail = input("Nhập: mail ")
    luong = input("Nhập lương: ")
    x = Professor(name, sdt, mail, luong)
    return x

def NhapSV(x):
    result = [] #result = list
    for i in range(x): # x = số sinh viên
        print("Nhập thông tin sinh viên", i + 1)
        result.append(Nhap1SV())
    return result #NhapSV() = danh sách gồm n đối tượng sinh viên

def NhapGV(x):
    result = []
    for i in range(x):
        print("Nhập thông tin giảng viên", i + 1)
        result.append(Nhap1GV())
    return result

def XuatSV(result):
    for i in result: #result = list danh sach SV
        print(i.outputStudent())

def XuatGV(result):
    for i in result:
        print(i.outputProfessor())

def XuatPS(result):
    for i in result:
        print(i.outputPerson())

def SapxepPS(result):
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if(result[i].name > result[j].name):
                result[i], result[j] = result[j], result[i]
    return result

def SapxepSV(result):
    for i in range(len(result)):
        for j in range(i+1,len(result)): #[i+1, len)
            if(result[i].averagerank > result[j].averagerank):
                result[i], result[j] = result[j], result[i]
    return result

def SapxepGV(result):
    for i in range(len(result)):
        for j in range(i+1,len(result)): #[i+1, len)
            if(result[i].salary < result[j].salary):
                result[i], result[j] = result[j], result[i]
    return result

def InVaoFilePS(result):
    with open("person.obj", "wb+") as f:
        for i in result:
            pickle.dump(i.outputPerson(), f)

def InVaoFileSV(result):
    f = open("sinhvien.obj", "wb+")
    for i in result: #Cho i chạy từ phần tử đầu tiên đến cuối cùng của danh sách sinh viên
        pickle.dump(i.outputStudent(), f)
    f.close()

def InVaoFileGV(result):
    with open("giangvien.obj", "wb+") as f:
        for i in result:
            pickle.dump(i.outputProfessor(), f)

def DocFile(tenfile, x, name):
    with  open(tenfile, "rb+") as sf:
        for i in range(x):
            print(name, "thứ", i+1, ":")
            print(pickle.load(sf))

#Hàm chính
def main():
    dssv = []
    dsgv = []
    ssv = NhapN(" sinh viên: ")
    sgv = NhapN(" giảng viên: ")

    #Sinh Viên
    dssv = NhapSV(ssv)
    #XuatSV(dssv)

    #Giảng Viên
    dsgv = NhapGV(sgv)
    #XuatGV(dsgv)

    #Người
    sps = ssv + sgv
    dsps = dssv + dsgv
    #XuatPS(sps)

    #Sapxep
    dsps = SapxepPS(dsps)
    dssv = SapxepSV(dssv)
    dsgv = SapxepGV(dsgv)

    #InFile
    InVaoFilePS(dsps)
    InVaoFileSV(dssv)
    InVaoFileGV(dsgv)

    #Docfile
    print("Person:")
    DocFile("person.obj", sps, "Người")
    print("Sinh viên:")
    DocFile("sinhvien.obj", ssv, "Sinh viên")
    print("Giảng viên:")
    DocFile("giangvien.obj", sgv, "Giảng viên")

if __name__ == "__main__":
    main()