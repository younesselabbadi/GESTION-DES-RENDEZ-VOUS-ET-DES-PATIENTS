#Classe Rapport 

from Consultation import Consultation 
from Soin import Soin 
from Facture import Facture 
from Devis import Devis

class Rapport():

    def __init__(self,numeroR,lien,consultation:Consultation,facture:Facture,soin:Soin):
        self.numerorapport = numeroR
        self.lien = lien 
        self.soin = soin 
        self.consultation = consultation 
        self.devis = None 
        self.facture = facture

    def getNumeroR(self):
        return self.numeroR
    
    def setNumeroR(self,numero):
        self.numeroR  = numero 
    
    def getLien(self):
        return self.lien
    
    def setLien(self,lien):
        self.lien  = lien      
    
    def getConsultation(self):
        return self.consultation

    def setConsultation(self,consultation:Consultation):
        self.consultation  = Consultation    

    def getSoin(self):
        return self.soin

    def setSoin(self,soin:Soin):
        self.soin  = soin  

    def getFacture(self):
        return self.facture

    def setFacture(self,facture:Facture):
        self.facture  = facture  

    def getDevis(self):
        return self.devis

    def setDevis(self,devis:Devis):
        self.devis = devis   
       
   

