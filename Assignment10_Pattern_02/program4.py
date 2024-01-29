# Output
# 2 5 10
# 17 26 37
# 50 65 82

rows=int(input("Enter Rows="))
x=1
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print((x*x)+1,end=" ")
        x=x+1
    print()

