# Output
# 1
# 3 5
# 7 9 11
# 13 15 17 19

rows=int(input("Enter Rows="))
x=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(x,end=" ")  
        x=x+2 
    print()

