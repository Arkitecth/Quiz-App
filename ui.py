from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
font = ("Arial 20 italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        self.score_label = Label(
            text=f"Score: {self.quiz.score}", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightbackground=THEME_COLOR)

        self.q_text = self.canvas.create_text(
            150, 125, text="Amazon acquired Twitch in August 2014 for $970 million dollars.", font=font, width=270, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.check_button = Button(image=true_image, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)
        self.cross_button = Button(
            image=false_image, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.q_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.window.after(1000, self.canvas.config(bg="Green"))
        else:
            self.window.after(1000, self.canvas.config(bg="red"))

        self.window.after(1000, self.get_next_question)
