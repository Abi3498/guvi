count=0

num=int(input("Enter num value"))

for i in range(1,num+1):

 if(num%i==0):

  count=count+1

print (count)

if(count==2):

 print ("prime")

else:

 print ("No")
 