class Question:
    """
    Takes question_text and question_answer and creates a Question object.
    """
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
