class quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_q(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number +=1
        user_ans = input(f"Q.{self.question_number}: {current_q.text} is True or False? ")
        self.check_ans(user_ans, current_q.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score +=1
            print("U are right")
        else:
            print("Ya wrong")
        print(f"The correct ans was: {correct_ans}")
        print(f"Your score is {self.score}/{self.question_number}")
