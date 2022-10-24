# Create a Window with Tkinter
from asyncio import subprocess
from tkinter import *
import os
import sys
import subprocess

# definition of programm's callback functions


def callbruteforce():
    os.system("python BruteForce.py")


def callgreedyv():

    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-w",
                   path])


def callgreedyw():
    subprocess.run(["python", "Greedy.py", "-w",
                   "Data/low-dimensional/f4_l-d_kp_4_11.txt"])


def callgreedyr():
    os.system("python Greedy.py -r Data/low-dimensional/f4_l-d_kp_4_11.txt")


def callDynamic():
    os.system("python Dynamic.py")


def callBranchAndBound():
    os.system("python Branch_and_Bound.py")


# main
window = Tk()
# personalise the window
window.title("Graphic Interface")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background="#528860")

# create 2 vertical frames that take boyh 50% of the window
frame_left = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
frame_left.pack(side=LEFT, fill=BOTH, expand=YES)

frame_right = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
frame_right.pack(side=RIGHT, fill=BOTH, expand=YES)

# determine a grid of 13*13 in the left frame
for i in range(13):
    frame_left.columnconfigure(i, weight=1)
    frame_left.rowconfigure(i, weight=1)

# label for file name
fnleft = Label(frame_left, text="Filename :",
               bg="#207436", fg="black", font=25)
fnleft.grid(row=0, column=0, rowspan=2, columnspan=5, sticky=NSEW)

# entry for file name
fnright = Entry(frame_left, bg="#528860", fg="white", font=25)
fnright.grid(row=0, column=5, rowspan=2, columnspan=8, sticky=NSEW)


# create 11 buttons in the left frame and each for one row and all columns
# call brute force
button1 = Button(frame_left, text="Brute Force",
                 bg="#8BC49A", fg="black", bd=1, command=callbruteforce)
button1.grid(row=2, column=0, columnspan=13, sticky=NSEW)

button2 = Button(frame_left, text="Greedy Value",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyv)
button2.grid(row=3, column=0, columnspan=13, sticky=NSEW)

button3 = Button(frame_left, text="Greedy Weight",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyw)
button3.grid(row=4, column=0, columnspan=13, sticky=NSEW)

button4 = Button(frame_left, text="Greedy Ratio",
                 bg="#8BC49A", fg="black", bd=1, command=callgreedyr)
button4.grid(row=5, column=0, columnspan=13, sticky=NSEW)

button5 = Button(frame_left, text="Dynamic", bg="#8BC49A",
                 fg="black", bd=1, command=callDynamic)
button5.grid(row=6, column=0, columnspan=13, sticky=NSEW)

button6 = Button(frame_left, text="Branch and Bound",
                 bg="#8BC49A", fg="black", bd=1, command=callBranchAndBound)
button6.grid(row=7, column=0, columnspan=13, sticky=NSEW)

button7 = Button(frame_left, text="Minimum spanning tree",
                 bg="#8BC49A", fg="black", bd=1)
button7.grid(row=8, column=0, columnspan=13, sticky=NSEW)

button8 = Button(frame_left, text="Fully polynomial time",
                 bg="#8BC49A", fg="black", bd=1)
button8.grid(row=9, column=0, columnspan=13, sticky=NSEW)

button9 = Button(frame_left, text="Randomized approach",
                 bg="#8BC49A", fg="black", bd=1)
button9.grid(row=10, column=0, columnspan=13, sticky=NSEW)

button10 = Button(frame_left, text="Ant colony",
                  bg="#8BC49A", fg="black", bd=1)
button10.grid(row=11, column=0, columnspan=13, sticky=NSEW)

button11 = Button(frame_left, text="Personnal algorithm",
                  bg="#8BC49A", fg="black", bd=1)
button11.grid(row=12, column=0, columnspan=13, sticky=NSEW)


# determine a grid of 13*13 in the right frame
for i in range(13):
    frame_right.columnconfigure(i, weight=1)
    frame_right.rowconfigure(i, weight=1)

# creation of the title
title1 = Label(frame_right, text="Maximum Value",
               bg="#207436", fg="black", bd=1, relief=RIDGE, font=25)
title1.grid(row=0, column=0, rowspan=2, columnspan=7, sticky=NSEW)

title2 = Label(frame_right, text="Time", bg="#207436",
               fg="black", bd=1, relief=RIDGE, font=25)
title2.grid(row=0, column=7, rowspan=2, columnspan=6, sticky=NSEW)


# Create 11 label for the row 2 to 12 and that take all column
label1 = Label(frame_right, text="",
               bg="#528860", fg="white", bd=1, relief=SUNKEN)
label1.grid(row=2, column=0, columnspan=7, sticky=NSEW)

label2 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label2.grid(row=3, column=0, columnspan=7, sticky=NSEW)

label3 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label3.grid(row=4, column=0, columnspan=7, sticky=NSEW)

label4 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label4.grid(row=5, column=0, columnspan=7, sticky=NSEW)

label5 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label5.grid(row=6, column=0, columnspan=7, sticky=NSEW)

label6 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label6.grid(row=7, column=0, columnspan=7, sticky=NSEW)

label7 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label7.grid(row=8, column=0, columnspan=7, sticky=NSEW)

label8 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label8.grid(row=9, column=0, columnspan=7, sticky=NSEW)

label9 = Label(frame_right, text=" ", bg="#528860",
               fg="white", bd=1, relief=SUNKEN)
label9.grid(row=10, column=0, columnspan=7, sticky=NSEW)

label10 = Label(frame_right, text=" ", bg="#528860",
                fg="white", bd=1, relief=SUNKEN)
label10.grid(row=11, column=0, columnspan=7, sticky=NSEW)

label11 = Label(frame_right, text=" ", bg="#528860",
                fg="white", bd=1, relief=SUNKEN)
label11.grid(row=12, column=0, columnspan=7, sticky=NSEW)

# Print the window
window.mainloop()
