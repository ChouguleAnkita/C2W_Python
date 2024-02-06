start=int(input("Enter start of range=")) 
end=int(input("Enter end of range="))   

print("All character values from given ASCII value range:")

if(start>=65 and end<=91):
    for i in range(start,end):
        print("The Character of ASCII value {} is {}".format(i,chr(i)))
else:
    print("Wrong Input")

