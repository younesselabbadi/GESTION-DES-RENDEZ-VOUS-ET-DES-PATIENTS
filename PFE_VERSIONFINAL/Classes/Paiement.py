#Classe Paiement 

from Facture import Facture

class Paiement():

    def __init__(self,typeP,montant,facture:Facture):
        self.type = typeP 
        self.montant = montant
        self.facture = facture
    
    def getType(self):
        return self.type

    def setType(self,typeP): 
        self.type = typeP

    def getMontant(self): 
        return self.montant

    def setMontant(self,montant):
        self.montant = montant    

    def getFacture(self): 
        return self.facture

    def setFacture(self,facture):
        self.facture = facture   

    def afficher(self):
        return " Montant : {} \n type de paiement : {}".format(self.montant,self.type)         



