class Company:
    def __init__(self,empCount,loc,compName):
        self.empCount=empCount
        self.loc=loc
        self.compName=compName
        
    
    def compInfo(self):
        print(self.empCount)
        print(self.loc)
    
class Employee(Company):
    def __init__(self,empId,empName):
        self.empId=empId
        self.empName=empName

    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1=Employee(45,"XYZ")
emp1.empInfo()

# Output
# 500
# Pune
# Veritas

