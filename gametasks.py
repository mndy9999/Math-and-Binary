from os import remove, rename

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        file=open("userScores.txt", "r")
        for line in file:
            content = line.split(", ")
            if content[0] == userName:
                file.close()
                return content[1]
        file.close()
        return -1
    except:
        file=open("userScores.txt", "w")


def updateUserScore(newUser, userName, score):
    if newUser == True:
        file = open("userScores.txt", "a")
        file.write(userName + ", " + score + "\n")
        file.close()
    else:
        temp_file = open("userScores.tmp", "w")
        file = open("userScores.txt", "r")
        for line in file:
            content = line.split(", ")
            if content[0] == userName:
                temp_file.write(userName + ", " + score + "\n")
            else:
                temp_file.write(line + "\n")
        temp_file.close()
        file.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")
