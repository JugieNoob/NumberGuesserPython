import game

__name__ = "__main__"

def main():
    print("Welcome to Hangman!\n1.Play\n2.How to Play")
    choice = input()
    if (choice == "1"):
        game.main()
    if (choice == "2"):
        howToPlay()

def howToPlay():
    print("Try to guess the word by inputting a character, if the stickman drawing is complete, you lose. If you guess the word, you win!\nPress ENTER to go back to the main menu")
    backtomenu = input()
    main()

if (__name__ == "__main__"):
    main()