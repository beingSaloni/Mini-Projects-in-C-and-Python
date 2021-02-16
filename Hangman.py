import random
def hangman():
    word = random.choice([	"Andhra Pradesh", "Arunachal Pradesh" ,  "Assam" ,	"Bihar"  ,"Chhattisgarh" ,"Goa", "Gujarat","Haryana", "Himachal Pradesh" ,"Jharkhand",	"Karnataka","Kerala" ,"Madhya Pradesh",	"Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",	"Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura" ,"Uttar Pradesh" ,"Uttarakhand","West Bengal"])
    turns = 10
    guessmade = ''
    
    while len(word) > 0:
       
        main = ""
        
        word = word.lower()
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input("Enter your letter choice in lower case please .")
        guessmade = guessmade + guess
        print("Guess made are :- " , guessmade)
       
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                print(f"The state was {word}")
                break
    print("Chose :- ")
    print("1. Play again \n2.Exit")
       
name = input("Enter your name ")

print(f"Welcome to hangman game {name} !!"  )
print("Chose :- ")
print("1. Play\n2. Exit")
print("Only lower case alphabets are allowed")
choose = " "
while choose != "2":
    choose = input()
    print("------------------------------------")
    if choose== "1":
        print(f"{name}, you will lose the game if you could not guess the indian state in 10 chances !! \n All the best !!")
        hangman()
    elif choose == "2":
        print("Thank you . Bye . See you soon !!")
    else:
        print("Wrong key entered .")
    
print("------------------------------------")



