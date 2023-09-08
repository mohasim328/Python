def fact(n):
    if(n==0):
        return 1
    elif(n==1):
        return n    
    else:
      return n*fact(n-1) 
s =int(input("enter a number : ")) 
sum = fact(s)        
print("factorial is : ",sum)      