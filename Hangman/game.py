import sys
import stickman
import wordshandler

__name__ = "__game__"

blankfields = []
wordtoarray = []
incorrectletters = []
disallowedcharacters = "!@#$%^&*()-+?_=,<>/"

word = wordshandler.fetchWord()

def main():
    stickman.firstStickman()

    for i in range(len(word)):
        blankfields.append('_')
        wordtoarray.append(word[i].upper())

    
    print(blankfields)
    while True:
        checkWin()
        if (not checkWin()):
            allowGuess()
                 
            checkLose()     
            print(blankfields)
            print("Wrong words:" + str(incorrectletters))
            checkWin()
            
            
def checkWin():
    for i in range(len(word)):
        if (wordtoarray == blankfields):
            sys.exit("---------YOU WIN---------")
            return True
        
def checkLose():
    if (len(incorrectletters) >= len(stickman.stickman) - 1):
        sys.exit("---------YOU LOSE---------\nThe word was: " + word)       

def allowGuess():
        guess = input()
        if (len(guess) < 2 and not guess.isdigit() and guess.isalnum()):
            for i in range(len(word)):
                if (guess.lower() == word[i].lower()):
                    blankfields.pop(i)
                    blankfields.insert(i, guess.upper())
                    stickman.updateStickman(len(incorrectletters))
                elif guess.lower() not in word:
                    if (guess.lower() not in incorrectletters):
                        incorrectletters.append(guess)
                        stickman.updateStickman(len(incorrectletters))
                        break
                    else:
                        print("You have already tried that letter, please try again.")
                        break
                        allowGuess()
        elif not guess.isalnum():
           print("Do not enter any special characters, only enter an alphabetical character!")
           allowGuess()                
        elif len(guess) > 1:
            print("Only enter one character!")
            allowGuess()
        elif int(guess) == guess.isdigit():
            print("Do not enter an integer value, only enter an alphabetical character!")
            allowGuess()
       
            
        