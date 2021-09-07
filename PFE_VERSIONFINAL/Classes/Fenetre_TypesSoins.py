from Lien_DB import CreationDB 
from tkinter import Tk,Button,Frame
import Fenetre_Login 
from Fenetre_Affichage_Soin import Fenetre_Affichage_Soin
from tkinter.font import Font


class Fenetre_TypesSoins(): 

    def __init__(self):  
        #initialisation de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("Fenetre d'inscription")
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        self.fenetre.title("Les Soins Disponibles : ")
        self.fenetre.resizable(width=False, height=False)
        self.cadre = Frame(self.fenetre)  
        self.cadre.pack() 

        font = Font(weight='bold',size=14)
        color = '#006666'
        i=1 
        j=1
        indice = 0
        self.listButton = list() 
        # Ce code permet de recupere tous les soins de la base de donnees 
        # et l'afficher sous forme des boutons
        for soin in CreationDB.collectionSoin.find({},{'Nom':1}):
            
            nom = soin['Nom']
            # on a utiliser lambda nom = nom : fonction d'affichage parceque en premier lieu pour passer un argument a la methode
            # et pour changer le parametre nom dans lambda puisque il change a chaque iteration on doit l'affecter
            self.listButton.append(Button(self.cadre, text=nom,width=20,height=8,bg=color,fg='white',font=font,bd=3,command=lambda nom=nom: self.afficher_info_soin(nom)))

            if j == 5 :

               i = i+1
               j=1
               self.listButton[indice].grid(row=i,column=j) 
              
            else:

              self.listButton[indice].grid(row=i,column=j)  
             
            j = j +1   
            indice = indice +1 

    def  afficher_info_soin(self,nom):
        f = Fenetre_Affichage_Soin(nom) 
        f.fenetre.mainloop()   

if __name__ == '__main__':   

    f = Fenetre_TypesSoins()
    f.fenetre.mainloop() 