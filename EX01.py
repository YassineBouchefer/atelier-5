# classe
class Vecteur2D: # Les Vecteurs plans
        def __init__(self, X=0, Y=0): # Constructeur avec parametres par defaut
                # initialisation de x et y, attributs d'instance
                self.x =X
                self.y = Y
                self.nom = "yassine"
        def affiche(self):
                print (self.nom)
        def __str__(self):
                return "x = %d, y = %d" % (self.x,self.y)

# Affichage
print(" une instance sans parametres ")
print (Vecteur2D())

print(" une instance initialisee ")
print (Vecteur2D(-5.2, 4.1))
Vecteur2D().affiche()