from random import randint

class Game:
    def __init__(self, number_of_questions = 10):
        self._number_of_questions = number_of_questions

    @property
    def numberOfQuestions(self):
        return self._number_of_questions

    @numberOfQuestions.setter
    def numberOfQuestions(self, value):
        if value < 1:
            self._number_of_questions = 1;
            print("Minimum number of questions is 1")
        elif value > 10:
            self._number_of_questions = 10
            print("Maximum number of questions is 10")
        else:
            self._number_of_questions = value

class BinaryGame(Game):
    def generateQuestions(self):
        score = 0;
        for i in range(self.numberOfQuestions):
            base10 = randint(1, 100)
            print(base10, end=" ")
            answer = input("in binary is ")
            binary = "{0:b}".format(base10)
            if answer == binary:
                print("CORRECT! \n-------------------------- \n")
            else:
                print("INCORRECT!")
                print(base10, "in binary is ", binary, "\n-------------------------\n")

            