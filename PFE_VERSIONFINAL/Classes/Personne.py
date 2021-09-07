# Personne : une classe abstraite qui regroupe les attributs commun
# des 3 class Medecin,Secretair,Patient

from abc import ABC,abstractmethod

class Personne(ABC):
   
    def __init__(self,nom,prenom,ddn,numerotele,adresse,sexe): 
          self.nom = nom 
          self.prenom = prenom 
          self.date_naissance = ddn 
          self.numeroTelephone = numerotele
          self.adresse = adresse
          self.sexe = sexe 

 # Les acceseurs en ecriture et lecture  
     
    def getNom(self): 
         return self.nom

    def getPrenom(self): 
         return self.prenom

    def getDateNaissance(self): 
         return self.date_naissance

    def getNumeroTele(self): 
         return self.numeroTelephone

    def getAdresse(self):
         return self.adresse  

    def getSexes(self):
         self.sexe    
        
    def setNom(self,nom):
         self.nom = nom

    def setPrenom(self,prenom):
         self.prenom = prenom

    def setDateNaissance(self,ddn):
         self.nom = ddn

    def setNumeroTelephone(self,numerot):
         self.numeroTelephone = numerot

    def setAdresse(self,adresse):
         self.adresse = adresse

    def setSexe(self,sexe):
         self.sexe = sexe
    
    @abstractmethod
    def getLogin(self):
        pass

    @abstractmethod
    def getPassword(self):
        pass

    @abstractmethod
    def setLogin(self,login):
        pass

    @abstractmethod
    def setPassword(self,password):
        pass 

           


   



    



