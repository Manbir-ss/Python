def summy(x,y,z):

    sum=x+y+z
    if x==y==z:
        sum=sum*3
    return sum

x=int(input("Enter first number: "))
y=int(input("ENter second number: "))
z=int(input("Enter third number: "))
pg=summy(x,y,z)
print(pg)