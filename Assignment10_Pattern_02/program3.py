# Output:
# A B C D
# A B C D
# A B C D
# A B C D

rows=4 #int(input("Enter Rows="))

for i in range(1,rows+1):
    x=65
    for j in range(1,rows+1):
        print(chr(x),end=" ")
        x=x+1
    print()
