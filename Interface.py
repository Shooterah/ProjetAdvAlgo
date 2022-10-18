# interface graphique avec Tkinter qui dispose de 8 boutons

from tkinter import *
import os


class Interface(Frame):

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        self.message = Label(self, text="Interface graphique")
        self.message.pack()

        self.boutonQuitter = Button(self, text="Quitter", command=self.quit)
        self.boutonQuitter.pack(side="bottom")

        self.bouton1 = Button(self, text="Brute Force", command=self.bouton1)
        self.bouton1.pack(side="left")

        self.bouton2 = Button(self, text="Greedy 1", command=self.bouton2)
        self.bouton2.pack(side="top")

        self.bouton3 = Button(self, text="3", command=self.bouton3)
        self.bouton3.pack(side="left")

        self.bouton4 = Button(self, text="4", command=self.bouton4)
        self.bouton4.pack(side="left")

        self.bouton5 = Button(self, text="5", command=self.bouton5)
        self.bouton5.pack(side="left")

        self.bouton6 = Button(self, text="6", command=self.bouton6)
        self.bouton6.pack(side="left")

        self.bouton7 = Button(self, text="7", command=self.bouton7)
        self.bouton7.pack(side="left")

        self.bouton8 = Button(self, text="8", command=self.bouton8)
        self.bouton8.pack(side="left")

    def bouton1(self):
        os.system("python /home/pi/Projet/Interface.py")

    def bouton2(self):
        os.system("python /home/pi/Projet/Interface2.py")

    def bouton3(self):
        os.system("python /home/pi/Projet/Interface3.py")

    def bouton4(self):
        os.system("python /home/pi/Projet/Interface4.py")

    def bouton5(self):
        os.system("python /home/pi/Projet/Interface5.py")

    def bouton6(self):
        os.system("python /home/pi/Projet/Interface6.py")

    def bouton7(self):
        os.system("python /home/pi/Projet/Interface7.py")

    def bouton8(self):
        os.system("python /home/pi/Projet/Interface8.py")


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Interface graphique")

# Création d'un widget Button (bouton Quitter)
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="bottom")

# Création d'un widget Button (bouton 1)
bouton1 = Button(fenetre, text="Brute Force", command=fenetre.quit)
bouton1.pack(fill=X, ipady=10)

# Création d'un widget Button (bouton 2)
bouton2 = Button(fenetre, text="Greedy 1", command=fenetre.quit)
bouton2.pack(fill=X, ipady=20)

# Création d'un widget Button (bouton 3)
bouton3 = Button(fenetre, text="3", command=fenetre.quit)
bouton3.pack(fill=X, ipady=30)

# Création d'un widget Button (bouton 4)
bouton4 = Button(fenetre, text="4", command=fenetre.quit)
bouton4.pack(fill=X, ipady=40)

# Création d'un widget Button (bouton 5)
bouton5 = Button(fenetre, text="5", command=fenetre.quit)
bouton5.pack(fill=X, ipady=50)

# Création d'un widget Button (bouton 6)
bouton6 = Button(fenetre, text="6", command=fenetre.quit)
bouton6.pack(fill=X, ipady=60)

# Création d'un widget Button (bouton 7)
bouton7 = Button(fenetre, text="7", command=fenetre.quit)
bouton7.pack(fill=X, ipady=70)

# Création d'un widget Button (bouton 8)
bouton8 = Button(fenetre, text="8", command=fenetre.quit)
bouton8.pack(fill=X, ipady=80)


# Création d'un widget Label (texte)
label = Label(fenetre, text="Interface graphique")
label.pack()

# Création d'un widget Canvas (zone graphique)
zone = Canvas(fenetre, width=768, height=576, background="white")
zone.pack()

# Création d'un widget Frame (cadre)
cadre = Frame(fenetre, borderwidth=2, relief=GROOVE)
cadre.pack(side=LEFT, padx=10, pady=10)


# Affichage du widget
fenetre.mainloop()
