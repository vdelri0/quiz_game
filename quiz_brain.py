#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're at the end of the quiz

class QuizBrain(object):
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        """Will pull up the question from questions_list"""
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        """Returns False if questions_list has no more questions, else returns True"""
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got It right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
