"""Enter rows=3
1  3  5
7  9  11
13  15  17
"""
rows=int(input("Enter rows="))
num=1
for i in range(rows):
    for j in range(rows):
        print(num, end="  ")
        num=num+2
    print()