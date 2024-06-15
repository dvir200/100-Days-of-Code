from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
  question_bank.append(Question(item.get("text"), item.get("answer")))

question_counter = 1

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

quiz.end_game()