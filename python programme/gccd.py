
def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return x
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(2, 2))
print(gcd(4, 6))
