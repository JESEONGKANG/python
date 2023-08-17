from tkinter import *
root = Tk()
root.geometry("200x250")

upFrame = Frame(root, bg="blue")
upFrame.pack(fill=X)
downFrame = Frame(root, background="yellow")
downFrame.pack(fill=X)

editBox = Entry(upFrame, width=10)
editBox.pack(fill=X, padx=20, pady=20)

listbox = Listbox(downFrame)
listbox.pack(fill=X, padx=10, pady=10)

listbox.insert(END, "하나")
listbox.insert(END, "둘")
listbox.insert(END, "셋")

root.mainloop()
