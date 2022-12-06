# Create a Window with Tkinter
from asyncio import subprocess
from tkinter import *
import os
import subprocess
import tkinter
import BruteForce
import Branch_and_Bound
import DataGenerator
import RandomizedApproach
import Dynamic
import AntColony
import Dynamic_top_down
import Fully_polynomial_time

#creat a boolean for all the algorithms
bruteAct = False
branchAct = False
DynamicAct = False
DynamicTDAct = False
AntcolonyAct = False
RandomizedAct = False
greedy1Act = False
greedy2Act = False
greedy3Act = False
fullpolyAct = False




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
    "dynamicTopDown": "",
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
    "dynamicTopDown": "",
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
    "dynamicTopDown": "",
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
    "dynamicTopDown": "",
}
def callBruteForce(problemType,fnright,frame_left,canvas):
    global bruteAct
    nbrItems = 0
    # retrieve the file name
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["brute"], maxValueSimple["brute"],nbrItems = BruteForce.main(
            "simple", path)
        file = open("Results/low-dimensional/Bruteforce", "a")
        file.write(str(timeSimple["brute"]) +" "+str(nbrItems)+"\n")
        file.close()
        bruteAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["brute"], maxValueMultiDim["brute"] = BruteForce.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callgreedyv(problemType,fnright,frame_left,canvas):

    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-v",
                   path])

def callgreedyw(problemType,fnright,frame_left,canvas):
    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-w", path])

def callgreedyr(problemType,fnright,frame_left,canvas):
    # retrieve the file name
    path = "Data/low-dimensional/"+fnright.get()
    print("path=", path)
    subprocess.run(["python", "Greedy.py", "-r", path])

def callDynamic(problemType,fnright,frame_left,canvas):
    global DynamicAct
    nbrItems = 0
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["dynamic"], maxValueSimple["dynamic"],nbrItems = Dynamic.main(
            "simple", path)
        file = open("Results/low-dimensional/Dynamic", "a")
        file.write(str(timeSimple["dynamic"]) +" "+str(nbrItems)+"\n")
        file.close()
        DynamicAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeSimple["dynamic"], maxValueSimple["dynamic"] = Dynamic.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callBranchAndBound(problemType,fnright,frame_left,canvas):
    global branchAct
    nbrItems = 0
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["branch"], maxValueSimple["branch"],nbrItems = Branch_and_Bound.main(
            "simple", path)
        file = open("Results/low-dimensional/Branch_and_Bound", "a")
        file.write(str(timeSimple["branch"]) +" "+str(nbrItems)+"\n")
        file.close()
        branchAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeSimple["branch"], maxValueSimple["branch"] = Branch_and_Bound.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callFPTAS(problemType,fnright,frame_left,canvas):
    global fullpolyAct
    nbrItems = 0
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["fullpoly"], maxValueSimple["fullpoly"],nbrItems = Fully_polynomial_time.main(
            "simple", path)
        file = open("Results/low-dimensional/Branch_and_Bound", "a")
        file.write(str(timeSimple["fullpoly"]) +" "+str(nbrItems)+"\n")
        file.close()
        fullpolyAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeSimple["fullpoly"], maxValueSimple["fullpoly"] = Fully_polynomial_time.main(
            "multi", path)
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callRandom(problemType,fnright,frame_left,canvas):
    global RandomizedAct
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["random"], maxValueSimple["random"],nbrItems = RandomizedApproach.main(
            "simple", path)
        file = open("Results/low-dimensional/RandomizedApproach", "a")
        file.write(str(timeSimple["random"]) +" "+str(nbrItems)+"\n")
        file.close()
        RandomizedAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["random"], maxValueMultiDim["random"] = RandomizedApproach.main(
            "multiDim", path)
        print("time=", timeMultiDim["random"],
              "maxValue=", maxValueMultiDim["random"])
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callDynamicTopDown(problemType,fnright,frame_left,canvas):
    global DynamicTopDownAct
    nbrItems = 0
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["dynamicTopDown"], maxValueSimple["dynamicTopDown"],nbrItems = Dynamic_top_down.main(
            "simple", path)
        file = open("Results/low-dimensional/DynamicTopDown", "a")
        file.write(str(timeSimple["dynamicTopDown"]) +" "+str(nbrItems)+"\n")
        file.close()
        DynamicTopDownAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["dynamicTopDown"], maxValueMultiDim["dynamicTopDown"] = Dynamic_top_down.main("multiDim", path)
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def callAnt(problemType,fnright,frame_left,canvas):
    global AntColonyAct
    if problemType.get() == "simple":
        path = "Data/low-dimensional/"+fnright.get()
        timeSimple["ant"], maxValueSimple["ant"],nbrItems = AntColony.main(
            "simple", path)
        file = open("Results/low-dimensional/AntColony", "a")
        file.write(str(timeSimple["ant"]) +" "+str(nbrItems)+"\n")
        file.close()
        AntColonyAct = True
    elif problemType.get() == "multiDim":
        path = "Data/multi-dimentional/"+fnright.get()
        timeMultiDim["ant"], maxValueMultiDim["ant"] = AntColony.main(
            "multiDim", path)
        print("time=", timeMultiDim["ant"], "maxValue=", maxValueMultiDim["ant"])
    # Refreh the values printed in the window (time and max value)
    init_grid(canvas)
    reloadValues(frame_left,problemType)

