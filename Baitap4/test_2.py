from ThongTin import Person, Student, Professor

def SapxepPS(a):
    for i in range (0, len(a)):
        tuple(a[i])
        j, k, l = a[i][1], a[i][2], a[i][3]
        t = Person(j, k, l)
        for j in range (i+1, len(a)):
            m = a[j]
            o = str()
            o = m[0]
            p = str()
            q = str(m[2])
            r = Person(o, p, q)
            if(t.name < r.name):
                a[i], a[j] = a[j], a[i]
    return a

def main():
    dsv1 = ["Nhật Minh", "minh92dd@gmail.com", "09481297812","21E122", 1]
    dsv2 = ["Quang Trung", "quangtrung@gmail.com", "0942129712","21E121", 2]

    ds = dsv1 + dsv2

    print("Sắp xếp", SapxepPS(ds))

if __name__== "__main__":
    main()