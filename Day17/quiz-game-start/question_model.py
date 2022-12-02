class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("Where is O'Hare Airport?\n", "... Chicago ...")
print(new_q.text, new_q.answer)
new_q_2 = Question("Where is Lahore?\n", "... Pakistan ...")
print(new_q_2.text, new_q_2.answer)
