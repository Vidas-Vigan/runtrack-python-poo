class Personne():
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        return f"je suis{self.nom}{self.prenom}"
personne1 = Personne("Jhon", "Doe")
personne2 = Personne("Jean", "Dupont")
personne3 = Personne("jean", "Dores")
personne4 = Personne("Jhon", "Jarvis")
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
print(personne4.SePresenter())
