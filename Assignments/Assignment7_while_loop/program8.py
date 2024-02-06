#palindrome number
num=int(input("Enter number:="))
rev=0
n=num
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(num==rev):
    print(num," is a palindrome number")
else:
    print(num," is not palindrome number")
