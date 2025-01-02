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
            print("Hence, number of questions will be setto 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be setto 10")
        else:
            self._noOfQuestions = value
