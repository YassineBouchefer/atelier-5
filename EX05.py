# Class
class étudiant:
    def __init__(self, nom, cne, age, prénom, moyenne):
        self.nom = nom
        self.prénom = prénom
        self.age= age
        self.cne = cne
        self.moyenne = moyenne
    def __repr__(self):
        return '({}, {}, {}, {}, {})'.format(self.nom, self.prénom, self.age, self.cne, self.moyenne)

étudiant1= étudiant("bouchefer", "yassine", 22, "P130390392", 18)
étudiant2= étudiant("hiti gueli", "ahmed", 21, "P130493875", 15)
étudiant3= étudiant("el rhali", "mohamed" , 23, "P130354934", 17)
# Liste
étudiants = [étudiant1, étudiant2, étudiant3]

def sortétudiants_age(etu):
    return etu.age
def sortétudiants_moyenne(etu):
    return etu.moyenne

# Ordonner selon l'age
sorted_étudiants_age = sorted(étudiants, key= sortétudiants_age)

# Ordonner selon la moyenne
sorted_étudiants_moyenne = sorted(étudiants, key= sortétudiants_moyenne)

# Affichage
print(étudiants)
print("Objects sorted by age:", sorted_étudiants_age)
print("Objects sorted by moyenne:", sorted_étudiants_moyenne)