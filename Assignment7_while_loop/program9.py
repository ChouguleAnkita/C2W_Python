# Armsstrong number =371=3*3*3 + 7*7*7 + 1*1*1
num=int(input("Enter number="))
n=num
count=0
result=0
while(n!=0):
    count=count+1
    n=n//10

n=num
while(n!=0):
    rem=n%10
    result=result+(rem**count)
    n=n//10

if(num==result):
    print(num," is a armstrong number")
else:
    print(num," is not armstrong number")
