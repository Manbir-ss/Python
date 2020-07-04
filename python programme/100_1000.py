def near(pron):
    return((1000-pron)<=100) or((2000-pron)<=100)
pron=int(input("Enter number: "))

print(near(pron))
