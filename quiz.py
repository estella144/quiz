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
