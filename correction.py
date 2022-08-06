from tkinter import *
from textblob import TextBlob
import textblob

if __name__ == '__main__':
    root = Tk()
    canvas1 = Canvas(root, width = 400, height = 300)
    canvas1.pack()
    root.title('Corrector')
    input = Entry()
    canvas1.create_window(200, 140, window=input)
    label1 = Label(root,text='')
    canvas1.create_window(200, 230, window=label1)
    def getcorrect ():  
        x1 = input.get()
        tb = TextBlob(x1)
        correctword = str(tb.correct())
        label1['text'] = correctword
        print(correctword)
    button1 = Button(text='Get the correct spelling', command=getcorrect)
    canvas1.create_window(200, 180, window=button1)
    root.configure(background="white")
    root.geometry('400x300')
    root.mainloop()
