# Output
# 1
# 2 2
# 3 3 3
# 4 4 4 4

rows=int(input("Enter Rows="))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ")    
    print()

