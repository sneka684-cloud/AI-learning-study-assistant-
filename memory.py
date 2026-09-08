class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, question, answer):
        self.history.append({
            "question": question,
            "answer": answer
        })

    def last_answer(self):
        if self.history:
            return self.history[-1]["answer"]

        return None

    def clear(self):
        self.history.clear()