def LCM(a,b):
    if a>b:
        z=a
    else:
        z=b
    while(True):
        if(z%a==0) and (z%b==0):
            LCM=z
            break        
        z+=1

    return LCM

print(LCM(78,45))
print(LCM(4,8))        