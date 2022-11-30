# Create a Window with Tkinter
from asyncio import subprocess
from tkinter import *
import os
import sys
import subprocess
import BruteForce
import Branch_and_Bound
import DataGenerator
import RandomizedApproach
import Dynamic

# Dictionnary Variable time and MaxValue from the programes for the simple knapsack problem
timeSimple = {
    "brute": "",
    "greedyV": "",
    "greedyW": "",
    "greedyR": "",
    "dynamic": "",
    "branch": "",
    "fullpoly": "",
    "random": "",
    "ant": "",
    "personnal": ""
}
maxValueSimple = {
    "brute": "",
    "greedyV": "",
    "greedyW": "",
    "greedyR": "",
    "dynamic": "",
    "branch": "",
    "fullpoly": "",
    "random": "",
    "ant": "",
    "personnal": ""
}

# Dictionnary Variable time and MaxValue from the programes for the MultiDimensional knapsack problem
timeMultiDim = {
    "brute": "",
    "greedyV": "",
    "greedyW": "",
    "greedyR": "",
    "dynamic": "",
    "branch": "",
    "fullpoly": "",
    "random": "",
    "ant": "",
    "personnal": ""
}
maxValueMultiDim = {
    "brute": "",
    "greedyV": "",
    "greedyW": "",
    "greedyR": "",
    "dynamic": "",
    "branch": "",
    "fullpoly": "",
    "random": "",
    "ant": "",
    "personnal": ""
}


# Function that call the program brute force with the file selected in the Entry fnright
def callBruteForce():
    # retrieve the file name
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["brute"], maxValueSimple["brute"] = BruteForce.main(
            "simple", path)
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["brute"], maxValueMultiDim["brute"] = BruteForce.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    reloadValues()


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
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["dynamic"], maxValueSimple["dynamic"] = Dynamic.main(
            "simple", path)
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeSimple["dynamic"], maxValueSimple["dynamic"] = Dynamic.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    reloadValues()


def callBranchAndBound():
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["branch"], maxValueSimple["branch"] = Branch_and_Bound.main(
            "simple", path)
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeSimple["branch"], maxValueSimple["branch"] = Branch_and_Bound.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    reloadValues()


# Function for called the program RandomizedApproach that solve the KnapSack problem with a randomized approach
def callRandom():
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["random"], maxValueSimple["random"] = RandomizedApproach.main(
            "simple", path)
        print("time=", timeSimple["random"],
              "maxValue=", maxValueSimple["random"])
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["random"], maxValueMultiDim["random"] = RandomizedApproach.main(
            "multiDim", path)
        print("time=", timeMultiDim["random"],
              "maxValue=", maxValueMultiDim["random"])
    # Refreh the values printed in the window (time and max value)
    reloadValues()


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

# create 2 entry to write the number of items and the capacity of the knapsack inside the frame frameMenu
# the variable items and capacity will be used to create a file with the right number of items and the right capacity
items = StringVar()
capacity = StringVar()
filename = StringVar()
# Create a frame to contain the entry
frameEntry = Frame(window, bg="#528860")
frameEntry.pack(side=TOP, fill=X)
# Create the entry
labelItems = Label(frameEntry, text="Number of items",
                   bg="#528860", fg="white")
labelItems.pack(side=LEFT, padx=5, pady=5)
entryItems = Entry(frameEntry, textvariable=items, width=10)
entryItems.pack(side=LEFT, padx=5, pady=5)
labelCapacity = Label(frameEntry, text="Capacity", bg="#528860", fg="white")
labelCapacity.pack(side=LEFT, padx=5, pady=5)
entryCapacity = Entry(frameEntry, textvariable=capacity, width=10)
entryCapacity.pack(side=LEFT, padx=5, pady=5)
labelFilename = Label(frameEntry, text="Filename", bg="#528860", fg="white")
labelFilename.pack(side=LEFT, padx=5, pady=5)
entryFilename = Entry(frameEntry, textvariable=filename, width=10)
entryFilename.pack(side=LEFT, padx=5, pady=5)
# creat the entry of the file name
# Create a button to create a file with the right number of items and the right capacity
# The file will be created in the folder Data/low-dimensional
# The name of the file will be the number of items and the capacity
# The file will be created only if the number of items and the capacity are not empty


def createFile_interface():
    if items.get() != "" and capacity.get() != "":
        if problemType.get() == "simple":
            path = "Data/low-dimensional/"
        elif problemType.get() == "multiDim":
            path = "Data/multi-dimentional/"
        elif problemType.get() == "multiBag":
            path = "Data/multi-bag/"
        DataGenerator.mainGraphique(
            path, filename.get(), int(items.get()), int(capacity.get()))
        changeFiles()

    else:
        print("Please enter the number of items and the capacity")


buttonCreateFile = Button(frameEntry, text="Create file", bg="green",
                          fg="white", command=createFile_interface)
buttonCreateFile.pack(side=LEFT, padx=5, pady=5)


# change the color of the button when the variable problemType is updated


def changeColor():
    if problemType.get() == "simple":
        buttonSimple.config(bg="green")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="red")
        reloadValues()
    elif problemType.get() == "multiDim":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="green")
        buttonMultiBag.config(bg="red")
        reloadValues()
    elif problemType.get() == "multiBag":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="green")
        reloadValues()


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
                 bg="#8BC49A", fg="black", bd=1, command=callRandom)
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


# Create 11 label for the row 2 to 12 and that take all column, the text is the value in the dictionary of the current problem
def reloadValues():
    if (problemType.get() == "simple"):
        i = 0
        for key, value in maxValueSimple.items():
            Label(frame_left, text=value, bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
                row=i+3, column=3, columnspan=2, sticky=NSEW)
            print(value)
            i += 1
        i = 0
        for key, value in timeSimple.items():
            Label(frame_left, text=value, bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
                row=i+3, column=5, columnspan=2, sticky=NSEW)
            i += 1
    elif (problemType.get() == "multiDim"):
        i = 0
        for key, value in maxValueMultiDim.items():
            Label(frame_left, text=value, bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
                row=i+3, column=3, columnspan=2, sticky=NSEW)
            i += 1
        i = 0
        for key, value in timeMultiDim.items():
            Label(frame_left, text=value, bg="#207436", fg="black", bd=1, relief=RIDGE).grid(
                row=i+3, column=5, columnspan=2, sticky=NSEW)
            i += 1


# Print the window
reloadValues()
window.mainloop()
