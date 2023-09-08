def sumof(n):
    sum=0
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:  
       return n+sumof(n-1)
x = int(input("enter a number"))
y = sumof(x)
print(y)  
   
sum =0
for i in range(1,x+1):
    sum+=i
print(sum) 