class Demo:
    def __init__(self):
        print("In Constrctor")

    def __del__(self):
        print("In Destructor")

obj1=Demo()
obj2=obj1
obj3=obj1
