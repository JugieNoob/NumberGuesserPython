import random
import main

__name__ = "__handler__"

global choice

    

def opponentChoice():
    global optionstr
    choice = random.randint(1, 3)
    
    match(choice):
        case 1:
            optionstr = "ROCK"
            print(optionstr) 
            return optionstr
        case 2:
            optionstr = "PAPER"
            print(optionstr)
            return optionstr
        case 3:
            optionstr = "SCISSORS"
            print(optionstr)
            return optionstr
        case _:
            print("L bozo?")
        
#def playerWon(): Old
#    if (chosenopt == "ROCK" and handler.optionstr == "PAPER"):
#        return False
#
#    elif (chosenopt == "ROCK" and handler.optionstr == "SCISSORS"):
#        return True
#    
#    if (chosenopt == "PAPER" and handler.optionstr == "SCISSORS"):
#        return False
#    elif (chosenopt == "PAPER" and handler.optionstr == "ROCK"):
#        return True
#    
#    if (chosenopt == "SCISSORS" and handler.optionstr == "ROCK"):
#        return False
#    elif (chosenopt == "SCISSORS" and handler.optionstr == "PAPER"):
#        return True
#    
#    if (chosenopt ==  handler.optionstr):
#         return None
#
#    match(playerWon):
#        case True: 
#            print("You Win! :D")
#        case False:
#            print("You Lose! :(")
#        case None:
#            print("Draw!")
#        case _:
#            print("Did not work :(")

