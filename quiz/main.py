from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

should_quiz_continue = True

while should_quiz_continue:
    quiz_brain.next_question()
    if not quiz_brain.still_has_questions():
        should_quiz_continue = False

print("You've completed the Quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
