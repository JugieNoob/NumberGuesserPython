import handler
import time



def main():
    global choice
    global chosenopt
    print("Welcome to Rock Paper Scissors!\nPress 1. to choose ROCK\nPress 2. to choose PAPER\nPress 3. to choose SCISSORS")
    choice = input()
   
    if (choice.isdigit):
        match(choice):
            case "1":
                chosenopt = "ROCK"
            case "2":
                chosenopt = "PAPER"
            case "3":
                chosenopt = "SCISSORS"  
    
    print("Rock,")
    time.sleep(0.5)
    print("Paper,")
    time.sleep(0.5)
    print("Scissors,")
    time.sleep(0.5)
    print("Shoot!")
    time.sleep(0.25)
    handler.opponentChoice()
    print("You picked: " + chosenopt)  
    print("Your opponent chose: " + handler.optionstr)   
    playerWon()


        
def playerWon():
    if (chosenopt == "ROCK" and handler.optionstr == "PAPER"):
        print("You Lose! :(")

    elif (chosenopt == "ROCK" and handler.optionstr == "SCISSORS"):
       print("You Win! :D")
    
    if (chosenopt == "PAPER" and handler.optionstr == "SCISSORS"):
        print("You Lose! :(")
    elif (chosenopt == "PAPER" and handler.optionstr == "ROCK"):
       print("You Win! :D")
    
    if (chosenopt == "SCISSORS" and handler.optionstr == "ROCK"):
        print("You Lose! :(")
    elif (chosenopt == "SCISSORS" and handler.optionstr == "PAPER"):
        print("You Win! :D")
    
    if (chosenopt ==  handler.optionstr):
        print("Draw!")


if __name__ == "__main__":
    main()