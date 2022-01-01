# classe des rectangles
class Rectangle:
        def __init__(self, longueur=5, largeur=2): # Initialisation avec valeurs par défaut
                self.Lo = longueur
                self.La = largeur
                self.nom = "rectangle"

        def surface(self): # Retourne la surface d'un rectangle.
                return self.Lo*self.La

        def __str__(self): # Affichage des caractéristiques d'un rectangle.
                return ("\nLe {0} de côtés {1} et {2} a une surface de {3}"
                .format(self.nom, self.Lo, self.La, self.surface()))

class Carré(Rectangle): # classe des carrés (hérite de Rectangle).

        def __init__(self, coté=4): # Constructeur par défaut
                Rectangle.__init__(self, coté, coté)
                self.nom = "carré"

# Affichage
r = Rectangle(8, 5)
print(r)
c = Carré(7)
print(c)