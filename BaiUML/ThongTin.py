class Item:
    shippingWeight:float
    description:str

    def __init__(self,shippingWeight,description):
        self.shippingWeight=shippingWeight
        self.description=description
    def addpriceofquantity(self):
        pass
    def addTax(self):
        pass
    def instock(self):
        pass
    def addItem(self)->str:
        result ="Vận chuyển:" + str(self.shippingWeight) + "\tMô tả:" + self.description
        return result

class OrderDetail:
    quantity:str
    taxStatus:str
    item: Item

    def __init__(self,quantity,taxStatus):
        self.quantity=quantity
        self.taxStatus=taxStatus
    def calcSubtotal(self):
        pass
    def Weight(self):
        pass
    def Tax(self):
        pass
    def lietkeItem(self,item:Item):
        print("Số lượng:", self.quantity, "đã mua")

class Payment:
    ammount : float

    def __init__(self,amount):
        super().__init__()
        self.amount=amount
    def addAmount(self)->str:
        result = "Giá: " + str(self.amount)
        return result

class Cash(Payment):
    cashTendered : float

    def __init__(self, ammount,cashTendered):
        Payment.__init__(self, ammount)
        self.cashTendered = cashTendered
    def addCash(self)->str:
        result= self.addAmount() + "\tTrả: " + self.cashTendered
        return result

class Check(Payment):
    name : str
    bankID : str

    def __init__(self, ammount, name, bankID):
        Payment.__init__(self, ammount)
        self.name = name
        self.bankID = bankID

    def addcheck(self)->str:
        result=self.addAmount() + "\tTên: " + self.name + "\tBank ID" + self.bankID
        return result

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

class Order:
    date : datetime
    status : str
    orderDetail : list[OrderDetail]
    payment : list[Cash,Check,Credit]

    def __init__(self,date,status):
        self.date = date
        self.status = status
    def calcSubTotal(self):
        pass
    def calcTax(self):
        pass
    def calcTotal(self):
        pass
    def Totalweight(self):
        pass
    def addOrderDetail(self,chitiet:OrderDetail):
        self.orderDetail.append(chitiet)
    def addOrderDetail(self) -> list[OrderDetail]:
        return self.orderDetail
    def addPayment(self,chitra:Payment):
        self.payment.append(chitra)
    def addPayment(self) -> list[Payment]:
        return self.payment
    def addOrder(self) -> str:
        return result

class Customer:
    name:str
    address:str
    orders:list[Order]

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.order=[]
    def addOrder(self,donhang:Order):
        self.order.append(donhang)
    def addOrder(self)->list[Order]:
        return self.order
    def addCustomer(self)->str:
        result="Khách hàng:" + self.name + "\tĐịa chỉ:" + self.address + "\tĐã mua:" + self.order
        return result