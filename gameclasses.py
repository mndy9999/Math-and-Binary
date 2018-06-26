class Game:
    def __init__(self, number_of_questions = 0):
        self._number_of_questions = number_of_questions

    @property
    def getNumberOfQuestions(self):
        return self._number_of_questions
    def setNumberOfQuestions(self, value):
        if value < 1:
            self._number_of_questions = 1;
            print("Minimum number of questions is 1")
        elif value > 10:
            self._number_of_questions = 10
            print("Maximum number of questions is 10")
        else:
            self._number_of_questions = value
            print("Number of questions: " + value)

class BinaryGame:

