# Output:
# E D C B A
# E D C B A
# E D C B A
# E D C B A
# E D C B A


rows=5 #int(input("Enter Rows="))

for i in range(1,rows+1):
    x=69
    for j in range(1,rows+1):
        print(chr(x),end=" ")
        x=x-1
    print()