# Output
# Enter Rows=4
# 1 2 3 4
# 1 2 3
# 1 2
# 1

rows=int(input("Enter Rows="))

for i in range(1,rows+1):
    for j in range(0,rows+1-i):
        print(j+1,end=" ")  
    print()

