class Payment:
    amount: float

    def __init__(self, amount) -> None:
        self.amount = amount
        pass

class Cash(Payment):
    cashTendered: float

    def __init__(self, amount, cashTendered) -> None:
        Payment.__init__(self, amount)
        self.cashTendered = cashTendered

class Check(Payment):
    name: str
    bankID: str

    def __init__(self, amount, name, bankID) -> None:
        Payment.__init__(self, amount)
        self.name = name
        self.bankID = bankID

    def authorized(self) -> bool:
        pass

class Credit(Payment):
    number: str
    type: str

    def __init__(self, amount, number, type, expDate) -> None:
        Payment.__init__(self, amount)
        self.type = type
        self.number = number

    def authorized(self) -> bool:
        pass

class Item():
    shippingWeight: float
    description: str

    def __init__(self, shippingWeight, description) -> None:
        self.shippingWeight = shippingWeight
        self.description = description

    def getPriceForQuantity(self) -> str:
        pass

    def getTaxi(self) -> str:
        pass

    def inStock(self) -> str:
        pass

class OrderDetail:
    taxStatus: str

    def __init__(self, quantity, taxStatus) -> None:
        self.taxStatus = taxStatus
        self.quantity = quantity

    def calcSubTotal(self) -> int:
        pass

    def calcWeight(self) -> int:
        pass

    def calcTax(self) -> int:
        pass

class Order:
    status: list[OderDetail]

    def __init__(self, date, status) -> None:
        self.date = date
        self.status = status

    def addPayment(self, Payment):
        pass

    def calcSubTotal(self) -> int:
        pass

    def calcTax(self, Tax):
        self.status = Tax
        pass

    def calcTotal(self) -> int:
        pass

    def calcTotalWeight(self) -> int:
        pass

class Customer:
    dsdh: list[Order]
    name: str
    address: str

    def addOder(self, Oder):
        pass