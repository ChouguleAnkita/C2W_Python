class Demo:
    def __init__(self):
        print("In Constrctor")

    def __del__(self):
        print("In Destructor")

def fun():
    print("In fun")
    obj=Demo()
    print("End fun")
    return obj

retObj=fun()
print("End Code")

# # Output
# In fun
# In Constrctor
# End fun
# End Code
# In Destructor