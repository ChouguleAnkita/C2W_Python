start=int(input("Enter start of range=")) 
end=int(input("Enter end of range="))  

print("Numbers divisible 7 and not by 3 from given range:")

for i in range(start,end):
    if(i%7==0 and i%3!=0):
        print(i,end="  ")
print()