"""Enter rows=3
1  3  5  7
5  7  9  11
9  11  13  15
13  15  17  19
"""
rows=int(input("Enter rows="))
for i in range(rows):
    num=rows*i+1
    for j in range(rows):
        print(num, end="  ")
        num=num+2
    print()