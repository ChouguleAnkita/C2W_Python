# Output
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

rows=int(input("Enter Rows="))
for i in range(1,rows+1):
    x=rows
    for j in range(1,i+1):
        print(x,end=" ")  
        x=x-1  
    print()

