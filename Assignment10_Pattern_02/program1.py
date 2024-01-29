# Output
# 1 4 9
# 16 25 36
# 49 64 81

rows=int(input("Enter Rows="))
x=1
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(x*x,end=" ")
        x=x+1
    print()

