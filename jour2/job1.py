class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    # getter
    def get__longueur(self):
        return self.__longueur
    # setter
    def set__longeur(self,longueur):
        self.__longueur = longueur
    # getter de largeur
    def get__largeur(self):
        return self.__largeur
    # setter de largeur
    def set__largeur(self,largeur):
        self.__largeur = largeur
    # Créaction du rectangle
rect = Rectangle(10,5)
# Afficher les valeurs initiales
print("longeur:",rect.get__longueur())
print("largeur:",rect.get__largeur())
    

    
    
