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
            userResult = input("\nPlease convert %d tobinary: " %(base10))
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
    
                        
                        
