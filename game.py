import time
import random


def time_Pause(message):
    print(message)
    time.sleep(2)


def conditions():
    time_Pause("Hello here in this game !!")
    time_Pause("there are six doors numbered from 1 to 6")
    time_Pause("and there are 3 ghosts behind 3 of these doors.")
    time_Pause("try your luck to scape from these ghosts\nLet's START !!\n\n")


def ghost():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    while (x == y or x == z or y == z):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = random.randint(1, 6)
    return [x, y, z]


def master():
    conditions()
    bol = True
    while bol:
        catch = ghost()
        luck = input("Enter a number from 1 to 6 : ")
        check = "123456"
        while True:
            if luck in check:
                luck = int(luck)
                break
            else:
                luck = input("wrong, Enter a number from 1 to 6 : ")
        r = range(1, 7)
        while bol:
            if luck not in catch:
                print("Good luck you scaped from the ghost")
                break
            elif luck in catch:
                print("Hard luck the ghost chatched you.....!")
                break
        end = input("If you want to play again pree 1, or 0 to exit : ")
        while True:
            if end == "0" or end == "1":
                end = int(end)
                break
            else:
                end = input("wrong, to play again pree 1, or 0 to exit : ")
        fine = True
        while fine:
            if end == 0:
                fine = False
                bol = False
                print("THE GAME IS ENDED")
                break
            elif end == 1:
                bol = True
                fine = False
                break


master()
