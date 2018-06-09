base=int(input("enter base:"))

exp=int(input("enter exp"))

def power(base,exp):

 if(exp==1):

  return(base)

 if(exp!=1):

  return(base*power(base,exp-1))

print("power of a number:",power(base,exp))
	