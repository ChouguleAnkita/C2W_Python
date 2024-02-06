"""Enter rows=4
1  1  1  1
2  2  2  2
3  3  3  3
4  4  4  4
"""
rows=int(input("Enter rows="))

for i in range(rows):
    for j in range(rows):
        print(i+1, end="  ")
    print()