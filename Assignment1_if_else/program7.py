#Take number of month and print number of days in that month
print("===========program7===============")

month=int(input("Enter number of month"))
if(month<=12 and month>0):
   if(month==1):
     print("January is 31 days month")
   elif(month==2):
     print("February is 28 days month")
   elif(month==3):
     print("March is 31 days month")
   elif(month==4):
     print("April is 30 days month")
   elif(month==5):
     print("May is 31 days month")
   elif(month==6):
     print("June is 30 days month")
   elif(month==7):
     print("July is 31 days month")
   elif(month==8):
     print("August is 31 days month")
   elif(month==9):
     print("September is 30 days month")
   elif(month==10):
     print("October is 31 days month")
   
   elif(month==11):
     print("November is 30 days month")
   else: 
     print("December is 31 days month")
else:
   print("Invalid Month")