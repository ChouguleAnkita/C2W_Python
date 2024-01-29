# Output:
# 1  2   9  4
# 25  6   49  8
# 81  10   121  12
# 169  14   225  16

rows=int(input("Enter Rows="))
x=1
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(x%2!=0):
            print(x*x,end="  ")
        else:
            print(x,end="   ")
        x=x+1
    print()

