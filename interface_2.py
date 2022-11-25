# Create a Window with Tkinter
from asyncio import subprocess
from tkinter import *
import os
import sys
import subprocess
import BruteForce
import Branch_and_Bound

# Variable time and MaxValue from the programes
time = [0 for x in range(8)]
maxValue = [0 for x in range(8)]


# Function that call the program brute force with the file selected in the Entry fnright
def callBruteForce():
    # retrieve the file name
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        time[0], maxValue[0] = BruteForce.main("simple", path)
        print("time=", time[0], "maxValue=", maxValue[0])
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        time[0], maxValue[0] = BruteForce.main("multi", path)
        print("time=", time[0], "maxValue=", maxValue[0])


def callgreedyv():

    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-v",
                   path])


def callgreedyw():
    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-w", path])


def callgreedyr():
    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-r", path])


def callDynamic():
    os.system("python Dynamic.py")


def callBranchAndBound():
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        time[5], maxValue[5] = Branch_and_Bound.main("simple", path)
        print("time=", time[5], "maxValue=", maxValue[5])
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        time[5], maxValue[5] = Branch_and_Bound.main("multi", path)
        print("time=", time[5], "maxValue=", maxValue[5])


# main
window = Tk()
# personalise the window
window.title("Graphic Interface")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background="#528860")

# Create a menu bar to select the type of problem to solve (simple or multi-dimensional or multi-bag)if we click on the buttons, the variable problemType will be updated
# The active button will be in green and the others in red
# The variable problemType will be used to call the right program
problemType = StringVar()
problemType.set("simple")
# Create a frame to contain the menu bar
frameMenu = Frame(window, bg="#528860")
frameMenu.pack(side=TOP, fill=X)
# Create the buttons, one for each type of problem to solve if we click on the buttons, the variable problemType will be updated and the color of the buttons will be updated
buttonSimple = Button(frameMenu, text="Simple", bg="green",
                      fg="white", command=lambda: problemType.set("simple"))
buttonSimple.pack(side=LEFT, padx=5, pady=5)
buttonMultiDim = Button(frameMenu, text="Multi-Dimensional", bg="red",
                        fg="white", command=lambda: problemType.set("multiDim"))
buttonMultiDim.pack(side=LEFT, padx=5, pady=5)
buttonMultiBag = Button(frameMenu, text="Multi-Bag", bg="red",
                        fg="white", command=lambda: problemType.set("multiBag"))
buttonMultiBag.pack(side=LEFT, padx=5, pady=5)

# change the color of the button when the variable problemType is updated


def changeColor():
    if problemType.get() == "simple":
        buttonSimple.config(bg="green")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="red")
    elif problemType.get() == "multiDim":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="green")
        buttonMultiBag.config(bg="red")
    elif problemType.get() == "multiBag":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="green")


# bind the function changeColor to the variable problemType
problemType.trace("w", lambda *args: changeColor())


# create 2 vertical frames that take boyh 50% of the window
frame_left = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
frame_left.pack(side=LEFT, fill=BOTH)

frame_right = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_right.pack(side=RIGHT, fill=BOTH, expand=YES)

# label for file name
fnleft = Label(frame_left, text="Select the file to solve :",
               bg="#207436", fg="black", font=25)
fnleft.grid(row=0, column=0, rowspan=2, columnspan=1, sticky=NSEW)

# Mettre la liste des fichiers dans un menu déroulant de taille égalent à la taille du label fnleft et collé adroite de celle-ci.
# Si la variable problemType est égale à "simple", on affiche les fichiers du dossier "Data/low-dimensional"
# Si la variable problemType est égale à "multiDim", on affiche les fichiers du dossier "Data/multi-dimensional"
# Si la variable problemType est égale à "multiBag", on affiche les fichiers du dossier "Data/multi-bag"

if problemType.get() == "simple":
    files = os.listdir("Data/low-dimensional")
elif problemType.get() == "multiDim":
    files = os.listdir("Data/multi-dimentional")
elif problemType.get() == "multiBag":
    files = os.listdir("Data/multi-bag")

