from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED,messagebox,Button,ttk
import datetime
from RDV import RDV 
import Fonction_Affichage_RDV,Fenetre_Gerer_RDV

class Fenetre_Affichage_RDV_Medecin(): 

    def __init__(self): 

        self.fenetre = Tk()
        self.fenetre.title("Emploi de Medecin")
        self.cadrevide = True
        color='#99ffff'
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.fenetre.configure(background=color) 
        self.fenetre.resizable(width=True, height=True)
        self.cadre = Frame(self.fenetre,bg=color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=3) 
        self.label_numero_Medecin = Label(self.cadre,text=" Medecin : ",width=20,font=("bold", 10),bg=color)
        listmedecin = Fenetre_Gerer_RDV.Fenetre_Gerer_RDV.listeMedecin()
        self.champ_Medecin = ttk.Combobox(self.cadre,values=listmedecin,width=17)
        self.bouton_envoyer = Button(self.cadre,text="valider",command=self.envoyer) 
        self.label_numero_Medecin.grid(row=0,column=0)
        self.champ_Medecin.grid(row=0,column=2)
        self.bouton_envoyer.grid(row=0,column=3,padx=2)
        self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid',bg="#99ffff")
        self.fenetre.mainloop()


    def envoyer(self):
        
        nomMedecin = self.champ_Medecin.get()[3:]
        reponserequeteMedecin = CreationDB.collectionMedecin.find_one({"Nom":nomMedecin},
                                                                        {"_id":0})

        

        if reponserequeteMedecin != None: 

            if self.cadrevide == False:
                self.cadreTab.destroy()
                self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid',bg="#99ffff")
                
            
            Fonction_Affichage_RDV.Affichage_RDV_Medecin(self.cadreTab,reponserequeteMedecin)

            self.cadrevide=False

            self.cadreTab.pack(pady=3)  
           
        
        else: 
            messagebox.showerror("Error", "Medecin Introuvable")
           
        


        
        self.fenetre.mainloop()
       



if __name__ == "__main__": 
   Fenetre_Affichage_RDV_Medecin().fenetre.mainloop()