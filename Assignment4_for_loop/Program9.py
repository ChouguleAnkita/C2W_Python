start=int(input("Enter start of range=")) 
end=int(input("Enter end of range=")) 

print("Cound of Negative Numbers from given range:")
count=0
for i in range(start,end):
    if(i<0):
        count+=1
print(count)
