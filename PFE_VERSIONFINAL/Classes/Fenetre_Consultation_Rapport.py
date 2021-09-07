import webbrowser
from tkinter import Tk,Label,Frame,Entry,Button,messagebox 

from Lien_DB import CreationDB



class Fenetre_Consultation_Rapport():

    def __init__(self,numrdv,numpatient,nummed):

        self.numrdv = numrdv
        self.numpatient = numpatient
        self.nummed = nummed

        reponseRapport = CreationDB.collectionRapport.find_one(
                                                                {"$and":
                                                                [
                                                                {"NumPat":self.numpatient
                                                                },
                                                                {"NumRDV":self.numrdv
                                                                }
                                                                ]
                                                                },
                                                                {"_id":0}
                                                                )

        if reponseRapport:
            chemine = reponseRapport['Chemine']
            webbrowser.open(chemine,new=2)
        else:
            messagebox.showerror("Rapport introuvable","Aucun rapport n'est trouvee")            


if __name__ == "__main__":

    Fenetre_Consultation_Rapport(6,0,2)

