import random

print("Welcome to the number guesser! Input a range of numbers!")
print("Range One:")
rangeone = input()
print("Range Two:")
rangetwo = input()


if (rangeone.isdigit and rangetwo.isdigit):
    randomint = random.randint(int(rangeone), int(rangetwo))
    print("Guess the number!")
    guess = input()
    if (guess.isdigit):
        if (int(guess) == int(randomint)):
            print("Correct! \nGuess:" + str(guess) + "\nRandom Number:" + str(randomint))
        else:
            print("Incorrect! \nGuess:" + str(guess) + "\nRandom Number:" + str(randomint))
    else:
        print("Error: Please enter an integer!")
else:
    print("Error: Please enter two integers!")