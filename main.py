from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_english = ""
english_list = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv")
    english_list = data.English.to_list()
else:
    english_list = data.English.to_list()

def check_answer():
    if not random_english:
        return
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(kanji_text, text="English", fill="white", font=("Arial", 30, "italic"))
    canvas.itemconfig(japanese_text, text=random_english, fill="white", font=("Arial", 70, "bold"))


def next_word():
    global random_english, flip_card, data
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/japanese_words.csv")
    english_list[:] = data.English.to_list()
    window.after_cancel(flip_card)
    random_english = random.choice(english_list)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(kanji_text, text=data[data.English == random_english].Kanji.item(), fill="black", font=("",70))
    canvas.itemconfig(japanese_text, text=data[data.English == random_english].Japanese.item(), fill="black", font=("",50))
    flip_card = window.after(3000, func=check_answer)

def is_known():
    global data, english_list, random_english
    if not random_english:
        return  # nothing to remove yet
    if random_english in english_list:
        english_list.remove(random_english)
        words_to_learn = data[data.English.isin(english_list)]
        words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()

window = Tk()
window.title("Japanese Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_card = window.after(3000, func=next_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
kanji_text = canvas.create_text(400,150, text="Study Japanese!", font=("",70))
japanese_text = canvas.create_text(400,300, text="Ready?", font=("",50))
canvas.grid(column=0,row=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_word)
wrong_button.grid(column=0,row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

window.mainloop()