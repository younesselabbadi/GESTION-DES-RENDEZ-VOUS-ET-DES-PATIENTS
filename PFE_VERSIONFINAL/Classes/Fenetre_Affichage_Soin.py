from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED
from Soin import Soin


class Fenetre_Affichage_Soin(): 

    def __init__(self,Nomsoin): 

        self.fenetre = Tk()
        self.fenetre.title("Information du soin : "+Nomsoin)
        color='#99ffff'
        self.fenetre.configure(background=color)
        self.fenetre.resizable(width=False, height=False)
        self.cadre = Frame(self.fenetre,bg=color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=3) 
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        reponserequete = CreationDB.collectionSoin.find_one({"Nom":Nomsoin},{"_id":0})
        soin = Soin(Nomsoin,reponserequete['Duree'],reponserequete['Description'],reponserequete['prix'])
       
        
        #nom du soin
        self.label_nom = Label(self.cadre, text="Nom Soin :" ,width=20,font=("bold", 10),bg=color)
        self.label_nom.grid(row=1,column=1)
        self.champ_nom= Entry(self.cadre,width=73)
        text=""+soin.getnomSoin()
        self.champ_nom.insert(0,text)
        self.champ_nom.configure(state='readonly')
        self.champ_nom.grid(row=1,column=2)
        
        #duree du soin
        self.label_dure = Label(self.cadre, text="Duree de Soin :" ,width=20,font=("bold", 10),bg=color)
        self.label_dure.grid(row=2,column=1)
        self.champ_duree= Entry(self.cadre,width=73)
        text=""+soin.getDuree()
        self.champ_duree.insert(0,text)
        self.champ_duree.configure(state='readonly')
        self.champ_duree.grid(row=2,column=2)
              
        #prix du soin
        self.valeur_prix = Label(self.cadre, text=" Prix :" ,width=20,font=("bold", 10),bg=color)
        self.valeur_prix.grid(row=3,column=1)
        self.champ_prix= Entry(self.cadre,width=73)
        text=""+soin.getPrix()
        self.champ_prix.insert(0,text)
        self.champ_prix.configure(state='readonly')
        self.champ_prix.grid(row=3,column=2)
       

       
        #description du soin
        self.label_description = Label(self.cadre, text=" Description du Soin :" ,width=20,font=("bold", 10),bg=color)
        self.label_description.grid(row=4,column=1)
        self.champ_description= Text(self.cadre,width=55,height=6,bg='#f5f5f0')
        text=""+soin.getDescription()
        self.champ_description.insert('insert',text)
        self.champ_description.configure(state=DISABLED)
        self.champ_description.grid(row=4,column=2) 


        self.fenetre.mainloop()


if __name__ == "__main__": 
     Fenetre_Affichage_Soin("Détartrage").fenetre

