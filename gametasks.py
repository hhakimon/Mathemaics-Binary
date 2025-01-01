def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                input.close()
                return content[ 1]
            input.close()
            return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return '-1'