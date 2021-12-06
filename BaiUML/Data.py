import datetime

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
        print("So luong:",self.quantity,"Duoc mua")

class Order:
    date: datetime
    status: str
    orderDetail:list[OrderDetail]
    payment:list[Cash,Check,Credit]

    def __init__(self,date,status):
        self.date=date
        self.status=status
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
    def getOrderDetail(self)->list[OrderDetail]:
        return self.orderDetail
    def addPayment(self,chitra:Payment):
        self.payment.append(chitra)
    def getPayment(self)->list[Payment]:
        return self.payment
    def getOrder(self)->str:
        result="Ngày:"+self.date+"\tTình trạng:"+self.status+"\tĐã mua:"+self.orderDetail+"\tThành tiền:"+self.payment
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
    def getOrder(self)->list[Order]:
        return self.order
    def getCustomer(self)->str:
        result="Khách hàng:"+self.name+"\tĐịa chỉ:"+self.address+"\tĐã mua:"+self.order
        return result


class Payment:
    amount:float

    def __init__(self,amount):
        super().__init__()
        self.amount = amount
    def getAmount(self)->str:
        result="Giá: " + str(self.amount)
        return result

class Cash(Payment):
    cashTendered: float

    def __init__(self,amount,cashTendered):
        Payment.__init__(self,amount)
        self.cashTendered=cashTendered
    def getCash(self)->str:
        result= self.getAmount()+"\tTrả: "+self.cashTendered
        return result

class Check(Payment):
    name:str
    bankID:str

    def __init__(self, amount, name, bankID):
        Payment.__init__(self, amount)
        self.name=name
        self.bankID=bankID
    def getcheck(self)->str:
        result=self.getAmount() + "\tTên: " + self.name  + "\tBank ID" + self.bankID
        return result

class Credit(Payment):
    number: str
    type: str
    expDate:str

    def __init__(self,amount,number,type,expDate):
        Payment.__init__(self,amount)
        self.number=number
        self.type=type
        self.expDate=expDate
    def getCredit(self)->str:
        result = self.getAmount() + "\tSố: "+self.number+"\tLoại:"+self.type+"\tNgày:"+self.expDate
        return result

class Item:
    shippingWeight:float
    description:str

    def __init__(self,shippingWeight,description):
        self.shippingWeight=shippingWeight
        self.description=description
    def getpriceofquantity(self):
        pass
    def getTax(self):
        pass
    def instock(self):
        pass
    def getItem(self)->str:
        result ="Vận chuyển:"+str(self.shippingWeight)+"\tMô tả:"+self.description
        return result