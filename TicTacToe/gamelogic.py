import sys
import time
import random as random

__name__ = "__gamelogic__"

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def startGame():
   
    playerturn()
    
    while True:
        if (checkForAIWin()):
            sys.exit("YOU LOSE!") 
        if (checkForWin()):
            sys.exit("YOU WIN!")
        if (not checkForWin()):
            time.sleep(1.5)          
            aiturn()
        if (not checkForAIWin()):
            playerturn()
    
def playerturn():
    print("Choose a row to place an 'x' at:")
    row = input()
    print("Choose a column to place an 'x' at:")
    column = input()
 

    if (grid[int(row)][int(column)] != ' '):
        print("There is already a value at this position, try again!")
        playerturn()
    else:
        print("Your turn:")
        print("---------------")
        grid[int(row)].pop(int(column))
        grid[int(row)].insert(int(column), "x")
        for i in range(len(grid)):
            print(grid[i])
        print("---------------")    
          
def aiturn():
    row = random.randint(0, 2)
    column = random.randint(0, 2)
   
    if (grid[int(row)][int(column)] != ' '):
       aiturn()
    else:
        print("AI turn:")
        print("---------------") 
        grid[int(row)].pop(int(column))
        grid[int(row)].insert(int(column), "o")
        for i in range(len(grid)):
          print(grid[i])
        print("---------------") 

def checkForWin():
    ##possiblewins = [[['x', None, None], [' ', 'x', ' '], [' ', ' ', 'x']],[[' ', ' ', 'x'], [' ', 'x', ' '], ['x', ' ', ' ']], [['x', 'x', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], ['x', 'x', 'x'], [' ', ' ', ' ']],[['x', ' ', ' '], ['x', ' ', ' '], ['x', ' ', ' ']],[[' ', 'x', ' '], [' ', 'x', ' '], [' ', 'x', ' ']],[[' ', ' ', 'x'], [' ', ' ', 'x'], [' ', ' ', 'x']]]

    possiblewins = [[[grid[0][0], grid[0][1], grid[0][2]], [grid[1][0], grid[1][1], grid[1][2]], ['x', 'x', 'x']],[[grid[0][0], grid[0][1], grid[0][2]], ['x', 'x', 'x'], [grid[2][0], grid[2][1], grid[2][2]]],[['x', 'x', 'x'], [grid[1][0], grid[1][1], grid[1][2]], [grid[2][0], grid[2][1], grid[2][2]]],[['x', grid[0][1], grid[0][2]], [grid[1][0], 'x', grid[1][2]], [grid[2][0], grid[2][1], 'x']], [[grid[0][0], grid[0][1], 'x'], [grid[1][0], 'x', grid[1][2]], ['x', grid[2][1], grid[2][2]]],[['x', grid[0][1], grid[0][2]], ['x', grid[1][1], grid[1][2]], ['x', grid[2][1], grid[2][2]]],[[grid[0][0], 'x', grid[0][2]], [grid[1][0], 'x', grid[1][2]], [grid[2][0], 'x', grid[2][2]]],[[grid[0][0], grid[0][1], 'x'], [grid[1][0], grid[1][1], 'x'], [grid[2][0], grid[2][1], 'x']]] 
   # print(possiblewins[1])
    for i in range(len(possiblewins)):
      
        if grid == possiblewins[i]:
           return True
       
def checkForAIWin():
    aipossiblewins = [[[grid[0][0], grid[0][1], grid[0][2]], [grid[1][0], grid[1][1], grid[1][2]], ['o', 'o', 'o']],[[grid[0][0], grid[0][1], grid[0][2]], ['o', 'o', 'o'], [grid[2][0], grid[2][1], grid[2][2]]],[['o', 'o', 'o'], [grid[1][0], grid[1][1], grid[1][2]], [grid[2][0], grid[2][1], grid[2][2]]],[['o', grid[0][1], grid[0][2]], [grid[1][0], 'o', grid[1][2]], [grid[2][0], grid[2][1], 'o']], [[grid[0][0], grid[0][1], 'o'], [grid[1][0], 'o', grid[1][2]], ['o', grid[2][1], grid[2][2]]],[['o', grid[0][1], grid[0][2]], ['o', grid[1][1], grid[1][2]], ['o', grid[2][1], grid[2][2]]],[[grid[0][0], 'o', grid[0][2]], [grid[1][0], 'o', grid[1][2]], [grid[2][0], 'o', grid[2][2]]],[[grid[0][0], grid[0][1], 'o'], [grid[1][0], grid[1][1], 'o'], [grid[2][0], grid[2][1], 'o']]] 
    for i in range(len(aipossiblewins)):
      
        if grid == aipossiblewins[i]:
           return True       

