#perfect number =sum of divisor given number e.g 28=1+2+4+7+14
num=int(input("Enter number:=")) #496
n=num//2
sum=0
while(n>=1):
    if(num%n==0):
        sum+=n
    n=n-1

if(sum==num):
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")

    
    