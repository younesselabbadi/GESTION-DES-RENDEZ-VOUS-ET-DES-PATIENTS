#Clsse Consultation  

from RDV import RDV 

class Consultation():

    def __init__(self,numero,rdv:RDV):
        self.numero = numero 
        self.RDV = None 
        self.rapport = None

    def getRDV(self):
        return self.RDV

    def setRDV(self,RDV:RDV):
        self.RDV = RDV  
    
    def getRapport(self):
        return self.rapport

    def setRapport(self,rapport):
        self.rapport = rapport  

