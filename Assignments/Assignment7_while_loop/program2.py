#prime number
num=int(input("Enter number:="))#2332

count=0
i=1
while(i<=num):
    if(num%i==0):
        count+=1
    i+=1

if(count==2):
    print(num,"is Prime number")
else:
    print(num,"is not Prime number")
