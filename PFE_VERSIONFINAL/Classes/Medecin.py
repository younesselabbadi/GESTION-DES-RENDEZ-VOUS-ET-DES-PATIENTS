# Class Medecin 

from Personne import Personne 
from  Lien_DB import CreationDB

class Medecin(Personne):

    # Constructeur 
    def __init__(self,login,password,nom,prenom,ddn,numerotele,adresse,sexe): 
        super().__init__(nom,prenom,ddn,numerotele,adresse,sexe)
        self.login = login
        self.password = password
    #methodes
    def getRDV(self,RDV):
        return self.RDV 

    def setRDV(self,RDV):
        self.RDV = RDV 
    
    def getRapport(self,rapport):
        return self.rapport
    
    def setRapport(self,rapport):
        self.rapport = rapport 
    
    def getLogin(self):
        return self.login

    def getPassword(self):
        return self.password

    def setLogin(self,login):
        self.login = login

    def setPassword(self,password):
        self.password = password  

    def afficher(self):
        return " Dr : {} {} \n date-Naissance : {} \n NumeroTelephone : {} \n Adresse : {} ".format(self.prenom,self.nom,self.date_naissance,self.numeroTelephone,self.adresse)                  
#TEST        
def main(): 
    print(CreationDB.lienBD.list_database_names())   
      
if __name__ == "__main__" :
     main()  