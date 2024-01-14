class Company:
    compName="Veritas"
    ceoName=""
    def __init__(self,empCount,loc,team):
        self.empCount=empCount
        self.loc=loc 
        self.team=team

    def info(self):
        print("Location:=",self.loc)
        print("Employee Count=",self.empCount)
        print("Team=",self.team)

    @classmethod
    def compInfo(cls):
        print("Name of Company:",cls.compName)
    
    @staticmethod
    def ceoInfo():
        print("Name of CEO:",Company.ceoName)


comp=Company(100,"Pune","Developers")
comp.info()
comp.compInfo()
comp.ceoInfo()

# Output
# Location:= Pune
# Employee Count= 100
# Team= Developers
# Name of Company: Veritas
# Name of CEO:
