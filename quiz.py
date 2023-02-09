class Quiz:
    """Quiz"""

    def __init__(self, questions):
        x = 0
        for i in questions:
            questions[questions.index(i, x, x+1)] = Question(i[0], i[1])
        self.questions = questions

    def ask(self):
        for i in self.questions:
            i.ask()

class Question:
    """Question in a quiz"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        print("Question:", self.question, "\nAnswer:", self.answer)

    def ask(self):
        answer = input(self.question + " ")
        if answer == self.answer:
            print("Correct")
        else:
            print("Incorrect. The answer is", self.answer)

q = Question("What is 3*5?", "15")
q.ask()
