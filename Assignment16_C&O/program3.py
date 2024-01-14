class Company:
    compName="Meta"
    def __init__(self,empCount,loc):
        self.empCount=empCount
        self.loc=loc
    
    def info(self):
        print(self.empCount)
        print(self.loc)
    
    @classmethod
    def compInfo(cls):
        print(cls.compName)

class Employee(Company):
    pass

emp1=Employee(200,"Pune")
emp1.info()
emp1.compInfo()

# Output
# 200
# Pune
# Meta