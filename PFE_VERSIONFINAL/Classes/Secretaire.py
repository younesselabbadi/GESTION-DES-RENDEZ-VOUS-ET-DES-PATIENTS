 # Class Secretaire 

from Personne import Personne

class Secretaire(Personne):

    # Constructeur 
    def __init__(self,login,password,nom,prenom,ddn,numerotele,adresse,sexe): 
        super().__init__(nom,prenom,ddn,numerotele,adresse,sexe)
        self.login = login
        self.password = password
    #methodes
    
    def getLogin(self):
        return self.login

    def getPassword(self):
        return self.password

    def setLogin(self,login):
        self.login = login

    def setPassword(self,password):
        self.password = password 

#Test 
def main(): 
    sec =Secretaire("oth","123","Othmane","Aja","27-01-1998","0654319970","rabat","M")
    print(sec.login)
    
if __name__ == "__main__":
     main()  
        


