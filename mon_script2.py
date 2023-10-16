from pip._vendor.pyparsing.core import NoMatch
class Livre:
    def __init__(self,titre,auteur):
        self.titre = titre
        self.auteur = auteur
class Auteur:
    def __init__(self,nom):
        self.nom = nom
auteur1= Auteur("j.k. rowling")  
auteur2= Auteur("jane doe")     
livre1= Livre("harry potter and the sorcerers stone", auteur1)   
livre2= Livre("history of the world", auteur2)   
class Bibliotheque:
    def __init__(self):
        self.collection=[livre2]
    def emprunter_livre(self,livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return print(livre.titre+"a ete emprunte.")
        else:
            return print("le livre n'est pas disponible")
    def ajouter_livre(self,livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return print(livre.titre+" est deja ajouter.")
        else:
            self.collection.append(livre)
bibliotheque= Bibliotheque()

resultat2= bibliotheque.ajouter_livre(livre2)