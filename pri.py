count=0
for x in range(1,8):
 num=x
 for i in range(1,num+1):
  if(num%i==0):
   count=count+1
 print (count)
 if(count==2):
  print (num)
 