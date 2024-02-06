"""Enter rows=4
1  2  3  4
1  2  3  4
1  2  3  4
1  2  3  4
"""
rows=int(input("Enter rows="))

for i in range(rows):
    for j in range(rows):
        print(j+1, end="  ")
    print()