#Classe Facture

from Rapport import Rapport 
from Paiement import Paiement


class Facture():

    def __init__(self,prixrestants,prixpayee,rapport:Rapport):
        self.prixrestants = prixrestants
        self.prixpayee = prixpayee
        self.rapport = rapport 
        self.paiement = None


    def getPrixRestansts(self):
        return self.prixrestants

    def setPrixRestants(self,prixr):
        self.prixrestants = prixr

    def getPrixPayee(self):
        return self.prixpayee

    def setPrixPayee(self,prixp):
        self.prixpayee = prixp
    
    def getRapport(self):
        return self.rapport

    def setRapport(self,rapport):
        self.rapport = rapport
    
    def getPaiement(self):
        return self.paiement

    def setPaiement(self,paiement):
        self.paiement = paiement

    def afficher(self):
        return "Prix Restansts : {} \n Prix Payee : {} ".format(self.prixrestants,self.prixpayee)    