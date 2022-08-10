import random
def lose():

    word = random.choice(["ironman" , "hulk" , "thor" , "captainamerica" , "clint" , "loki" , "avengers" , "nick" , "antman" , "marvel" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 8
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

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
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 7:
                print("7 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
            if turns == 6:
                print("6 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")

            if turns == 5:
                print("5 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")

                print ("  - - - - ")
                print(" |       | ")
                print(" |       | ")
               

            if turns == 4:
                print("4 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")
                
                print ("  - - - -")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print("  - - - - ")
              

                
            if turns == 3:
                print("3 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")
                
                print ("  - - - -")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print("  - - - -  ")
                
                print(" _ _ _ _ ")
                print("| ")
                print("| ")
                print(" - -")
                
               
                

                
            if turns == 2:
                print("2 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")
                
                print ("  - - - - ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print("  - - - -  ")
                
                print(" _ _ _ _ ")
                print("| ")
                print("| ")
                print(" - - - -")
                print("        |")
                print("        |")
                print(" - - - - ")
                
                

                
            if turns == 1:
                print("1 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")
                
                print ("  - - - - ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print("  - - - -  ")
                
                print(" _ _ _ _ ")
                print("| ")
                print("| ")
                print(" - - - -")
                print("        |")
                print("        |")
                print(" - - - - ")
                
                print(" - - - -")
                print("|")
                print("|")
                print("|- - ")
                
                
            if turns == 0:
                print("0 turns left")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" | ")
                print(" - - - - ")
                
                print ("  - - - - ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print(" |       | ")
                print("  - - - -  ")
                
                print(" _ _ _ _ ")
                print("| ")
                print("| ")
                print(" - - - -")
                print("        |")
                print("        |")
                print(" - - - - ")
                
                print(" - - - -")
                print("|")
                print("|")
                print("|- - - ")
                print("|")
                print("|")
                print(" - - - -")
                print("SORRY..!")
                print("YOU LOST THE GAME...!")
            
                break
               

name = input("Enter your name")
print("Welcome to the game" , name )
print("try to guess the word in less than 10 attempts")
lose()
print()
