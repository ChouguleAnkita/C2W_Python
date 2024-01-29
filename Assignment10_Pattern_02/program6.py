# Output:
# 1   4   7   10
# 2   5   8   11
# 3   6   9   12
# 4   7   10   13

rows=int(input("Enter Rows="))

for i in range(1,rows+1):
    x=i
    for j in range(1,rows+1):
        print(x,end=" ")
        x=x+3
    print()
