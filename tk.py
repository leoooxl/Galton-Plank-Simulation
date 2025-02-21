import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import numpy as np
from tkinter import Tk, Button, Label, Frame, ttk, Entry, StringVar, messagebox

class MyWindow(Tk):

    def __init__(self):
        # On appelle le constructeur parent
        super().__init__()
        
        self.nb_billes = StringVar()
        self.nb_colonnes = StringVar()
        
        left_frame = Frame(self, bg='#FFFFFF', width = 200)
        left_frame.pack(side='left', fill='y')
        left_frame.pack_propagate(False)

        
        label = Label(self, text='Simulation de la planche de Galton',fg='black', bg='#0caded',justify='center')
        label.pack(side='top', fill='x')
    
        billes = Label(left_frame,text='Entrez le nombre de billes :')
        billes.pack(side = 'top', fill = 'x')
        
        self.nb_billes_entry = Entry(left_frame, textvariable = self.nb_billes)
        self.nb_billes_entry.focus_set()
        self.nb_billes_entry.pack(side='top')
        
        colonnes = Label(left_frame,text='Entrez le nombre de colonnes :')
        colonnes.pack(fill='x')
        
        self.nb_colonnes_entry = Entry(left_frame, textvariable = self.nb_colonnes)
        self.nb_colonnes_entry.pack(side='top')
        
        button = Button(left_frame, text='Valider',bg = '#0caded', command=self.do_something)
        button.pack(fill='x')
        
        self.billes_label = Label(left_frame, text="Nombre de billes : 0", fg="black")  # Label pour afficher le résultat
        self.billes_label.pack(fill='x')
        self.colonnes_label = Label(left_frame,text='Nombre de colonnes:0',fg='black')
        self.colonnes_label.pack(fill='x')
        
        self.geometry('900x600')
        self.title('Simulation planche de Galton')

    # gestionnaire d'événement
    def do_something(self):
        try :
            print(self.nb_billes.get())
            print(self.nb_colonnes.get())
            nb_billes = int(self.nb_billes.get().strip())
            nb_colonnes = int(self.nb_colonnes.get().strip())
            print(nb_billes)
            print(nb_colonnes)
            if nb_billes <= 0 :
                messagebox.showerror("Erreur", "Le nombre de billes doit être un entier positif.")
                return 
            if nb_colonnes <= 0:
                messagebox.showerror("Erreur", "Le nombre de colonnes doit être un entier positif.")
                return
            print('Nombre de billes :',nb_billes)
            self.billes_label.config(text=f"Nombre de billes : {nb_billes}")
            self.colonnes_label.config(text=f'Nombre de colonnes : {nb_colonnes}')
            self.nb_billes.set('')
            self.nb_colonnes.set('')
            self.nb_billes_entry.focus_set()
        except ValueError:
                    # Gestion des erreurs avec une boîte de message
                    messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide dans chaque champs avant de valider.")



# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()



## TO DO :
# * penser aux try except, ...
