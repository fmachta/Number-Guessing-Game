import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame(tk.Frame):
    def __init__(self, parent, controller, min_val, max_val):
        super().__init__(parent)
        self.controller = controller
        self.min = min_val
        self.max = max_val

        self.random_num = random.randint(self.min, self.max)

        tk.Label(
            self, text=f"Guess a number between {self.min} and {self.max}:", font=("Helvetica", 20)
        ).pack(pady=20)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=0)

        self.guess_entry = tk.Entry(self, font=("Helvetica", 20))
        self.guess_entry.pack(pady=0)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=20)

        self.return_button = tk.Button(self,text="⏎",font=("Ariel", 10), command=lambda: controller.show_frame(EnterNumbers),)
        self.return_button.place(x=5, y=170)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid integer!")
            return

        if guess < self.min or guess > self.max:
            self.result_label.config(
                text="Number not within range, try again", fg="red"
            )
            return

        if self.random_num > guess:
            self.result_label.config(text="Too Small!", fg="white")
        elif self.random_num < guess:
            self.result_label.config(text="Too Big!", fg="white")
        else:
            self.result_label.config(text="YOU GOT IT", fg="green")
            messagebox.showinfo("Congratulations", "YOU GOT IT!")

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Guessing Game!", font=("Helvetica", 20))
        label.pack(pady= 10, padx=50)
        
        label2 = tk.Label(self, text="Click Start to Begin", font=("Helvetica", 10))
        label2.pack(padx=50,pady=(20,0))

        button = tk.Button(
            self,
            text="Start",
            command=lambda: controller.show_frame(EnterNumbers),
        )
        button.pack()

class EnterNumbers(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Enter Numbers",font=("Ariel",20,"bold" ))
        self.label.pack(pady=0, padx=0)

        self.label = tk.Label(self, text="Enter a range of numbers to guess from:",font=("Ariel",10))
        self.label.pack(pady=(0, 5), padx=0)

        self.label_min = tk.Label(self, text="Minimum").pack()
        
        self.min_entry = tk.Entry(self, font=("Helvetica", 12))
        self.min_entry.pack()

        self.label_max = tk.Label(self, text="Maximum").pack()

        self.max_entry = tk.Entry(self, font=("Helvetica", 12))
        self.max_entry.pack()

        self.submit_button = tk.Button(self, text="Continue", font=("Ariel", 10), command=self.sendNum)
        self.submit_button.pack()

        self.return_button = tk.Button(self,text="⏎",font=("Ariel", 10), command=lambda: controller.show_frame(StartPage),)
        self.return_button.place(x=5, y=170)
    def sendNum(self):
        try:
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
            self.controller.update_guessing_range(min_val, max_val)
        except ValueError:
            self.label.config(text="Please enter a valid integer!", font=("Ariel",10,"bold"))
            return

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guessing Game")
        self.geometry("400x200")
        self.eval("tk::PlaceWindow . center")
        self.resizable(False, False)

        self.min = 0
        self.max = 100

        self.frames = {}
        for F in (StartPage, EnterNumbers):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[GuessingGame] = GuessingGame(self, self, self.min, self.max)
        self.frames[GuessingGame].grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    def update_guessing_range(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
        self.frames[GuessingGame] = GuessingGame(self, self, self.min, self.max)
        self.frames[GuessingGame].grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
