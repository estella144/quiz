##    quiz - A quiz.
##    Copyright (C) 2023 Oliver Nguyen
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.
##
##    Oliver Nguyen <oliverng2512@icloud.com>

import json

print("Quiz 0.2.0, 2 Mar 2023, by Oliver Nguyen")
print("Test release, Last commit: 9a6e188\n")

NOTICE = """quiz Copyright (C) 2023 Oliver Nguyen
This program comes with ABSOLUTELY NO WARRANTY;
for details go to Settings > License > Disclaimer of Warranty.
This is free software, and you are welcome to redistribute it
under certain conditions;
go to Settings > License > Conditions for details.\n"""

print(NOTICE)

class Quiz:
    """Quiz"""

    def __init__(self, questions):
        x = 0
        for i in questions:
            questions[questions.index(i)] = Question(i[0], i[1].lower())
        self.questions = questions

    def ask(self):
        number_of_questions = len(self.questions)
        correct_answers = 0
        username = input("What is your name? ")
        for i in self.questions:
            x = i.ask()
            if x:
                correct_answers += 1

        percent_correct_answers = (correct_answers / number_of_questions) * 100
        print(username + ", you scored", str(correct_answers)) 
        print("You answered", str(round(percent_correct_answers, 1)) + "% of questions correctly.")
        input("Press ENTER to quit the quiz")

class Question:
    """Question in a quiz"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        print("Question:", self.question, "\nAnswer:", self.answer)

    def ask(self):
        answer = input(self.question + " ")
        if answer == self.answer.lower():
            print("Correct")
            return True
        else:
            print("Incorrect. The answer is", self.answer)
            return False

# Type all answers in lowercase
q_list = [["Do integers have quotes around them? [YES/NO]", "no"],
          ["What is the data type which is True or False called?", "boolean"],
          ["What is the assignment symbol in Python?", "="],
          ["What is a piece of data with a name and value which can change called?", "variable"]]

def json_dump(path):
    return json.dump(path, indent=2)

def read_quiz(quiz_name):
    conf_path = "config.json"
    conf = json_dump(conf_path)
    quizes_path = conf[quizes_path]
    quiz_path = quizes_path + "quizes/" + quiz_name
    quiz = json_dump(quiz_path)
    return Quiz(quiz)

def main_menu():
    print("Main Menu")
    print("[S]tart a Quiz")
    print("S[E]ttings")
    choice = input("> ").lower()

    if choice == "s":
        qn = input("Quiz name: ").lower()
        q = read_quiz(qn)
        q.ask()
        main_menu()
    elif choice == "e":
        pass

q = Quiz(q_list)
q.ask()
