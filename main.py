from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

root = Tk()
root.title("Flash card App")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# ___________________________ Creating Button____________________________________
# Right Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

# Wrong Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)


# _______________________Canvas creating__________________________________


root.mainloop()



