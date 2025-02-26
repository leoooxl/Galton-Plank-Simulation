# Simulation de la planche de Galton
## Fonctionnement global 
La simulation de la planche de Galton est divisé en plusieurs parties expliqué plus en détail ci dessous, mais grossièrement la fonction va générer une fenetre tkinter, et a partir d'un nombre de bille et de colonne donné, va générer un arbre avec une hauteur équivalent aux nombre de colonne rentrés puis va lancer une simulation calulant la position d'une bille dans l'arbre comme si elle descendait dedans puis nous renvoyer sa position, qui nous donnera la colonne dans laquelle elle est tombé. Répéter cette simulation puis afficher via un histogramme la répatition des billes grace a mathplotlib, puis mettre l'histogramme obtenu dans la fenetre Tkinter.

### Gestion d'un arbre
Une premiere partie permettant de créer une classe Arbre et générant un Arbre de profondeur donné et disposant de méthode basique ainsi que certaines permettant de simuler une chute de bille sur une planche de Galton.

### Gestion de l'affichage
La deuxième et grande partie permet de générer tout la fenètre tkinter, les paramètres, les titres, les champs de saisis. L'affichaque de la réparition des billes et de la courbe de Gauss est géré dans une sous partie dédié grâce a mathplotlib puis transféré dans notre fenetre Tkinter.
## Utilisation de l'IA 
L'IA nous a servis afin du calcul de la courbe de Gauss et pour régler certains problèmes d'affichage dans Tkinter mais son impact n'a été que secondaire.
 
  
