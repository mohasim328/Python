def finder(x,y,z):
    
    if(x>y and x>z):
        print("the  greast number in these",x)
    elif(y>x and y>z):
        print("the  greast number in these",y)
    else:
        print("the  greast number in these",z)    
i =int(input("enter 1 : "))
j =int(input("enter 2 : "))
k =int(input("enter 3 : "))
a = finder(i,j,k)
print(a)