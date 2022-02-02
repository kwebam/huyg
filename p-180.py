from tkinter import *
from tkinter import ttk

root = Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("1010x375")
root.config(bg = '#F2CCC3')

Heading = Label(root, text = "LANGUAGE TRANSLATOR", bg = '#F2CCC3', font = ("Cooper Black",18, "bold", "italic"))
Heading.place(relx = 0.5, rely = 0.05, anchor = N)

input_label = Label(root, text = "Enter Text in the box below", bg = '#F2CCC3')
input_label.place(relx = 0.02, rely = 0.27, anchor = W)

input_text = Text(root, bg = '#ffffff', height = 5, wrap = "word", width = 20, bd = 0)
input_text.place(relx = 0.02, rely = 0.45, anchor = W)

root.mainloop()