def createFile_interface(problemType,items,capacity,filename,fnrightMenu,fnright):
    if items.get() != "" and capacity.get() != "":
        if problemType.get() == "simple":
            path = "Data/low-dimensional/"
        elif problemType.get() == "multiDim":
            path = "Data/multi-dimentional/"
        elif problemType.get() == "multiBag":
            path = "Data/multi-bag/"
        DataGenerator.mainGraphique(
            path, filename.get(), int(items.get()), int(capacity.get()))
        changeFiles(problemType,fnrightMenu,fnright)

    else:
        print("Please enter the number of items and the capacity")

def changeColor(problemType,buttonSimple,buttonMultiDim,buttonMultiBag,frame_left):
    if problemType.get() == "simple":
        buttonSimple.config(bg="green")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="red")
        reloadValues(frame_left,problemType)
    elif problemType.get() == "multiDim":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="green")
        buttonMultiBag.config(bg="red")
        reloadValues(frame_left,problemType)
    elif problemType.get() == "multiBag":
        buttonSimple.config(bg="red")
        buttonMultiDim.config(bg="red")
        buttonMultiBag.config(bg="green")
        reloadValues(frame_left,problemType)

def changeFiles(problemType,fnrightMenu,fnright):
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

def draw_samples(canvas,filename,color):
    time = []
    nitems= []
    file = open(filename, "r")
    # ignore if the file is empty
    if file.readline() != "":
        lines = file.readlines()
        file.close()
        #sort the lines by the number of items
        lines.sort(key=lambda x: int(x.split()[1]))
        for line in lines:
            time.append(float(line.split()[0]))
            nitems.append(int(line.split()[1]))

        #draw the graph representing the time of execution of the bruteforce algorithm in function of the number of items come from the file "Results/Bruteforce"

        for i in range(len(time)):
                if time[i] < time[i-1] and i != len(time):
                    if i != 0:
                        canvas.create_line(( 450/25)*nitems[i], 600 - (time[i]*13.3),( 450/25)*nitems[i], 600 - (time[i-1]*13.3), width=3, fill=color)
                    canvas.create_oval(( 450/25)*nitems[i], 595,( 450/25)*nitems[i]+10, 605, fill=color)
                    canvas.create_text(( 450/25)*nitems[i]+10, 600, text=str(nitems[i]), anchor=SW)
                elif i != len(time)+1:
                    if i != 0:
                        canvas.create_line(( 450/25)*nitems[i-1], 600 - (time[i-1]*13.3),( 450/25)*nitems[i], 600 - (time[i]*13.3), width=3, fill=color)
                    canvas.create_oval(( 450/25)*nitems[i], 595 - (time[i]*13.3),( 450/25)*nitems[i]+10, 605 - (time[i]*13.3), fill=color)
                    canvas.create_text(10 + (nitems[i]*18), 595 - (time[i]*13.3), text=str(nitems[i]), anchor=SW)

