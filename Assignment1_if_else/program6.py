#Check whether the character is alphabet or not
# Enter Character:x
# x is an albhabet
print("===========program6===============")
x=input("Enter Character:")

if((ord(x)>=97 and ord(x)<=122) or (ord(x)>=65 and ord(x)<=90)):
	print(x,"is an albhabet")
else:
	print(x,"is not albhabet")


