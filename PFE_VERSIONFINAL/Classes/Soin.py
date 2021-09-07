#Classe Soin herite de motif


from Motif import Motif

class Soin(Motif): 

    def __init__(self,nomsoin:str,duree:str,description,prix): 
        super().__init__(prix)
        self.nomsoin = nomsoin 
        self.duree = duree 
        self.description =description
        self.Rapport = None
        
    def getnomSoin(self):
        return self.nomsoin

    def setnomSoin(self,Rapport):
        self.nomsoin =Rapport   

    def getDuree(self):
        return self.duree

    def setDuree(self,duree):
        self.duree = duree  

    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description =description     


    def getRapport(self):
        return self.Rapport

    def setRapport(self,Rapport):
        self.Rapport =Rapport   

    def afficherSoinInfos(self):
        return "Nom : {} \n Duree : {} \n Description : {} "     


    