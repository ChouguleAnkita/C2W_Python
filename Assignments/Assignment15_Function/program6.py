def outer():
    def inner1(a,b):
        print("In inner1")
        return a-b
    def inner2(obj):
        print("In inner2")
        print(obj)
        return inner2
    
    retInner1=inner1(10,4)
    retInner2=inner2(retInner1)
    return retInner2

if __name__=='__main__':
    retObj=outer()
    print(retObj)
    
# Output
# In inner1
# In inner2
# 6
# <function outer.<locals>.inner2 at 0x0000001722278EA0>