"""Enter rows=3
1  3  5
3  5  7
5  7  9
"""
rows=int(input("Enter rows="))
for i in range(rows):
    num=i+i+1
    for j in range(rows):
        print(num, end="  ")
        num=num+2
    print()