import random

player="y"

while player=="y":
    
    no=random.randint(1,6)
    
    player ==input("Press y to roll again ")
    
    if no==1:
        print("|---------|")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print("|         |")
        print("|---------|")
    if no==2:
        print("|---------|")
        print("|o        |")
        print("|         |")
        print("|         |")
        print("|        o|")
        print("|---------|")
    if no==3:
        print("|----------|")
        print("|o         |")
        print("|    o     |")
        print("|         o|")
        print("|----------|")
    if no==4:
        print("|---------|")
        print("|o       o|")
        print("|         |")
        print("|         |")
        print("|o       o|")
        print("|---------|")
    if no==5:
        print("|---------|")
        print("|o       o|")
        print("|    o    |")
        print("|         |")
        print("|o       o|")
        print("|---------|")        
            
    if no==6:
        print("|---------|")
        print("|o   o   o|")
        print("|         |")
        print("|o   o   o|")
        print("|---------|")    
        