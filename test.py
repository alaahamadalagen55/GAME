import time
import random


print("Hello here in this game !!")
time.sleep(2)
print("there are six doors numbered from 1 to 6\nand there are 3 ghosts behind 3 of these doors.")
time.sleep(2)
print("try your luck to scape from these ghosts\nLet's START !!\n\n")
    
    
bol = True
while bol :
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    
    while (x == y or x == z or y == z):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = random.randint(1, 6)
    
    catch = [x,y,z]
    luck = int(input("Enter a number from 1 to 6 : "))
    
    r = range(1,7)
    while bol:
        if luck not in r:
            luck = int(input("Your choice is wrong, please enter a number from 1 to 6 : "))
        elif luck not in catch:
            print("Good luck you scaped from the ghost )
            break
        elif luck in catch: 
            print ("Hard luck the ghost chatched you.....!")
            break
        
    end = int(input("If you want to play again pree 1, or 0 to exit : "))
    fine = True
    while fine :
        if end == 0:
            fine == False
            bol == False
            print("THE GAME IS ENDED")
            break
        elif end==1:
            bol == True
            fine == False
            break
        else :
            end = int(input("If you want to play again pree 1, or 0 to exit : "))
            
    if(end == 0):
        break