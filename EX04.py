# classes
class Point: # classe des points du plan.
        def __init__(self, x=0.0, y=0.0): # Initialisation avec des valeurs par defaut
                self.P_x = float(x)
                self.P_y = float(y)

class Segment: # classe composite utilisant la classe Point.
        def __init__(self, x1, y1, x2, y2): # L'initialisation utilise deux objets Point
                self.orgn = Point(x1, y1)
                self.extm = Point(x2, y2)
        def __str__(self): # Representation d'un objet segment.
                return ("Segment : [({0}, {1}), ({2}, {3})]"
                .format(self.orgn.P_x, self.orgn.P_y, self.extm.P_x, self.extm.P_y))

Val = Segment(1, 2, 3, 4)
print(Val)