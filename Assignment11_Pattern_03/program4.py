# Output
# 1 1 1 1
# 2 2 2
# 3 3
# 4

rows=int(input("Enter Rows="))
for i in range(1,rows+1):
    for j in range(0,rows+1-i):
        print(i,end=" ")  
    print()

