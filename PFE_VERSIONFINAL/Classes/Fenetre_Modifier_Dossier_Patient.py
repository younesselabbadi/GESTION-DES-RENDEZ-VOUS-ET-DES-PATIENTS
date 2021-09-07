from Lien_DB import CreationDB 
from tkinter import Tk,Frame,Label,Entry,messagebox,Button
import Fenetre_Login,Fenetre_inscription,Fenetre_inscription
from Fenetre_Affichage_Soin import Fenetre_Affichage_Soin
from tkinter.font import Font
from tkcalendar import DateEntry
import Fonction_Affichage_RDV


class Fenetre_Modifier_Dossier_Patient(): 

    def __init__(self):  

        #initialisation de la fenetre

        self.fenetre = Tk()
        self.fenetre.title("Fenetre Modification d'un patient")
        self.color='#99ffff'
        self.fenetre.configure(background=self.color) 
        self.fenetre.resizable(width=True, height=True)
        self.cadre = Frame(self.fenetre,bg=self.color, borderwidth=1,relief='solid')
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.cadre.pack(padx=2,pady=3) 
        self.label_numero_patient = Label(self.cadre,text="Numero de Patient : ",width=20,font=("bold", 10),bg=self.color)
        self.champ_numero_patient = Entry(self.cadre)
        self.bouton_envoyer = Button(self.cadre,text="Valider",command=self.afficherForm) 
        self.label_numero_patient.grid(row=0,column=0)
        self.champ_numero_patient.grid(row=0,column=2)
        self.bouton_envoyer.grid(row=0,column=3,padx=2) 
        self.cadre_modification = Frame(self.fenetre,bg='#99ffff',borderwidth=1,relief='solid')

    def afficherForm(self):

        self.numeroPatient = self.champ_numero_patient.get() 
        
        reponse = CreationDB.collectionPatient.find_one({"NumPat":int(self.numeroPatient)},{"_id":0})
       

        if reponse != None:
           
            nom =str(reponse['Nom'])
            prenom = str(reponse['Prenom'])
            ddn = str(reponse['Date-naissance'])
            adresse = str(reponse['Adresse'])
            numtel = str(reponse['Numero-telephone']) 

            self.label_numero_patient = Label(self.cadre_modification,text="Numero  Patient:",bg=self.color) 
            self.champ_numero_patient = Entry(self.cadre_modification)
            self.champ_numero_patient.insert(0,self.numeroPatient)
            self.champ_numero_patient.configure(state='readonly') 

            self.label_nom = Label(self.cadre_modification,text="Nom Patient:",bg=self.color) 
            self.champ_nom = Entry(self.cadre_modification) 
            self.champ_nom.insert(0,str(nom))
            self.champ_nom.configure(state='readonly') 

            self.label_prenom = Label(self.cadre_modification,text="Prenom Patient:",bg=self.color) 
            self.champ_prenom= Entry(self.cadre_modification)
            self.champ_prenom.insert(0,str(prenom))
            self.champ_prenom.configure(state='readonly')

            self.label_date_naissance = Label(self.cadre_modification,text="Date de naissance :",bg=self.color) 
            self.champ_date_naissance = DateEntry(self.cadre_modification,width=18)
            self.champ_date_naissance.delete(0,'end')
            self.champ_date_naissance.insert(0,str(ddn))
            self.champ_date_naissance.configure(state='disabled')

            self.label_numero = Label(self.cadre_modification,text="Numero :",bg=self.color) 
            self.champ_numero = Entry(self.cadre_modification)
            self.champ_numero.insert(0,str(numtel))
            self.champ_numero.configure(state='readonly')


            self.label_adresse = Label(self.cadre_modification,text="Adresse :",bg=self.color) 
            self.champ_adresse = Entry(self.cadre_modification)
            self.champ_adresse.insert(0,str(adresse))
            self.champ_adresse.configure(state='readonly')
            
            self.bouton_modifier =Button(self.cadre_modification,width=10,height=1,text="modifier",bg='brown',command=self.modifier)
            
            self.label_numero_patient.grid(row=0,column=2,columnspan=2,rowspan=2)
            self.champ_numero_patient.grid(row=0,column=4,columnspan=4,rowspan=2)
            self.label_nom.grid(row =2 , column= 2,columnspan=2,rowspan=2) 
            self.champ_nom.grid(row=2 ,column = 4,columnspan=4,rowspan=2)
            self.label_prenom.grid(row=4,column =2,columnspan=2,rowspan=2)
            self.champ_prenom.grid(row=4,column=4,columnspan=4,rowspan=2)
            self.label_date_naissance.grid(row=6,column=2,columnspan=2,rowspan=2)
            self.champ_date_naissance.grid(row=6,column=4,columnspan=4,rowspan=2)
            self.label_numero.grid(row=8,column=2,columnspan=2,rowspan=2)
            self.champ_numero.grid(row=8,column=4,columnspan=4,rowspan=2)
            self.label_adresse.grid(row=10,column=2,columnspan=2,rowspan=2)
            self.champ_adresse.grid(row=10,column=4,columnspan=4,rowspan=2)
            self.bouton_modifier.grid(row=12,column=3) 
            self.cadre_modification.pack()
       
       
        else: 
            messagebox.showerror("Error", "patient introuvable")



    def modifier(self):
        self.champ_nom.config(state="normal")
        self.champ_prenom.config(state="normal")
        self.champ_date_naissance.config(state="normal")
        self.champ_numero.config(state="normal")
        self.champ_adresse.config(state="normal")
        self.bouton_valider = Button(self.cadre_modification,width=7,height=1,text="Valider",bg='brown',command=self.valider) 
        self.bouton_modifier.destroy()
        self.bouton_valider.grid(row=14,column=4)
        
    def valider(self):
        test_vide = self.champ_nom.get() == "" or self.champ_prenom.get() == "" or self.champ_adresse.get() == "" or self.champ_numero.get() == "" or self.champ_date_naissance.get() == ""

        if test_vide:
            messagebox.showerror("Error", "Un champ est vide")
        else:
            nom = self.champ_nom.get()
            prenom = self.champ_prenom.get()
            add = self.champ_adresse.get()
            numerot = self.champ_numero.get()
            ddn = Fonction_Affichage_RDV.convertisseurDate(self.champ_date_naissance.get())
            testNumero = Fenetre_inscription.Fenetre_inscription.testNumero(numerot)
            testdate = not(Fenetre_inscription.Fenetre_inscription.testDate(ddn,0))
            testNomPrenom = (any( char.isdigit() for char in nom)) or (any( char.isdigit() for char in prenom)) or (nom == '' or prenom == '' )
            if testdate or testNumero or testNomPrenom: 

                messagebox.showerror("Error", "Champ mal")
            else:
                reponse = CreationDB.collectionPatient.update_one({"NumPat":int(self.numeroPatient)},{"$set":{"Nom":nom,"Prenom":prenom,"Numero-telephone":numerot,"Date-naissance":ddn,"Adresse":add}},upsert=False) 
                if reponse:
                    messagebox.showinfo("Confirmation de la mise a jour","Les mises a jours sont faite avec succes")
                    self.fenetre.destroy()
                else:
                    messagebox.showerror("Erreur", "Une erreur c'est servenue lors de la mise a jour")
if __name__ == '__main__':   

    f = Fenetre_Modifier_Dossier_Patient()
    f.fenetre.mainloop() 
