# la classe
class Vecteur2d :
  def __init__(self,x ,y):
     self.x = x
     self.y = y
  def add(self, vect1, vect2):
    vect1 = Vecteur2d(self.x, self.y)
    vect2 = Vecteur2d(self.x, self.y)
  def show (self):
      print ("\nl'addition de c'est deux vecteurs du plan est : (%d, %d)" %(vect1.x + vect2.x, vect1.y + vect2.y))
vect1 = Vecteur2d(18,56)
vect2 = Vecteur2d(6,21)
vect = Vecteur2d(0,0)
vect.show()