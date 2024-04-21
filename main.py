from pandas import *
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
word_text = {}
words_to_learn_fr = []
words_to_learn_en = []

df = read_csv("french_words.csv")

try:
    datafr = read_csv("Words_to_learn.csv")
except FileNotFoundError:
    words_dict = df.to_dict(orient='records')
    print(words_dict)
else:
    words_dict = datafr.to_dict(orient='records')
    print(words_dict)


def card_flip():
    front_can.itemconfig(flash_text, text=word_text["English"])
    front_can.itemconfig(flash_title, text="English")
    front_can.itemconfig(front_card, image=back_img)


def button_pressed():
    global word_text
    front_can.itemconfig(front_card, image=front_img)
    front_can.itemconfig(flash_title, text="French")
    word_text = choice(words_dict)
    ran_word = word_text["French"]
    front_can.itemconfig(flash_text, text=ran_word)
    return ran_word


def right_press():
    words_dict.remove(word_text)
    window.after(3000, func=card_flip)
    button_pressed()


def wrong_press():
    words_dict.remove(word_text)
    words_to_learn_fr.append(word_text["French"])
    words_to_learn_en.append(word_text["English"])
    window.after(3000, func=card_flip)
    button_pressed()


window = Tk()
window.title("Flash Cards")
window.config(padx=30, pady=40, highlightthickness=0, bg=BACKGROUND_COLOR)

front_can = Canvas(width=850, height=538, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
front_card = front_can.create_image(425, 276, image=front_img)
front_can.grid(row=0, column=0, columnspan=2)
flash_title = front_can.create_text(425, 120, text="French", font=("Ariel", 30, "italic"))
flash_text = front_can.create_text(425, 330, text="", font=("Ariel", 50, "bold"))

button_pressed()
window.after(3000, func=card_flip)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, command=right_press)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, command=wrong_press)
wrong_button.grid(row=1, column=0)

window.mainloop()

dataf = DataFrame(
    {
        "French": words_to_learn_fr,
        "English": words_to_learn_en
    }
)

dataf.to_csv("Words_to_learn.csv", index=False)
