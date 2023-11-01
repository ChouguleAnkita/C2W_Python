start=input("Enter start of range=")
end=input("Enter end of range=") 

s=ord(start)
e=ord(end)

print("All ASCII values from given character range:")

for i in range(s,e):
    print("ASCII value of {} is {}".format(chr(i),i))