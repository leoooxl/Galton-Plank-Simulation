import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import numpy as np

def simu_test():
    a=input("Combien de cases/tubes voulez vous ?")
    A=Arbre(8)
    return A.laisser_tomber_n_billes(1)


class Arbre:
    def __init__(self,niveau):
        self.niveau=niveau
        self.arbre=self.creer_arbre(niveau)

    def creer_arbre(self,niveau):
        """Construit un arbre binaire de profondeur donnée avec des feuilles
        initialisées à 0."""
        if niveau==0:
            return [0,[],[]]
        return [None,Arbre(niveau-1),Arbre(niveau-1)]

    def est_vide(self):
        """Vérifie si un arbres est vide."""
        return self.niveau==0

    def est_feuille(self,arbre):
        """Vérifie si un nœud est une feuille."""
        return arbre==[]

    def inserer_bille(self,niveaux,position,distribution={}):
        """Fait tomber une bille dans l'arbre jusqu'à une feuille en respectant
         la loi binomiale. Cette fonction est dépendante de la fonction
         laisser_tomber_n_bille(self,nb_billes)"""
        if self.niveau==0:
            distribution[position]+=1
            return
        if random.random() < 0.5:
            self.arbre[1].inserer_bille( niveaux-1, position, distribution)
        else:
            self.arbre[2].inserer_bille( niveaux-1, position+1, distribution)

    def laisser_tomber_n_billes(self,nb_billes):
        """Simule la chute d'un nombre de billes dans l'arbre en les
        répartissant correctement. Cette fonction est dépendante de la fonction
        inserer_bille(self,niveaux,position,distribution={})"""

        distribution={}
        for i in range(0,self.niveau+1):
            distribution[i]=0
        for _ in range(nb_billes):
            self.inserer_bille(self.niveau,0,distribution)

        return distribution,repartition(distribution)

def afficher_graphe_tkinter(graphe_pur):
    """ Fonction prenant en paramètre un "graphe pur" (graphe créé par mathplot lib)
    qui va etre converti en un fichier utilisable par tkinter puis afficher dans
    une fenetre de Tkinter
    """
    fenetre = tk.Tk()
    fenetre.title("Graphe de la Planche de Galton")
    image = Image.open(graphe_pur)
    Convert = ImageTk.PhotoImage(image)
    label = Label(fenetre, image=Convert)
    label.image = Convert
    label.pack()
    fenetre.mainloop()


def repartition(distribution):
    """ Fonction qui prend en paramètre la répartition des billes dans un arbre
    sous la forme d'un dictionnaire et qui renvoie une représentation graphique
    de cette répartition
    """
    x=list(distribution.keys())
    y=list(distribution.values())

    n = max(x)
    nb_billes = sum(y)
    mu = n/2
    sigma = np.sqrt(n)/2

    x_gauss = np.linspace(min(x),max(x),100)
    y_gauss = (nb_billes/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x_gauss - mu) ** 2) / (2 * sigma ** 2))


    plt.bar(x, y, color='blue', alpha=0.6, label='Répartition des billes')
    plt.plot(x_gauss, y_gauss, color='red', linewidth=2, label='Courbe de Gauss')
    plt.xlabel('colonnes')
    plt.ylabel('Nombres de billes')
    plt.title('Simulation de la planche de galton')
    plt.legend()
    plt.savefig(r"C:\Users\lherm\Desktop\Galton_affichage.png")
    plt.close()
    img = afficher_graphe_tkinter(r"C:\Users\lherm\Desktop\Galton_affichage.png")

    return img

def simu_test():
    A=Arbre(8)
    return A.laisser_tomber_n_billes(1000)





