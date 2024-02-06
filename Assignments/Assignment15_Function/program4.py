def outer():
    def inner():
        return outer
    return inner

if __name__=='__main__':
    retObj=outer()
    retInner=retObj()
    print(retInner)

# Output
    # <function outer at 0x000000A8CE5F04A0>