# create a variable to store the file name
fnright = StringVar()
# create a menu to select the file name
fnright.set(files[0])
fnrightMenu = OptionMenu(frame_left, fnright, *files)
fnrightMenu.grid(row=0, column=1, rowspan=2, columnspan=2, sticky=NSEW)

# Change the list of files in the menu when the variable problemType is updated


def changeFiles():
    if problemType.get() == "simple":
        files = os.listdir("Data/low-dimensional")
    elif problemType.get() == "multiDim":
        files = os.listdir("Data/multi-dimentional")
    elif problemType.get() == "multiBag":
        files = os.listdir("Data/multi-bag")
    fnrightMenu["menu"].delete(0, "end")
    for file in files:
        fnrightMenu["menu"].add_command(
            label=file, command=lambda value=file: fnright.set(value))


# bind the function changeFiles to the variable problemType
problemType.trace("w", lambda *args: changeFiles())


# determine a grid of 13*7 in the left frame
for i in range(13):
    frame_left.rowconfigure(i, weight=1)
for i in range(7):
    frame_left.columnconfigure(i, weight=1)


# create 11 buttons in the left frame and each for one row and all columns
# call brute force
button1 = Button(frame_left, text="Brute Force",
                 bg="#8BC49A", fg="black", bd=1, command=callBruteForce)
button1.grid(row=3, column=0, columnspan=3, sticky=NSEW)

button2 = Button(frame_left, text="Greedy Value",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyv)
button2.grid(row=4, column=0, columnspan=3, sticky=NSEW)

button3 = Button(frame_left, text="Greedy Weight",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyw)
button3.grid(row=5, column=0, columnspan=3, sticky=NSEW)

button4 = Button(frame_left, text="Greedy Ratio",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyr)
button4.grid(row=6, column=0, columnspan=3, sticky=NSEW)

button5 = Button(frame_left, text="Dynamic", bg="#8BC49A",
                 fg="black", bd=1, command=callDynamic)
button5.grid(row=7, column=0, columnspan=3, sticky=NSEW)

button6 = Button(frame_left, text="Branch and Bound",
                 bg="#8BC49A", fg="black", bd=1, command=callBranchAndBound)
button6.grid(row=8, column=0, columnspan=3, sticky=NSEW)

button7 = Button(frame_left, text="Fully polynomial time",
                 bg="#8BC49A", fg="black", bd=1)
button7.grid(row=9, column=0, columnspan=3, sticky=NSEW)

button8 = Button(frame_left, text="Randomized approach",
                 bg="#8BC49A", fg="black", bd=1)
button8.grid(row=10, column=0, columnspan=3, sticky=NSEW)

button9 = Button(frame_left, text="Ant colony",
                 bg="#8BC49A", fg="black", bd=1)
button9.grid(row=11, column=0, columnspan=3, sticky=NSEW)

button10 = Button(frame_left, text="Personnal algorithm",
                  bg="#8BC49A", fg="black", bd=1)
button10.grid(row=12, column=0, columnspan=3, sticky=NSEW)


# determine a grid of 12*12 in the right frame
for i in range(12):
    frame_right.columnconfigure(i, weight=1)
    frame_right.rowconfigure(i, weight=1)

# creation of the title
title1 = Label(frame_left, text="Maximum Value",
               bg="#207436", fg="black", bd=1, relief=RIDGE, font=25)
title1.grid(row=0, column=3, rowspan=2, columnspan=2, sticky=NSEW)

title2 = Label(frame_left, text="Time of algorithme", bg="#207436",
               fg="black", bd=1, relief=RIDGE, font=25)
title2.grid(row=0, column=5, rowspan=2, columnspan=2, sticky=NSEW)


# Create 11 label for the row 2 to 12 and that take all column
for i in range (10):
    Label(frame_left, text="", bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
        row=i+3, column=3, columnspan=2, sticky=NSEW)

for i in range (10):
    Label(frame_left, text="", bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
        row=i+3, column=5, columnspan=2, sticky=NSEW)
# Print the window
window.mainloop()
