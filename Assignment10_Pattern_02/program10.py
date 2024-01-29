# Output:
# D4 C3 B2 A1
# D4 C3 B2 A1
# D4 C3 B2 A1
# D4 C3 B2 A1

rows=int(input("Enter Rows="))

for i in range(1,rows+1):
    x=68
    i=rows
    for j in range(1,rows+1):
        print("{}{}".format(chr(x),i),end=" ")
        x=x-1
        i=i-1
    print()
