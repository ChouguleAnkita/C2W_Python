"""Enter rows=3
1  3  5
1  3  5
1  3  5
"""
rows=int(input("Enter rows="))
for i in range(rows):
    num=1
    for j in range(rows):
        print(num, end="  ")
        num=num+2
    print()