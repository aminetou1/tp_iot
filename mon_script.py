from pip._vendor.pyparsing.core import NoMatch
class Livre:
    def __init__(self,titre,auteur):
        self.titre = titre
        self.auteur = auteur
class Auteur:
    def __init__(self,nom):
        self.nom = nom
auteur1= Auteur("j.k. rowling")     
livre1= Livre("harry potter and the sorcerers stone", auteur1)   
class Bibliotheque:
    def __init__(self):
        self.collection=[]
    def emprunter_livre(self,livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return print(livre.titre+"a ete emprunte.")
        else:
            return print("le livre n'est pas disponible")
bibliotheque= Bibliotheque()
resultat = bibliotheque.emprunter_livre(livre1)