def draw_grid(canvas, width, height):

    global bruteAct
    global branchAct
    global DynamicAct
    global AntcolonyAct
    global RandomizedAct
    global greedy1Act
    global greedy2Act
    global greedy3Act

    for i in range(0, width, 50):
        canvas.create_line([(i, 0), (i, height-50)])
    # Creates all horizontal lines at intevals of 100
    for i in range(0, height, 50):
        canvas.create_line([(0, i), (width-50, i)])
    
    canvas.create_text(455,5, text="45s", anchor=NW)
    canvas.create_text(450, 615, text="25", anchor=SE)
    canvas.create_text(5,620, text="0", anchor=SW)
    canvas.create_text(469, 590, text="0s", anchor=NE)
    canvas.create_text(470, 589, text="Time", anchor=W)
    canvas.create_text(400, 635, text="Number of items", anchor=S)

    #draw samples for all the algorithms with all time a different color
    if bruteAct == True:
        draw_samples(canvas,"Results/low-dimensional/Bruteforce","red")
    if branchAct == True:
        draw_samples(canvas,"Results/low-dimensional/Branch_and_Bound","blue")
    if DynamicAct == True:
        draw_samples(canvas,"Results/low-dimensional/Dynamic","green")
    if AntcolonyAct == True:
        draw_samples(canvas,"Results/low-dimensional/AntColony","yellow")
    if RandomizedAct == True:
        draw_samples(canvas,"Results/low-dimensional/RandomizedApproach","orange")
    if greedy1Act == True:
        draw_samples(canvas,"Results/low-dimensional/Greedy1","pink")
    if greedy2Act == True:
        draw_samples(canvas,"Results/low-dimensional/Greedy2","purple")
    if greedy3Act == True:
        draw_samples(canvas,"Results/low-dimensional/Greedy3","brown")

def reset(canvas):
    global bruteAct
    global branchAct
    global DynamicAct
    global AntcolonyAct
    global RandomizedAct
    global greedy1Act
    global greedy2Act
    global greedy3Act

    if bruteAct == True or branchAct == True or DynamicAct == True or AntcolonyAct == True or RandomizedAct == True or greedy1Act == True or greedy2Act == True or greedy3Act == True:
        canvas.delete("all")
        bruteAct = False
        branchAct = False
        DynamicAct = False
        AntcolonyAct = False
        RandomizedAct = False
        greedy1Act = False
        greedy2Act = False
        greedy3Act = False
        draw_grid(canvas, 500, 650)
    else:
        draw_grid(canvas, 500, 650)

def init_grid(canvas):
    draw_grid(canvas, 500, 650)
    

def reloadValues(frame_left,problemType):
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

