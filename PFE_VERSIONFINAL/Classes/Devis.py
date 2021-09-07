#Class Devis 

from Rapport import Rapport

class Devis():

    def __init__(self,montanttotale,rapport:Rapport):
        self.montanttotale = montanttotale
        self.rapport = Rapport

    def getMontantTotale(self):
        return self.montanttotale 

    def setMontantTotale(self,montant):
        self.montanttotale = montant

    def getRapport(self):
        return self.rapport

    def setRapport(self,rapport:Rapport):
        self.rapport = rapport  

             
 