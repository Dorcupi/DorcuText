from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import scrolledtext

openedFile = False

openedFileLocation = ""

defaultViewSize = 15

root = Tk("DorcuText")

root.title('DorcuText - New file')

root.iconbitmap("dorcutext.ico")

def newFile():
    global openedFile
    global openedFileLocation
    t = text
    t.delete("1.0", "end")
    openedFile = False
    openedFileLocation = ""
    root.title('DorcuText - New file')
def openfile():
    global openedFile
    global openedFileLocation
    t = text
    openlocation = filedialog.askopenfilename()
    if openlocation:
        file = open(openlocation, "r")
        openText = file.read()
        t.delete("1.0", "end")
        t.insert(END, openText)
        file.close()
        openedFile = True
        openedFileLocation = openlocation
        root.title(f'DorcuText - {openlocation}')

def saveFile():
    global openedFile
    global openedFileLocation
    t = text.get("1.0", "end-1c")
    if openedFile == True:
        file1 = open(openedFileLocation, "w+")
        file1.write(t)
        file1.close()
        openedFile = True
        openedFileLocation = openedFileLocation
    else:
        saveas()

def saveas():
    global openedFile
    global openedFileLocation
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt")
    if savelocation:
        file1 = open(savelocation, "w+")
        file1.write(t)
        file1.close()
        openedFile = True
        openedFileLocation = savelocation
        root.title(f'DorcuText - {savelocation}')

def changeviewsize():
    global text
    newsize = simpledialog.askinteger("DorcuText", "Enter new font size")
    if newsize:
        text.config(font=("Courier", newsize))

def popup_window(root = root):
    window = Toplevel()

    window.title("DorcuText - About")

    window.iconbitmap("dorcutext.ico")

    titleLabel = Label(window, text="DorcuText", font=("Courier", 25))

    titleLabel.pack(fill='x', padx=50, pady=5)

    descripLabel = Label(window, text="Lighter than Notepad", font=("Courier", 10))

    descripLabel.pack(fill='x', padx=50, pady=5)

    byLabel = Label(window, text="By: Divine Ejiogu (Dorcupi)", font=("Courier", 10))

    byLabel.pack(fill='x', padx=50, pady=5)

    copyLabel = Label(window, text="DorcuText © 2023 by Divine Ejiogu (Dorcupi) is licensed under CC BY 4.0.", font=("Courier", 10))

    copyLabel.pack(fill='x', padx=50, pady=5)

    copyLabel2 = Label(window, text="To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/", font=("Courier", 10))

    copyLabel2.pack(fill='x', padx=50, pady=5)

    button_close = Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x', padx=50, pady=5)

menubar = Menu(root)

root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

file_menu.add_command(
    label='New File',
    command=newFile,
)

file_menu.add_command(
    label='Save',
    command=saveFile,
)

file_menu.add_command(
    label='Save As',
    command=saveas,
)

file_menu.add_command(
    label='Open',
    command=openfile,
)

file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=root.destroy,
)

view_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(
    label="View",
    menu=view_menu,
    underline=0
)

view_menu.add_command(
    label='Adjust Zoom',
    command=changeviewsize,
)

about_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(
    label="DorcuText",
    menu=about_menu,
    underline=0
)

about_menu.add_command(
    label='About',
    command=popup_window,
)

global text

text = scrolledtext.ScrolledText(root)

def make_dynamic(widget):
    col_count, row_count = widget.grid_size()

    for i in range(row_count):
        widget.grid_rowconfigure(i, weight=1)

    for i in range(col_count):
        widget.grid_columnconfigure(i, weight=1)

text.grid(padx = 5, pady = 5)

text.grid_configure(sticky="nsew")

text.config(font=("Courier", 15))

make_dynamic(root)

root.mainloop()
