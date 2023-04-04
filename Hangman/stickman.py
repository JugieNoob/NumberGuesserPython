__name__ = "__stickman__"

global stickman
stickman = ["|\n|\n|\n|\n|", "--------------\n|\n|\n|\n|\n|", "--------------\n|\tO\n|\n|\n|\n|", "--------------\n|\tO\n|\t|\n|\n|\n|", "--------------\n|\tO\n|      /|\n|\n|\n|", "--------------\n|\tO\n|      /|\ \n|\n|\n|", "--------------\n|\tO\n|      /|\ \n|      /\n|\n|", "--------------\n|\tO\n|      /|\ \n|      / \ \n|\n|"]


def firstStickman():
    print(stickman[0])

def updateStickman(curstickman):
    print(stickman[curstickman])
