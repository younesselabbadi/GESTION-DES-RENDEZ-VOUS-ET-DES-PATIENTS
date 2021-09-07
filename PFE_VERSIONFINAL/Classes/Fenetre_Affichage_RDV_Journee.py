from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED,messagebox 
from datetime import datetime
from RDV import RDV 
import Fonction_Affichage_RDV

class Fenetre_Affichage_RDV_Journee(): 

    def __init__(self): 

        self.fenetre = Tk()
        self.fenetre.title("Emploi de la journee")
        color='#99ffff'
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.fenetre.configure(background=color) 
        self.fenetre.resizable(width=True, height=True)
        self.cadre = Frame(self.fenetre,bg=color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=3) 
        date_courante = datetime.now().strftime('%Y-%m-%d')
        
        print(date_courante)
        # reponserequete = CreationDB.collectionRDV.find({"Date":date_courante},{"_id":0})
        
        # if reponserequete == None or len(list(reponserequete)) == 0 : 
        #     messagebox.showerror("Error", "Aucune Rendez-Vous Prevu Pour Cette Journee")
        #     self.fenetre.destroy()
        
        # if reponserequete != None: 

           
        self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid',bg=color)
        Fonction_Affichage_RDV.Affichage_RDV_Journee(self.cadreTab,date_courante)
        self.cadreTab.pack(pady=3)   

       
        


        
        self.fenetre.mainloop()
       



if __name__ == "__main__": 
   Fenetre_Affichage_RDV_Journee().fenetre.mainloop()
