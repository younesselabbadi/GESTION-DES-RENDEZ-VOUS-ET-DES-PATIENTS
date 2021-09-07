from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED,messagebox,Button 
from Patient import Patient
import Fonction_Affichage_RDV
from RDV import RDV 

class Fenetre_Affichage_Dossier_Patient(): 

    def __init__(self,medecin): 
        self.estMedecin = medecin
        self.fenetre = Tk()
        self.fenetre.title("Fenetre Dossier d'un patient")
        self.color='#99ffff'
        self.cadrevide=True
        self.fenetre.configure(background=self.color) 
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -500 ,(hauteurEcran // 2) - 200))
        self.fenetre.resizable(width=True, height=True)
        self.cadre = Frame(self.fenetre,bg=self.color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=5) 
        self.label_numero_patient = Label(self.cadre,text="Numero de Patient : ",width=20,font=("bold", 10),bg=self.color)
        self.champ_numero_patient = Entry(self.cadre)
        self.bouton_envoyer = Button(self.cadre,text="Valider",command=self.afficherDossier) 
        self.label_numero_patient.grid(row=0,column=0)
        self.champ_numero_patient.grid(row=0,column=2)
        self.bouton_envoyer.grid(row=0,column=3,padx=2) 
        self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid',bg=self.color)
        self.cadre_dossier =Frame(self.fenetre, borderwidth=1,relief='solid')

    def afficherDossier(self):  
        if  self.cadrevide==False: 
            self.cadre_dossier.destroy()
            self.cadreTab.destroy()
            self.cadre_dossier =Frame(self.fenetre, borderwidth=1,relief='solid')
            self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid',bg=self.color)
          
            self.cadrevide=True


        self.cadrevide=False
        Numeropatient = int(self.champ_numero_patient.get()) 

        reponserequete = CreationDB.collectionPatient.find_one({"NumPat":Numeropatient},{"_id":0})

        if reponserequete != None: 

            nom = reponserequete['Nom']
            prenom = reponserequete['Prenom']
            ddn = reponserequete['Date-naissance']
            numerotel = reponserequete['Numero-telephone']
            add = reponserequete['Adresse']
            sexe = reponserequete['Sexe']
            numerCIN = reponserequete['NumCIN']
            numeroassur = reponserequete['NumAssur']

            self.patient = Patient(numerCIN,numeroassur,Numeropatient,nom,prenom,ddn,numerotel,add,sexe)
            #patient.setRDV(reponserequete['RDV'])

            #Numero de Patient
            self.label_nom = Label(self.cadre_dossier, text="NPatient :" ,width=20,font=("bold", 10),bg=self.color)
            self.label_nom.grid(row=0,column=1)
            self.champ_nom= Entry(self.cadre_dossier,width=73)
            text=""+str(self.patient.getNpatient())
            self.champ_nom.insert(0,text)
            self.champ_nom.configure(state='readonly')
            self.champ_nom.grid(row=0,column=2)
            
             #Numero CIN de Patient
            self.label_nom = Label(self.cadre_dossier, text="NumeroCIN :" ,width=20,font=("bold", 10),bg=self.color)
            self.label_nom.grid(row=1,column=1)
            self.champ_nom= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getNcin()
            self.champ_nom.insert(0,text)
            self.champ_nom.configure(state='readonly')
            self.champ_nom.grid(row=1,column=2)
            
             #Numero d'Assurance de Patient
            self.label_nom = Label(self.cadre_dossier, text="Numero Assurance :" ,width=20,font=("bold", 10),bg=self.color)
            self.label_nom.grid(row=2,column=1)
            self.champ_nom= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getNassurance()
            self.champ_nom.insert(0,text)
            self.champ_nom.configure(state='readonly')
            self.champ_nom.grid(row=2,column=2)

            #nom de Patient
            self.label_dure = Label(self.cadre_dossier, text="nom :" ,width=20,font=("bold", 10),bg=self.color)
            self.label_dure.grid(row=3,column=1)
            self.champ_duree= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getNom()
            self.champ_duree.insert(0,text)
            self.champ_duree.configure(state='readonly')
            self.champ_duree.grid(row=3,column=2)
              
            #prenom de Patient
            self.valeur_prix = Label(self.cadre_dossier, text=" Prenom  :" ,width=20,font=("bold", 10),bg=self.color)
            self.valeur_prix.grid(row=4,column=1)
            self.champ_prix= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getPrenom()
            self.champ_prix.insert(0,text)
            self.champ_prix.configure(state='readonly')
            self.champ_prix.grid(row=4,column=2)
       
            #Date de naissance du Patient
            self.valeur_prix = Label(self.cadre_dossier, text=" Date de naissance :" ,width=20,font=("bold", 10),bg=self.color)
            self.valeur_prix.grid(row=5,column=1)
            self.champ_prix= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getDateNaissance()
            self.champ_prix.insert(0,text)
            self.champ_prix.configure(state='readonly')
            self.champ_prix.grid(row=5,column=2)

            #Numero telephone du Patient
            self.valeur_prix = Label(self.cadre_dossier, text=" Numero de telephone :" ,width=20,font=("bold", 10),bg=self.color)
            self.valeur_prix.grid(row=6,column=1)
            self.champ_prix= Entry(self.cadre_dossier,width=73)
            text=""+self.patient.getNumeroTele()
            self.champ_prix.insert(0,text)
            self.champ_prix.configure(state='readonly')
            self.champ_prix.grid(row=6,column=2)

            #Adresse du Patient
            self.label_description = Label(self.cadre_dossier, text=" Adresse :" ,width=20,height=3,font=("bold", 10),bg=self.color)
            self.label_description.grid(row=7,column=1)
            self.champ_description= Text(self.cadre_dossier,width=55,height=3,bg='#f5f5f0')
            text=""+self.patient.getAdresse()
            self.champ_description.insert('insert',text)
            self.champ_description.configure(state=DISABLED)
            self.champ_description.grid(row=7,column=2)

            #les RDVs

            test=False
            if 'RDV' in reponserequete:
                test = True
            if test:
                if reponserequete['RDV']:

                    Fonction_Affichage_RDV.Affichage_RDV_Patient(self.cadreTab,reponserequete,reponserequete["NumPat"],self.estMedecin)
               
            
            self.cadre_dossier.pack()
            self.cadreTab.pack(pady=3)
           
            

            

        else: 

            messagebox.showerror("Error", "patient introuvable")
            



       



if __name__ == "__main__": 
   Fenetre_Affichage_Dossier_Patient(True).fenetre.mainloop()