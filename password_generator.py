import random , string

User = int(input("Size of the password"))
pro = int (input("level of password"))

if(pro==1):
    password_char=string.ascii_letters + string.digits
    

else:
    password_char=string.ascii_letters + string.digits + string.punctuation
    


password=[]

for x in range(User):
    password.append(random.choice(password_char))
print("".join(password))    
     