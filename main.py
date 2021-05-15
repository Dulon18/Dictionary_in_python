from tkinter import*
from PyDictionary import PyDictionary
dictionary = PyDictionary
root= Tk()

#for fixed window use geometry
root.geometry("600x400")

root.title("Dictionary in tkinter")

#windows background color
root["bg"] = "#b30086"

def dict():
     meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
     synonym.config(text=dictionary.synonym(word.get()))
     antonym.config(text=dictionary.antonym(word.get()))

Label(root, text="<>:<> Dictionary <>:<>", font="arial 24 bold", fg="#000").pack(pady=10)
frame=Frame(root)

#frame making
Label(frame, text="Type word: ", font="Rochester 15 bold").pack(side=LEFT)
word = Entry(frame, font="Helvetica 20 bold", bg="#99004d", bd=5)
word.pack()
frame.pack(pady=10)

#submit button make
Button(root, text="Submit", font="Helvetica 15 bold", bg="#99004d",fg="#fff", bd=4, command = dict).pack()

#Frame1
frame1= Frame(root)
Label(frame1, text="Meaning: ", font="Helvetica 15 bold").pack(side=LEFT)
meaning= Label(frame1, text=" ", font="Helvetica 10 bold")
meaning.pack(pady=10)
frame1.pack(pady=10)

#frame2
frame2= Frame(root)
Label(frame2, text="Synonym: ", font="Helvetica 15 bold").pack(side=LEFT)
synonym= Label(frame2, text=" ", font="Helvetica 10 bold")
synonym.pack(pady=10)
frame2.pack(pady=10)

#frame 3
frame3= Frame(root)
Label(frame3, text="Antonym: ", font="Helvetica 15 bold").pack(side=LEFT)
antonym= Label(frame3, text="", font="Helvetica 15 bold")
antonym.pack(pady=10)
frame3.pack(pady=10)



root.mainloop()  #execute tkinter
