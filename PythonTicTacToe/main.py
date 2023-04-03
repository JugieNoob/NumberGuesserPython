#

__name__ = "__main__"

def menu():
    print("Welcome to Tic Tac Toe\n1. Play\n2. How to play")
    choice = input()
    if (choice == "1"):
      import gamelogic
      print("Amogn")
    elif (choice == "2"):
        howToPlay()

def howToPlay():
    print("1. Choose a row to place your tile\n2.Choose a column to place your tile \n\nPress ENTER to go back to the menu")
    choice = input()
    menu()

if __name__ == "__main__":
    menu()