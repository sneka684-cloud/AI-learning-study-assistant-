class KnowledgeBase:

    def __init__(self):
        self.knowledge = {
            "rag": "RAG stands for Retrieval-Augmented Generation. It retrieves relevant information from a knowledge base to answer user questions.",
            
            "agentic ai": "Agentic AI is an AI system that can understand a task, make decisions and use suitable tools or information to complete the task.",
            
            "tool calling": "Tool Calling allows an AI agent to use a specific function such as a calculator or attendance calculator.",
            
            "memory": "Memory allows an AI agent to retain useful information from previous interactions.",
            
            "python": "Python is a high-level programming language used for software development, automation and artificial intelligence.",
            
            "github": "GitHub is a platform used to store, manage and share source code using Git.",
            
            "streamlit": "Streamlit is a Python framework used to create interactive web applications."
        }

    def search(self, question):

        question = question.lower()

        for keyword, answer in self.knowledge.items():

            if keyword in question:
                return answer, "Knowledge Base"

        return "Sorry, I could not find relevant information.", "Knowledge Base"