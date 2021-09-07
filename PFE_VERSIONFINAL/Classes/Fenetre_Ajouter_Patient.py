from Lien_DB import CreationDB 
from tkinter import Tk,Frame,Label,Entry,messagebox,Button,Radiobutton,StringVar
from tkinter.font import Font
import Fenetre_inscription,Fonction_Affichage_RDV 
from tkcalendar import DateEntry
import os



class Fenetre_Ajouter_Patient(): 

    def __init__(self):  

        #initialisation de la fenetre

        self.fenetre = Tk()
        self.fenetre.title("Ajouter Patient")
        #self.fenetre.iconbitmap("Classes//IHM//logo.ico")
        self.fenetre.resizable(width=False, height=False)
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.cadre = Frame(self.fenetre)  
        self.cadre.pack() 

       
        
        self.label_numero_cin = Label(self.cadre,text="Numero CIN :") 
        self.champ_numero_cin = Entry(self.cadre)

        self.label_numero_assurance = Label(self.cadre,text="Numero d'assurance :") 
        self.champ_numero_assurance = Entry(self.cadre)
        

        self.label_nom = Label(self.cadre,text="Nom Patient:") 
        self.champ_nom = Entry(self.cadre) 
        

        self.label_prenom = Label(self.cadre,text="Prenom Patient:") 
        self.champ_prenom= Entry(self.cadre)
        

        self.label_date_naissance = Label(self.cadre,text="Date de naissance :") 
        self.champ_date_naissance = DateEntry(self.cadre,width=18) 
        self.champ_date_naissance.delete(0,'end')
        
        

        self.label_numero = Label(self.cadre,text="Telephone :") 
        self.champ_numero = Entry(self.cadre)
       


        self.label_adresse = Label(self.cadre,text="Adresse :") 
        self.champ_adresse = Entry(self.cadre) 

        self.label_sexe = Label(self.cadre, text=" Sexe :",width=20,font=("bold", 10))
        self.label_sexe.place(x=80,y=205) 
        self.sexe = StringVar()
        self.radiom = Radiobutton(self.cadre, text="Male",padx = 5,variable= self.sexe , value = "M")
        self.radiom.place(x=250,y=205)
        self.radiof = Radiobutton(self.cadre, text="Female",padx = 20,variable= self.sexe , value = "F")
        self.radiof.place(x=305,y=205)
       
            
        self.bouton_Ajouter =Button(self.cadre,width=10,height=1,text="Confirmer",bg='brown',command=self.ajouterPatient)
        self.bouton_Annuler =Button(self.cadre,width=10,height=1,text="Annuler",bg='brown')
            
        self.label_numero_cin.grid(row=2,column=2,columnspan=2,rowspan=2)
        self.champ_numero_cin.grid(row=2,column=4,columnspan=4,rowspan=2) 
        self.label_numero_assurance.grid(row=4,column=2,columnspan=2,rowspan=2)
        self.champ_numero_assurance.grid(row=4,column=4,columnspan=4,rowspan=2)
        self.label_nom.grid(row =6 , column= 2,columnspan=2,rowspan=2) 
        self.champ_nom.grid(row=6 ,column = 4,columnspan=4,rowspan=2)
        self.label_prenom.grid(row=8,column =2,columnspan=2,rowspan=2)
        self.champ_prenom.grid(row=8,column=4,columnspan=4,rowspan=2)
        self.label_date_naissance.grid(row=10,column=2,columnspan=2,rowspan=2)
        self.champ_date_naissance.grid(row=10,column=4,columnspan=4,rowspan=2)
        self.label_numero.grid(row=12,column=2,columnspan=2,rowspan=2)
        self.champ_numero.grid(row=12,column=4,columnspan=4,rowspan=2)
        self.label_adresse.grid(row=14,column=2,columnspan=2,rowspan=2)
        self.champ_adresse.grid(row=14,column=4,columnspan=4,rowspan=2)
        self.label_sexe.grid(row=16,column=2,columnspan=2,rowspan=2)
        self.radiom.grid(row=16,column=4)
        self.radiof.grid(row=16,column=6)
        self.bouton_Ajouter.grid(row=18,column=3)
        self.bouton_Annuler.grid(row=18,column=5)

    def ajouterPatient(self):

        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        date = Fonction_Affichage_RDV.convertisseurDate(self.champ_date_naissance.get())
        numero = self.champ_numero.get()
        adresse = self.champ_adresse.get()  
        ncin = self.champ_numero_cin.get()
        nassur = self.champ_numero_assurance.get()
        sexe = self.sexe.get()  

        testNomPrenom =(any( char.isdigit() for char in nom)) or (any( char.isdigit() for char in prenom)) or (nom == '' or prenom == '' )
        testdate = Fenetre_inscription.Fenetre_inscription.testDate(date,3)
        testnumero = Fenetre_inscription.Fenetre_inscription.testNumero(numero)
        testadresse =  len(adresse)==0  

        if len(nom)==0 and len(prenom) ==0 and len(date) ==0 and len(numero)==0 and len(adresse) == 0 and len(ncin)==0 and len(nassur)==0 :
             messagebox.showerror("Les Champs Sont Vides" ,"Veuillez Remplir Tous  Les  Champs ")
        elif not (testdate):
            messagebox.showerror("Date-invalide /format invalide","veuillez resaisir la date ")
        elif testnumero:
            messagebox.showerror("Format numero invalide","veuillez resaisir le numero ")    
        elif testadresse:
             messagebox.showerror("Adresse vide ","veuillez Entrer l'adresse ") 
        elif testNomPrenom:
            messagebox.showerror("nom/prenom invalide","Veuillez Saisir le nom et le prenom correctement ")
        elif len(ncin) == 0:
             messagebox.showerror("Numero CIN vide","veuillez Entrer le Numero CIN")
        elif len(nassur)==0:
            messagebox.showerror("Numero Assurance vide","Veuillez Entre le Numero D'Assurance")
        elif len(sexe)=='':
             messagebox.showerror("Sexe non-indiquee","veuillez choisir un sexe")
        elif testadresse:
             messagebox.showerror("Adresse vide ","veuillez Entrer l'adresse ")
        else:

            idpatient = Fonction_Affichage_RDV.GenererID("Patient")
            reponsePatient = CreationDB.collectionPatient.insert_one({"NumPat":idpatient,
                                                                      "NumAssur":nassur,
                                                                      "NumCIN":ncin,
                                                                      "Nom":nom,
                                                                      "Prenom":prenom,
                                                                      "Numero-telephone":numero,
                                                                      "Date-naissance":date,
                                                                      "Sexe":sexe, 
                                                                      "Adresse":adresse,
                                                                      })
            if reponsePatient:
                messagebox.showinfo("Confirmation D'ajout","Le Patient Est Ajoutee Avec Le Numero : "+str(idpatient)) 
                Fenetre_Ajouter_Patient.creationRepertoirPatient(nom,prenom,idpatient)
                self.fenetre.destroy()
            else:
                messagebox.showerror("Erreur lors De L'Ajout"," Un Erreur Est Servenu,Veuillez Recommencer Plus Tard ")

    @staticmethod
    def creationRepertoirPatient(nomP,prenomP,numeroP):

        dossier = ".//DossierdesPatients//"+nomP+"_"+prenomP
        sousdossierrapport = dossier+"//Rapport"
        sousdossiercertificat = dossier+"//Certificat"

        try:  
            os.mkdir(dossier)
            os.mkdir(sousdossierrapport)
            os.mkdir(sousdossiercertificat)
        except OSError:  
            messagebox.showerror("Erreur","La creation du repertoire est echouee")
        else:  
           pass

       
if __name__ == '__main__':   

    f = Fenetre_Ajouter_Patient()
    f.fenetre.mainloop() 
