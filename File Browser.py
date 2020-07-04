from tkinter import *
from tkinter import filedialog
import os

root = Tk()

def open_file():
    filename = filedialog.askopenfilenames(parent=root, initialdir="/", title="File Browser",
                                      filetypes=[("Text files","*.txt*"),("PDF","*.pdf*"),
                                                 ("PNG", "*.png"),("JPEG", "*.jpg"),("All files", "*")])
    print(filename)
    try:
        os.startfile(filename[0])
    except IndexError:
        print("No file selected")

root.title('File Explorer')
root.geometry("325x140")
root.config(background="black")
label_file_explorer = Label(root, text="File Explorer", width=40, height=4, fg="blue",
                            background="white", font=("Ariel",10,"bold"))
button_explore = Button(root, text="Browse Files", border=3, command=open_file)
button_exit = Button(root, text="Exit", border=3, command=exit)
label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

root.mainloop()