#classe Rendez-vous

from Medecin import Medecin
from Patient import Patient

class RDV():

    def __init__(self,numeroRDv,nummedecin,numpatient,motif,date,heure):
       self.numeroRDv = numeroRDv
       self.numeroMedecin = nummedecin 
       self.numpatient = numpatient 
       self.motif = motif 
       self.date = date
       self.heure = heure
       self.annuler = False 
       self.consultation = None
    def annulerRDV(self):
        self.annuler = True

    def getMedecin(self):
        return self.numeroMedecin     

    def setMedecin(self,nummedecin):
        self.numeroMedecin = nummedecin 
    
    def getNRDV(self):
        return self.numeroRDv     

    def setNRDV(self,numer):
        self.numeroRDv = numer 

    def getPatient(self):
        return self.numpatient     

    def setPatient(self,patient):
        self.numpatient = patient 

    def getMotif(self):
        return self.motif

    def setMotif(self,motif):
        self.motif = motif  

    def getConsultation(self):
        return self.consultation

    def setConsultation(self,consultation):
        self.consultation = consultation  

    def getDate(self):
        return self.date 

    def setDate(self,date):
        self.date = date   
    
    def getHeure(self):
        return self.heure 

    def setHeure(self,heure):
        self.heure = heure 

    def afficherRDV(self): 
        return "Numero-RDV : {} \n Patient : {} \n Medecin : {} \n Motif : {} \n Date-RDV : {} \n".format( 
            self.numeroRDv,self.numpatient,self.numeroMedecin,self.motif,self.date)


