# Output:
# Enter Rows=4
# $  =   $  =
# $  =   $  =
# $  =   $  =
# $  =   $  =

rows=int(input("Enter Rows="))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(j%2!=0):
            print("$",end="  ")
        else:
            print("=",end="   ")
    print()