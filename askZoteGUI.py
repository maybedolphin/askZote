from tkinter import *
from PIL import ImageTk, Image
from assets.askZote import zoteAnswer, randomPrecept

root = Tk()
root.title("Ask Zote")
root.iconbitmap("assets/SquareZote.ico")
root.geometry('800x300')
zoteImage = ImageTk.PhotoImage(Image.open("assets/Zote_Idle.png"))

question = Entry(root, width=90)

zoteSpeech = Label(root, text="I am Zote the Mighty.\nAsk away, cur!", wraplength=500)

def ask():
    answer = zoteAnswer(question.get())
    zoteSpeech.config(text=answer)

def surprise():
    surprise = randomPrecept()
    zoteSpeech.config(text=surprise)

askButton = Button(root, text="Ask", command=ask, padx=30)
surpriseButton = Button(root, text="Surprise Me", command=surprise)
padding = Label(root, text="")
exitButton = Button(root, text="Goodbye", command = root.quit)

Label(root, image=zoteImage).grid(row=0, column=0)
zoteSpeech.grid(row=0, column=1)
question.grid(row=2, column=1)
askButton.grid(row=2, column=2)
padding.grid(row=3)
surpriseButton.grid(row=4, column=1)
padding.grid(row=9)
exitButton.grid(row=10, column=1)
root.mainloop()
