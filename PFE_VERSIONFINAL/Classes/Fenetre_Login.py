from tkinter import messagebox 
from Lien_DB import CreationDB 
from tkinter.font import Font
import Fenetre_inscription,Fenetre_Menu_Secretaire 
import Fenetre_Menu_Medecin
from tkinter import Tk,Label,Entry,Button,font,messagebox,Frame,PhotoImage,LEFT,RIGHT
from datetime import datetime,timedelta
import Pmw


class FenetreLogin(): 

    def __init__(self): 

        #intialisation de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("Fenetre d'authentification")
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        geo = '{}x{}+{}+{}'.format(800,345,(largeurEcran // 2) - 400,(hauteurEcran // 2) - 235)
        self.fenetre.geometry(geo)  
        self.fenetre.resizable(width=False, height=False)

        #fond d'ecran
        image_fond = PhotoImage(file="Classes\\IHM\\login2.png")  
        image_label = Label(self.fenetre,image=image_fond)
        image_label.place(x=0,y=0,relwidth=1,relheight=1) 
        
        #Creation et insertion des composants 
        color = '#C3e4f7'
        cadre = Frame(self.fenetre,bg=color,bd=30) 
        cadre.grid(padx=40,pady=40) 
        my_font = Font(family="Curlz MT",size=30, slant="italic")
        text_font = Font(family="fantasy",size=12,)
        self.label_titre = Label(cadre,text="LOGIN ",pady=10,bg=color,font=my_font)
        self.label_pseudo = Label(cadre,text="Pseudo :",bg=color,font=text_font)
        self.label_password = Label(cadre,text="Mot de passe :",bg=color,font=text_font)
        self.champ_pseudo = Entry(cadre)
        self.champ_password = Entry(cadre,show="*")
        self.boutton_confirmation = Button(cadre,text="Confirmer",command=self.verificationAuthe,font=text_font) 
        self.boutton_creation = Button(cadre,text="Effacer",command=self.Effacer,font=text_font)
        self.label_titre.pack()
        self.label_pseudo.pack()
        self.champ_pseudo.pack()
        self.label_password.pack()
        self.champ_password.pack()
        self.boutton_confirmation.pack(pady=10,padx=10,side=LEFT) 
        self.boutton_creation.pack(side = RIGHT)
        self.fenetre.mainloop() 

        #methode de test d'authentification
    
    def verificationAuthe(self):
        # pour verifier est ce que l'utilisateur a remplis tous les champs de saissie
        if self.champ_pseudo.get() == "" or self.champ_password.get()== "":

           messagebox.showerror("Error", "Veuillez Remplir tous Les Champs !!")

        else: 
            # On Envoie une requete a la DataBase pour verifier les coordonnees de l'utilisatuer
            login = self.champ_pseudo.get()
            password = self.champ_password.get()
            test_secretaire = CreationDB.collectionSecretaire.find_one({"Login":login,"Password":password},{})  
            test_medecin =  CreationDB.collectionMedecin.find_one({"Login":login,"Password":password},{})
            test_Admin =  CreationDB.collectionAdmin.find_one({"pseudo":login,"password":password},{})

            if test_secretaire != None:  
                # si c'est la secretaire on ouvre la session de la secretaire
                self.fenetre.destroy()
                f = Fenetre_Menu_Secretaire.Fenetre_Menu_Secretaire() 
                f.fenetre

            elif test_medecin !=None:
                # si c'est le medecin on ouvre la session du medecine , A continuer 
                self.fenetre.destroy()
                f = Fenetre_Menu_Medecin.Fenetre_Menu_Medecin()
                f.fenetre
            elif test_Admin != None :  
                self.fenetre.destroy()
                Fenetre_inscription.Fenetre_inscription().fenetre 

            else: 
                #si on trouve pas d'element on affiche une erreur 
                messagebox.showerror("Error", "Pseudo/mot de passe incorrect !!")    

    def Effacer(self):
         self.champ_pseudo.delete(0, 'end') 
         self.champ_password.delete(0,'end')
         

if __name__ == '__main__':   

    f = FenetreLogin() 
    f.fenetre.mainloop()  
