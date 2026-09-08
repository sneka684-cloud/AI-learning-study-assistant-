from tools import calculator, attendance_calculator
from memory import ConversationMemory
from rag import KnowledgeBase


class StudentSupportAgent:

    def __init__(self):
        self.memory = ConversationMemory()
        self.knowledge = KnowledgeBase()

    def ask(self, question):
        text = question.lower()

        if "hello" in text or "hi" in text:
            answer = "Hello! Welcome to AI Student Support Assistant. How can I help you?"
            self.memory.add(question, answer)
            return answer, "Agent", "Greeting"

        if "calculate" in text or "plus" in text:
            result = calculator(text)
            answer = "Calculation Result: " + str(result)
            self.memory.add(question, answer)
            return answer, "Tool Calling", "Calculator"

        if "attendance" in text or "percentage" in text:
            answer = attendance_calculator(text)
            self.memory.add(question, answer)
            return answer, "Tool Calling", "Attendance Calculator"

        if "previous" in text or "earlier" in text:
            answer = self.memory.last_answer()

            if answer is None:
                answer = "There is no previous answer in memory."

            return answer, "Memory", "Conversation Memory"

        answer, source = self.knowledge.search(question)
        self.memory.add(question, answer)

        return answer, "RAG", source