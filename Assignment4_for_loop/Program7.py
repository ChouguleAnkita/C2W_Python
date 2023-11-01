
start=int(input("Enter start of range=")) 
end=int(input("Enter end of range="))  
print("All Positive Numbers from given range:")
for i in range(start,end):
    if(i>0):
        print(i,end="  ")
print()