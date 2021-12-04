class Customer:

    name : str
    address

    def outputCus

class Order:
    date : date
    status : str

    def __init__(self):
        calcSubTotal

class OrderDetail:
    quanlity
    taxStatus : str
    def __init__(self, name, address, quanlity, taxStatus):
        Customer.__init__(self, name, address)
        self.quanlity = quanlity
        self.taxStatus = taxStatus

    def calcTotal(self):
        return calcWeight()
    def calcWeight(self):
        pass
    def calcTax(self):
        pass



class Payment():
    ammount : float

    def __init__(self, ammount):
        self.ammount = ammount

class Cash(Payment):
    cashTendered : float

    def __init__(self, ammount,cashTendered):
        Payment.__init__(self, ammount)
        self.cashTendered = cashTendered

class Check(Payment):
    name : str
    bankID : str

    def __init__(self, ammount, name, bankID):
        Payment.__init__(self, ammount)
        self.name = name
        self.bankID = bankID

    def outputCheck(self):
        pass

class Credit(Payment):
    number : str
    type : str
    expDate

    def __init__(self, payment, number, type, expDate):
        self.number = number
        self.type = type
        self.expDate = expDate

    def outputCredit(self):
        pass

