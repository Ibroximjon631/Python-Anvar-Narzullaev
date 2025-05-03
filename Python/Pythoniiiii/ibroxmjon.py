from uuid import    uuid4
class  Malumotlar():
    __abcdef=0
    def __init__(self,Name,Fname,Nimadr,Ii,Abc):
        self.Name=Name
        self.Fname=Fname
        self.Nimadr=Nimadr
        self.__Ii=Ii
        self.__Abc=uuid4()
        self.__abcdef+=1
    def __str__(self):
        return f"{self.Name} {self.Fname} {self.Nimadr}"
    def __repr__(self):
        return f"{self.Name} {self.Fname} {self.Nimadr}"
    def gt_ii(self):
        return self.__Ii
    @classmethod
    def iabc(cls):
        return cls.__abcdef
    def abc(self):
        return self.__Abc
    def add_ii(self,abcd):
        self.__Ii+=abcd
        return self.__Ii


abc=Malumotlar('Ibroximjon',"Iii",123,123,"Hi")
abcdi=Malumotlar('Ibroximjon',"Iii",123,123,"Hi")
print(abc.gt_ii())
print(abc.abc())
print(abc.add_ii(123))
print(Malumotlar.iabc())
















#     def gt_info(self):
#         return f"{self.Name}, {self.Fname}, {self.Nimadr}"
# abc=Malumotlar("Ibroximjon","Ali",17)
# print(abc.gt_info())
# class Kimdrla(Malumotlar):
#     def __init__(self,Name,Fname,Nimadr,Kurs):
#         super().__init__(Name,Fname,Nimadr)
#         self.Kurs=1
# ii=Kimdrla("Ibroximjon","Ali",17)
# print(ii.gt_info())