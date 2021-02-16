import random
press = "y"
print("**Welcome to play roll the dice !!**")
print("<< Press Y to roll >>")
print(">> Any other key to discontinue <<")
press = input()

while(press == "y" or press == "Y"):
    x = random.randint(1 , 6)
    print("------------")
    if x == 1:
        print("|           |")
        print("|     *     |")
        print("|           |")
    elif x == 2:
        print("|           |")
        print("|  *     *  |")
        print("|           |")
        
    elif x ==3:
        print("|     *     |") 
        print("|  *     *  |")
        print("|           |")
    elif x ==4:
        print("|  *     *  |")
        print("|           |")
        print("|  *     *  |")
    elif x ==5:
        print("|  *     *  |")
        print("|     *     |")
        print("|  *     *  |")
    elif x==6:
        print("|  *     *  |")
        print("|  *     *  |")
        print("|  *     *  |")
    print("------------")
    print("It's a " , x , "!")

    print("<< Press Y to roll again >>")
    print(">> Any other key to discontinue <<")
    press = input()
print("***Thank you for playing!!***")
print(".....We hope that you enjoyed it !!.....")





