print("Amstrong number")

for x in range(1,700):

 num=x

 ams=0

 while(num>0):

  dig=num%10

  ams+=dig**3

  num=num/10

 if(x==ams):

  print (x)
 