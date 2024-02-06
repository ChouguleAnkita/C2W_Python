"""Enter rows=4
1  2  3  4
2  3  4  5
3  4  5  6
4  5  6  7
"""
rows=int(input("Enter rows="))

for i in range(rows):
    num=i+1
    for j in range(rows):
        print(num, end="  ")
        num=num+1
    print()