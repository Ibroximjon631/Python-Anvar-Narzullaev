# class Hi:
#     def __init__(self):
#         print("Hi")
#     def name(self, name):
#         self.name = name
#         self.abc=10
#         return self.name
#     def xyz(self, abcd):
#         self.abc=abcd
#     def get_info(self):
#         print(f"{self.name} {self.abc}")
# abc=Hi()
# abc.name("Iii")
# abc.xyz(5)
# abc.get_info()
# print(abc.name)


class Korsatsh:
    def __init__(self,object):
        self.object = object
        self.names=[]
        self.nectaligi=0
        #Konstruktr yaratadi. Return bomiydi
    def add_name(self,name):
        self.names.append(name)
        self.nectaligi+=1

    def inf(self):
        for i in self.names:

            print(f"{i} ")
    def malumot(self,name):
        return [mlmt for mlmt in dir(name) if mlmt.startswith("__") is False]
class Nimdadrla:
    super.__init__(object)

brci=Korsatsh("Matematika")
print(brci.inf())
brci.add_name("Hi hi hi")
brci.inf()
print(brci.malumot(Korsatsh))
#print(dir(Korsatsh))