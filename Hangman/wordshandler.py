import json
import random

global words_list

with open('words.json', 'r') as words_file:
    words_list = json.load(words_file)
    
def fetchWord():
    wordpos = random.randint(0, 99)
    return words_list['possiblewords'][wordpos]

