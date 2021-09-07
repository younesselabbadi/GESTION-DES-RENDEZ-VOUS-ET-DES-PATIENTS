# Class patient

from Personne import Personne 
from  Lien_DB import CreationDB

class Patient(Personne):

    # Constructeur 
    def __init__(self,numeroCIN,numeroAssur,numeroP:int,nom:str,prenom:str,ddn,numerotele,adresse,sexe): 
        super().__init__(nom,prenom,ddn,numerotele,adresse,sexe)
        self.numeroCIN = numeroCIN
        self.numerAssur = numeroAssur
        self.numeroP = numeroP
    # methodes
    def afficher(self): 
        if self.sexe.upper() == "M" :
          entete = "Mr"

        else: 
            entete = "Mme"  

        return entete+" : {} {} \n date-Naissance : {} \n NumeroTelephone : {} \n Adresse : {} ".format(self.prenom,self.nom,self.date_naissance,self.numeroTelephone,self.adresse)    
    
    def getRDV(self,RDV):
        return self.RDV 

    def setRDV(self,RDV):
        self.RDV = RDV 

    def getNassurance(self): 
        return self.numerAssur
    
    def setNassurance(self,numeroA):
        self.numerAssur = numeroA     

    def getNpatient(self):
        return self.numeroP 

    def setNpatient(self,numero):
        self.numeroP = numero  

    def getNcin(self):
        return self.numeroCIN

    def setNcin(self,numero):
        self.numeroCIN = numero   

    def getLogin(self):
        pass

    def getPassword(self):
        pass

    def setLogin(self,login):
        pass

    def setPassword(self,password):
        pass

    def afficherDossierMedicale(self): 
         return False

#TEST