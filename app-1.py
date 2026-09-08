import tkinter as tk
from tkinter import scrolledtext
from agent import StudentSupportAgent


agent = StudentSupportAgent()


def ask_question():
    question = entry.get().strip()

    if not question:
        return

    chat.insert(tk.END, "Student: " + question + "\n")

    answer, capability, source = agent.ask(question)

    chat.insert(
        tk.END,
        "Assistant: " + answer + "\n"
    )

    chat.insert(
        tk.END,
        "Capability: " + capability + " | Source: " + source + "\n\n"
    )

    entry.delete(0, tk.END)


window = tk.Tk()

window.title("AI Student Support Assistant")
window.geometry("750x550")

title = tk.Label(
    window,
    text="AI Student Support Assistant",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)


chat = scrolledtext.ScrolledText(
    window,
    width=85,
    height=22,
    font=("Arial", 11)
)
chat.pack(padx=15, pady=10)


entry = tk.Entry(
    window,
    width=65,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=15, pady=10)


button = tk.Button(
    window,
    text="Ask",
    font=("Arial", 11, "bold"),
    command=ask_question
)
button.pack(side=tk.LEFT)


window.mainloop()