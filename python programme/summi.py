def sum(a,b,c):
    if(a==b) or (b==c) or (c==a):
        sum=0
        return sum
    else:
        sum=a+b+c
        return sum

print(sum(2,3,6))
print(sum(6,2,6))            