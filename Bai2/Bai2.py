from Person import Person, Student, Lecturer

def main():
    per = []
    count = 0
    while(count < 2):
        n = input("Nhap ten: ")
        e = n + "@gmail.com"
        sdt = input("Nhap sdt: ")
        per.append(Person(n, e, sdt))
        count += 1

    count = 0
    while (count < 2):
        print(per[count].outputPerson())
        count += 1

if __name__ == "__main__":
    main()