num=int(input("Enter num value"))

rev=0

while(num>0):

 rem=num%10

 rev=(rev*10)+rem

 num=num/10

print ("reverse value:",rev)
 
if(num==rev):

  print ("Yes")

if(num!=rev):

 print ("No")