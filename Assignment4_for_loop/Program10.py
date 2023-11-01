start=1
end=11
count=0
prod=1
print("Product of count of odd Numbers from given range:")

for i in range(start,end):
    if(i%2==1):
        count=count+1
        prod=prod * count
    
print(prod)

#o/p= 45