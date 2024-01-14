def outer():
    def inner(outer):
        print(outer)
        return inner
    return inner(outer)

if __name__=='__main__':
    retObj=outer()
    print(retObj)

#Output
# <function outer at 0x000000BE47C904A0>  #address of outer function
# <function outer.<locals>.inner at 0x000000BE47DE8E00>  # address of inner Function