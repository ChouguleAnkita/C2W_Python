"""Enter rows=4
#  #  #  #  #
@  @  @  @  @
#  #  #  #  #
@  @  @  @  @
#  #  #  #  #
"""
rows=int(input("Enter rows="))

for i in range(rows):
    for j in range(rows):
        if(i%2==0):
            print("#", end="  ")
        else:
            print("@", end="  ")
    print()