def main():
    window = Tk()
    # personalise the window
    window.title("Graphic Interface")
    window.geometry("1080x720")
    window.minsize(480, 360)
    window.maxsize(1080,720)
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


    frame_left = Frame(window, bg="#528860", bd=1, relief=SUNKEN)
    frame_left.pack(side=LEFT, fill=BOTH)

    frame_right = Frame(window, bg="#8BC49A", bd=1, relief=SUNKEN)
    frame_right.pack(side=RIGHT, fill=BOTH, expand=YES)

    canvas= tkinter.Canvas(frame_right, width=800, height=800, bg="white")
    canvas.pack()


    buttonCreateFile = Button(frameEntry, text="Create file", bg="green",
                            fg="white", command=lambda:createFile_interface(problemType,items,capacity,filename,fnrightMenu,fnright))
    buttonCreateFile.pack(side=LEFT, padx=5, pady=5)

    # Create a button to refresh the right frame (frame_right) with the function init_grid
    buttonReset = Button(frameEntry, text="R", bg="green",
                            fg="white", command=lambda:reset(canvas))
    buttonReset.pack(side=LEFT, padx=20, pady=5)


    # change the color of the button when the variable problemType is updated

    # bind the function changeColor to the variable problemType
    problemType.trace("w", lambda *args: changeColor(problemType,buttonSimple,buttonMultiDim,buttonMultiBag,frame_left))

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

    # bind the function changeFiles to the variable problemType
    problemType.trace("w", lambda *args: changeFiles(problemType,fnrightMenu,fnright))


    # determine a grid of 13*7 in the left frame
    for i in range(13):
        frame_left.rowconfigure(i, weight=1)
    for i in range(7):
        frame_left.columnconfigure(i, weight=1)


    # create 11 buttons in the left frame and each for one row and all columns
    # call brute force
    button1 = Button(frame_left, text="Brute Force",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callBruteForce(problemType,fnright,frame_left,canvas))
    button1.grid(row=3, column=0, columnspan=3, sticky=NSEW)

    button2 = Button(frame_left, text="Greedy Value",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callgreedyv(problemType,fnright,frame_left,canvas))
    button2.grid(row=4, column=0, columnspan=3, sticky=NSEW)

    button3 = Button(frame_left, text="Greedy Weight",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callgreedyw(problemType,fnright,frame_left,canvas))
    button3.grid(row=5, column=0, columnspan=3, sticky=NSEW)

    button4 = Button(frame_left, text="Greedy Ratio",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callgreedyr(problemType,fnright,frame_left,canvas))
    button4.grid(row=6, column=0, columnspan=3, sticky=NSEW)

    button5 = Button(frame_left, text="Dynamic", bg="#8BC49A",
                    fg="black", bd=1, command=lambda:callDynamic(problemType,fnright,frame_left,canvas))
    button5.grid(row=7, column=0, columnspan=3, sticky=NSEW)

    button6 = Button(frame_left, text="Branch and Bound",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callBranchAndBound(problemType,fnright,frame_left,canvas))
    button6.grid(row=8, column=0, columnspan=3, sticky=NSEW)

    button7 = Button(frame_left, text="Fully polynomial time",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callFPTAS(problemType,fnright,frame_left,canvas))
    button7.grid(row=9, column=0, columnspan=3, sticky=NSEW)

    button8 = Button(frame_left, text="Randomized approach",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callRandom(problemType,fnright,frame_left,canvas))
    button8.grid(row=10, column=0, columnspan=3, sticky=NSEW)

    button9 = Button(frame_left, text="Ant colony",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callAnt(problemType,fnright,frame_left,canvas))
    button9.grid(row=11, column=0, columnspan=3, sticky=NSEW)

    button10 = Button(frame_left, text="Dynamic Top Down",
                    bg="#8BC49A", fg="black", bd=1, command=lambda:callDynamicTopDown(problemType,fnright,frame_left,canvas))
    button10.grid(row=12, column=0, columnspan=3, sticky=NSEW)


    # creation of the title
    title1 = Label(frame_left, text="Maximum Value",
                bg="#207436", fg="black", bd=1, relief=RIDGE, font=25)
    title1.grid(row=0, column=3, rowspan=2, columnspan=2, sticky=NSEW)

    title2 = Label(frame_left, text="Time of algorithme", bg="#207436",
                fg="black", bd=1, relief=RIDGE, font=25)
    title2.grid(row=0, column=5, rowspan=2, columnspan=2, sticky=NSEW)

    # Print the window
    
    init_grid(canvas)
    reloadValues(frame_left,problemType)
    window.mainloop()


main()