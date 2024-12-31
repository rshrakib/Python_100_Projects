import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = [
            {'question': "What is the capital of Bangladesh?",
             'choice': ["London", "Dhaka", "Delhi", "Rome"],
             'correct_answer': "Dhaka"
             },
            {'question': "What is the capital of Pakistan?",
             'choice': ["London", "Dhaka", "Karachi", "Rome"],
             'correct_answer': "Karachi"
             },
            {'question': "What is the capital of France?",
             'choice': ["London", "Dhaka", "Paris", "Rome"],
             'correct_answer': "Paris"
             }
        ]
        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.choices = []
        for i in range(4):
            choice = tk.Radiobutton(root, text="", variable=self.radio_var, value="", font="Arial 12", anchor='w')
            choice.pack(pady=10, anchor='w')
            self.choices.append(choice)


        self.next_button = tk.Button(root, text="Next", command=self.next_question, font="Arial 12", bg="green", fg="white")
        self.next_button.pack(pady=20)

        self.display_questions()

    def display_questions(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data['question'])
            for i, choice in enumerate(self.choices):
                choice.config(text=question_data['choice'][i], value=question_data['choice'][i])

            self.radio_var.set("")
        else:
            self.show_result()

    def next_question(self):

        selected_choice = self.radio_var.get()
        if not selected_choice:
            messagebox.showwarning("Warning", "Please select an option")
        else:
            if selected_choice == self.questions[self.question_index]['correct_answer']:
                self.score += 1
            self.question_index += 1
            self.display_questions()

    def show_result(self):
        """Displays the final score and exits the application."""
        messagebox.showinfo("Quiz Result", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
