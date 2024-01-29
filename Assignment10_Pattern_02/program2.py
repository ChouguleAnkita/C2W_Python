# Output:
# A B C
# D E F
# G H I

rows=int(input("Enter Rows="))
x=65
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(chr(x),end=" ")
        x=x+1
    print()
