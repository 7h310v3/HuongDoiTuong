class XeMay:
    phankhoi: int
    tenxe: str
    xuatxu : str

    def __init__(self, phankhoi, tenxe, xuatxu):
        self.phankhoi = phankhoi
        self.tenxe = tenxe
        self.xuatxu = xuatxu

    def outputXeMay(self) -> str:
        result = "Phân Khối: " + str(self.phankhoi) + "\nTên Xê: " + self.tenxe + "\nXuất xứ: " + self.xuatxu
        return result