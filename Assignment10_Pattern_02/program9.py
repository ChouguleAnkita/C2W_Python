# Output:
# A  b   C
# d   E  f
# G  h   I

rows=int(input("Enter Rows="))
x=65
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(x%2!=0):
            print(chr(x),end="  ")
        else:
            print(chr(x+32),end="   ")
        x=x+1
    print()

