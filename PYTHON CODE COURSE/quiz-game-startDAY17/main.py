from question_model import question
from data import question_data
from quiz_brain import quizbrain
question_bank = []
for everyquestion in question_data:
    question_text = everyquestion["question"]
    question_ans = everyquestion["correct_answer"]
    new_question = question(question_text, question_ans)
    question_bank.append(new_question) #add new question into the questionbank list

quiz= quizbrain(question_bank)

while quiz.still_has_q():
    quiz.next_question()

print("You have done all the questions!!!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

