class  Malumotlar():
    def __init__(self,Name,Fname,Nimadr):
        self.Name=Name
        self.Fname=Fname
        self.Nimadr=Nimadr
    def gt_info(self):
        return f"{self.Name}, {self.Fname}, {self.Nimadr}"
abc=Malumotlar("Ibroximjon","Ali",17)
print(abc.gt_info())
class Kimdrla(Malumotlar):
    def __init__(self,Name,Fname,Nimadr,Kurs):
        super().__init__(Name,Fname,Nimadr)
        self.Kurs=1
ii=Kimdrla("Ibroximjon","Ali",17)
print(ii.gt_info())