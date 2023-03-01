class Livre:
    #  Créaction des classes
    def __init__(self,titre,auteur,page):
          self.__titre = titre
          self.__auteur = auteur
          self.__page = page
    # getter de titre
    def get__titre(self):
        return self.__titre
    # setter de titre
    def set__titre(self,titre):
        self.__titre = titre
    
    # getter auteur
    def get__auteur(self):
         return self.__auteur
    # setter de auteur
    def set__auteur(self,auteur):
         self.__auteur = auteur
    
    # getter page
    def get_page(self):
         return self.__page
    # setter page
    def set__page(self,page):
         self.__page = page

# Changer le nombre de page qui doit être un nombre positif
# sinon la valeur n'est pas changer et un message d'erreur est afficher
    def verification(self):
        "Créaction dictionnaire"
        dict={1,2,3,4,5,
            6,7,8,9,10}
        if dict > self.page:
            print("La valeur est changer")
        else:
             print("La valeur n'est changer")

    def __init__(self,dispo):
         self.__dispo = dispo

    # getter de titre
    def get__dispo (self):
        return self.__dispo
    
    # setter de titre
    def set__titre(self,dispo):
        self.__dispo = dispo
    
    def dispo(self):
         if self.__dispo == True:
              return True
         else:
              return False
valeur = Livre("l'armées de l'ombre","joseph kessel","300")
# Imprimer les valeurs
print(valeur.get__auteur())
print(valeur.get__titre())
print(valeur.get_page())
