class Royhat:
    def __init__(self):
        self.lst=[]
        self.cnt=0
    def  AddRoyhat(self,name,iiii ):
        self.lst.append({'name':name,'iii':iiii})
        self.cnt+=1
    def ocirishlst(self,name):
        for i in self.lst:
            if i['name']==name:
                self.lst.remove(i)
                break
        self.cnt-=1
    def korsatsh(self):
        for i in self.lst:
            print(f"Nimadr:{i['name'].capitalize()} Kimdr:{i['iii']}")
    def cnti(self):
        print(self.cnt)
    def ozgartirish(self,name,yangi):
        for i in self.lst:
            if i['name']==name:
                i['iii']=yangi
                break
abc = Royhat()
abc.AddRoyhat("School 21","21")
abc.AddRoyhat("Najot talim","37")
abc.korsatsh()
abc.ocirishlst("School 21")
abc.korsatsh()
abc.ozgartirish("School 21","School")
abc.korsatsh()