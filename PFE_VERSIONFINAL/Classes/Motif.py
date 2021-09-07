#Classe Motif

from abc import ABC,abstractclassmethod

class Motif(ABC):

    def __init__(self , prix:float):
        self.prix =prix 
        self.RDV = None
    
    def getPrix(self): 
         return self.prix

    def setPrix(self,prix): 
        self.prix = prix

    def getRDV(self): 
         return self.RDV

    def setRDV(self,RDV): 
        self.RDV = RDV   