class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\nPlease convert %d to binary: " %(base10))
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print("Wrong answer. The correct answer"\
                             " is {:b}.".format(base10))
                        break
                except:
                    print("You did not enter a binary number.Please try again.")
                    userResult = input("\nPlease convert %d tobinary: " %(base10))

        return score

class MathGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:' + ', 2:' - ', 3:'*', 4:'**'}

        for i in range(self.noOfQuestions):
            for index in range(0, 5):
                numberList[index] = randint(1, 9)
# См. объяснение ниже
            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == '**':
                    symbolList[index] = operatorDict[randint(1, 3)]

                else:
                    symbolList[index] = operatorDict[randint(1, 4)]

            questionString = str(numberList[0])
            
            for index in range(0, 4):
                questionString = questionString + symbolList[index] + str(numberList[index+1])

            result = eval(questionString)
            questionString = questionString.replace("**", "^")
            userResult = input("\nPlease evaluate %s:"%(questionString))

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:d}.".format(result))
                        break
                except:
                    print("You did not enter a valid number. Please try again.")
                    userResult = input("\nPlease evaluate %s:"%(questionString))

        return score 
                     
                       
'''
 Начиная со второго элемента (т. е. index = 1) 
в symbolList, строка
 if index > 0 and symbolList[index-1] == '**': 
проверяет, содержит ли
 предыдущий элемент в symbolList оператор **.
 Если содержит, то команда symbolList[index] = 
operatorDict[randint(1, 3)]
 выполняется. В этом случае функции randint передается 
диапазон от 1 до 3.
 Таким образом, оператор **, имеющий ключ 4 
в operatorDict, НЕ БУДЕТ
 присвоен symbolList[index].
 С другой стороны, если предыдущий элемент не содержит 
оператор **, команда
 symbolList[index] = operatorDict[randint(1, 4)] будет 
выполнена. Так как
 функции randint передается диапазон от 1 до 4, будут 
сгенерированы числа
 из набора 1, 2, 3 и 4. А значит, symbolList[index] 
будут присваиваться 
операторы +, -, * и **.
 '''
