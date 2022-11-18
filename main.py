# ___________________________imports_____________________________________________
from tkinter import *
import pandas
import random

# ___________________________ Constant____________________________________________
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
# word_choice = {}

# ___________________________ Working with data__________________________________
data = pandas.read_csv("./data/french_words.csv")
data2 = data.to_dict(orient="records")

word_choice = random.choice(data2)


# ___________changing word after button pressed_______________________
def flip_back():
    print(word_choice["English"], word_choice["French"])
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(language_name, text="English", fill="white")
    canvas.itemconfig(french_word, text=word_choice["English"], fill="white")


def flip_front():
    global word_choice, flip_timer
    root.after_cancel(flip_timer)
    word_choice = random.choice(data2)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(language_name, text="French", fill="black")
    canvas.itemconfig(french_word, text=word_choice["French"], fill="black")
    flip_timer = root.after(3000, func=flip_back)


# ___________________________ Creating Window____________________________________
root = Tk()
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = root.after(3000, func=flip_back)

# ___________________________ Creating Button____________________________________
# Right Button
right_image = PhotoImage(file="./images/right.png")         # Converting image to supported format
right_button = Button(image=right_image, highlightthickness=0, border=0, command=flip_front)
# For removing border from button use "highlightthickness=0, border=0"
right_button.grid(column=1, row=1)

# Wrong Button
wrong_image = PhotoImage(file="./images/wrong.png")         # Converting image to supported format
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=flip_front)
# For removing border from button use "highlightthickness=0, border=0"or bd=0 or borderwith =0
wrong_button.grid(column=0, row=1)


# ___________________________ Creating Canvas____________________________________
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Front Canvas
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)


# Creating texts in canvas
language_name = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
french_word = canvas.create_text(400, 263, text=word_choice["French"], font=WORD_FONT)


root.mainloop()




