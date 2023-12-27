#Strong number=sum of factorial of digits e.g 145= 1! + 4! + 5!
num=int(input("Enter number="))
fact=1
sumFact=0
n=num
while(n!=0):
    rem=n%10
    while(rem>=1):
        fact=fact*rem
        rem-=1
    
    sumFact=sumFact+fact
    n=n//10
    fact=1

if(num==sumFact):
    print(num," is a Strong number")
else:
    print(num," is not Strong number")
