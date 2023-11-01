#Take an integer ranging fom 0 to 6 & print corresponding weekday  
# Enter Value:2
# Wednesday
print("===========program5===============")
days=['Monday','Tuesday','Wednesday','Thuresday','Firday','Saturday','Sunday']

i=int(input("Enter Value:"))
for n in range(0,7):
	if(n==i):
		print(days[n])
	
