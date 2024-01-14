class Company:
    def __init__(self,empCount,loc,compName):
        self.empCount=empCount
        self.loc=loc
        self.compName=compName
        
    
    def compInfo(self):
        print(self.empCount)
        print(self.loc)
    
class Employee(Company):
    # def __init__(self,empCount,loc):
    #     self.empCount=empCount
    #     self.loc=loc

    def compInfo(self):
        print(self.empCount)
        print(self.loc)
        print(self.compName)

emp1=Employee(500,"Pune","Veritas")
emp1.compInfo()

# Output
# 500
# Pune
# Veritas

