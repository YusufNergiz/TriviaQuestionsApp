import tkinter
from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz_brain

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.score_label.config(font=("Arial",15,"italic"))
        self.score_label.config(padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="SOme text here", font=("Arial",20,"italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = PhotoImage(file=r"C:\Users\yusuf\PycharmProjects\TriviaQuestionsApp\quizzler-app-start\images\true.png")
        self.right_button = Button(image=true_image, command=self.check_if_answer_true)
        self.right_button.config(highlightthickness=0)
        self.right_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file=r"C:\Users\yusuf\PycharmProjects\TriviaQuestionsApp\quizzler-app-start\images\false.png")
        self.false_button = Button(image=false_image, command=self.check_if_answer_false)
        self.false_button.config(highlightthickness=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)


        exit_image = PhotoImage(
           file=r"C:\Users\yusuf\PycharmProjects\TriviaQuestionsApp\quizzler-app-start\images\exit_image_50.png")
        self.exit_button = Button(image=exit_image, command=self.window.destroy)
        self.exit_button.config(highlightthickness=0, height=100, width=50)
        self.exit_button.grid(row=0, column=0)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.right_button["state"] = "active"
            self.false_button["state"] = "active"
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")


    def check_if_answer_true(self):
        self.right_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.give_feedback(self.quiz.check_answer("true"))

    def check_if_answer_false(self):
        self.right_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def end_game(self):
        if self.quiz.still_has_questions() == False:
            print("The game is over!")
        else:
            pass

















