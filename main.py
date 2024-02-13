from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

on = True
question_bank = [Question(data['text'], data['answer']) for data in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
