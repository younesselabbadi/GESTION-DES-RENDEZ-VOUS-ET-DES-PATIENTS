from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Radiobutton,StringVar,Button,font,messagebox,Frame 
import Fenetre_Login,Fonction_Affichage_RDV
from datetime import datetime,timedelta
from tkcalendar import DateEntry

import re
#from Pmw import Balloon


class Fenetre_inscription(): 

    def __init__(self):  
        #initialisation de la fenetre
        self.cadrevide = True
        self.fenetre = Tk()
        self.fenetre.title("Fenetre d'inscription")
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        geo = '{}x{}+{}+{}'.format(500,500,(largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250)
        self.fenetre.geometry(geo)  
        self.fenetre.resizable(width=False, height=False) 
        #self.bulle_ddn = Balloon(self.fenetre)
        #self.bulle_numerot = Balloon(self.fenetre) 
        self.cadrebouton = Frame(self.fenetre,pady=20)
        self.boutonAjouter = Button(self.cadrebouton, text='Ajouter Un Compte',width=20,bg='brown',fg='white',command=self.creeCompte)
        self.boutonAjouter.grid(row=1,column=1)
        self.boutonModifier = Button(self.cadrebouton, text='Modifier Un Compte',width=20,bg='brown',fg='white',command=self.formulaireRecherche)
        self.boutonModifier.grid(row=1,column=2)
        self.boutonSupprimer = Button(self.cadrebouton, text='Supprimer Un  Compte',width=20,bg='brown',fg='white',command=self.Supprimer)
        self.boutonSupprimer.grid(row=1,column=3)
        self.cadrebouton.pack()
        self.cadre = Frame(self.fenetre)
        self.cadreTitre = Frame(self.fenetre)
        self.cadrebouton2 = Frame(self.fenetre)
        

    def creeCompte(self):

        if  self.cadrevide==False: 

            self.cadre.destroy()
            self.cadreTitre.destroy()
            self.cadrebouton2.destroy()
            self.cadre = Frame(self.fenetre)
            self.cadreTitre = Frame(self.fenetre)
            self.cadrebouton2 = Frame(self.fenetre)
            self.cadrevide=True
        
        
        
        #Text 
        
        self.label_titre = Label(self.cadreTitre, text="Enregistrement",width=20,font=("bold", 20))
        self.label_titre.pack()
        self.cadreTitre.pack(pady=20)
        
        #Nom
        self.label_nom = Label(self.cadre, text=" Nom :" ,width=20,font=("bold", 10))
        self.label_nom.grid(row=1,column=0)
        self.input_nom = Entry(self.cadre)
        self.input_nom.grid(row=1,column=1)

        #Prenom
        self.label_prenom = Label(self.cadre, text=" Prenom :",width=20,font=("bold", 10))
        self.label_prenom.grid(row=2,column=0)
        self.input_prenom = Entry(self.cadre)
        self.input_prenom.grid(row=2,column=1)

        #Date Naissance
        self.label_ddn = Label(self.cadre, text=" Date Naissance :",width=20,font=("bold", 10))
        self.label_ddn.grid(row=3,column=0)
        self.input_ddn = DateEntry(self.cadre,width=18)
        self.input_ddn.grid(row=3,column=1) 
        

        #Sexe
        self.label_sexe = Label(self.cadre, text=" Sexe :",width=20,font=("bold", 10))
        self.label_sexe.grid(row=4,column=0) 
        self.valeursexe = StringVar()
        self.radiom = Radiobutton(self.cadre, text="Male",padx = 5,variable= self.valeursexe , value = "M")
        self.radiom.grid(row=4,column=1)
        self.radiof = Radiobutton(self.cadre, text="Female",padx = 20,variable= self.valeursexe , value = "F")
        self.radiof.grid(row=5,column=1)

        #Numero Telephone
        self.label_nt= Label(self.cadre, text=" Numero Telephone :",width=20,font=("bold", 10))
        self.label_nt.grid(row=6,column=0)
        self.input_nt = Entry(self.cadre)
        self.input_nt.grid(row=6,column=1)
        

        
        #Adresse
        self.label_add= Label(self.cadre, text=" Adresse :",width=20,font=("bold", 10))
        self.label_add.grid(row=7,column=0)
        self.input_add = Entry(self.cadre)
        self.input_add.grid(row=7,column=1)

        #type_session
        self.label_session = Label(self.cadre, text=" Session :",width=20,font=("bold", 10))
        self.label_session.grid(row=8,column=0) 
        self.valeursession = StringVar()
        self.radiom = Radiobutton(self.cadre, text="Medecin",padx = 5,variable= self.valeursession , value = "M")
        self.radiom.grid(row=8,column=1)
        self.radiof = Radiobutton(self.cadre, text="Secretaire",padx = 20,variable= self.valeursession , value = "S")
        self.radiof.grid(row=9,column=1)
        
        #Pseudo
        self.label_pseudo= Label(self.cadre, text=" Pseudo :",width=20,font=("bold", 10))
        self.label_pseudo.grid(row=10,column=0)
        self.input_pseudo = Entry(self.cadre)
        self.input_pseudo.grid(row=10,column=1)
        
        #Mot de Pass  
        self.label_mdp= Label(self.cadre, text=" Mot De Passe :",width=20,font=("bold", 10))
        self.label_mdp.grid(row=11,column=0)
        self.input_mdp = Entry(self.cadre,show='*')
        self.input_mdp.grid(row=11,column=1)
        
        #Confirmation du Mot de pass   
        self.label_cmdp= Label(self.cadre, text=" Ressaisie le Mot De Passe :",width=20,font=("bold", 10))
        self.label_cmdp.grid(row=12,column=0)
        self.input_cmdp = Entry(self.cadre,show='*')
        self.input_cmdp.grid(row=12,column=1)
        
        #Boutton Pour Envoyer    
        self.boutonC = Button(self.cadrebouton2, text='Confirmer',width=20,bg='brown',fg='white',command=self.valider)
        self.boutonC.grid(row=14,column=0)
        
        #Boutton Pour Annulation    
        self.boutonA = Button(self.cadrebouton2, text='Annuler',width=20,bg='brown',fg='white',command=self.annuler)
        self.boutonA.grid(row=14,column=1,padx=5)
        
        self.cadre.pack()
        self.cadrebouton2.pack(pady=20)
        self.cadrevide = False

    def formulaireRecherche(self):
        if  self.cadrevide==False: 

            self.cadre.destroy()
            self.cadreTitre.destroy()
            self.cadrebouton2.destroy()
            self.cadre = Frame(self.fenetre)
            self.cadreTitre = Frame(self.fenetre)
            self.cadrebouton2 = Frame(self.fenetre)
            self.cadrevide=True

        self.label_titre = Label(self.cadreTitre, text="Chercher Le Compte",width=20,font=("bold", 20))
        self.label_titre.pack()
        self.cadreTitre.pack(pady=20) 

        self.label_numeroCompte = Label(self.cadre,text=" Numero Compte : ")
        self.champ_numeroCompte = Entry(self.cadre)
        self.label_sessioncompte = Label(self.cadre, text=" Session :",width=20,font=("bold", 10))
        self.vs = StringVar()
        self.radiomedecin = Radiobutton(self.cadre, text="Medecin",padx = 5,variable= self.vs , value = "M")       
        self.radioseceretaire = Radiobutton(self.cadre, text="Secretaire",padx = 20,variable= self.vs , value = "S")
        self.label_numeroCompte.grid(row=0,column=0)
        self.champ_numeroCompte.grid(row=0,column=1)
        self.label_sessioncompte.grid(row=1,column=0)
        self.radiomedecin.grid(row=1,column=1)
        self.radioseceretaire.grid(row=2,column=1)

        self.boutonChercher = Button(self.cadre,text="Chercher",width=20,bg='brown',fg='white',command=self.chercher)
        self.boutonChercher.grid(row=3,column=1)
        self.cadre.configure(pady=30)
        self.cadre.pack()
    


        self.cadre.pack()
        self.cadrebouton2.pack(pady=20)
        self.cadrevide = False


    def chercher(self):
        nCompte = self.champ_numeroCompte.get()   
        self.session = self.vs.get()

        if not(nCompte.isdigit()):
            messagebox.showerror("Erreur ","Veuillez entrer un nombre ")
        elif self.session == "":
            messagebox.showerror("Erreur ","Veullez Choisir La Session")
        else:
            self.numeroCompte = int(nCompte)
            if self.session == "M":
                reponserequete = CreationDB.collectionMedecin.find_one({"NumMed":self.numeroCompte},{"_id":0}) 
                if reponserequete:
                    self.modifier(reponserequete)

            else:
                reponserequete = CreationDB.collectionSecretaire.find_one({"NumSecretaire":self.numeroCompte},{"_id":0})    
                if reponserequete:
                    self.modifier(reponserequete)
                else:
                    messagebox.showerror("Erreur","lors de l'acces a la BD")


    def modifierSession(self):
        nom = self.input_nom.get()
        prenom = self.input_prenom.get()
        date = Fonction_Affichage_RDV.convertisseurDate(self.input_ddn.get())
        numeroT = self.input_nt.get()
        pseudo = self.input_pseudo.get()
        adresse = self.input_add.get()
        password = self.input_mdp.get()
        test_nom_prenom = (any( char.isdigit() for char in nom)) or (any( char.isdigit() for char in prenom)) or (nom == '' or prenom == '' )
        test_numerot = Fenetre_inscription.testNumero(numeroT)
        test_adresse = len(adresse)==0 
        test_pseudo = len(pseudo) == 0  or pseudo[:1].isdigit() or len(pseudo) > 15 or len(password)==0
        test_ddn =  not (Fenetre_inscription.testDate(date,18)) 
        

        if test_nom_prenom or test_numerot or test_adresse or test_pseudo or test_ddn or test_adresse :

            messagebox.showerror("Erreur","Veuillez bien remplir le champ")    

        else:
            if self.session == "M":
                reponse = CreationDB.collectionMedecin.update_one({"NumMed":self.numeroCompte},
                                                                {"$set":
                                                                {"Nom":nom,
                                                                "Prenom":prenom,
                                                                "Numero-telephone":numeroT,
                                                                "Date-naissance":date,
                                                                "Adresse":adresse,
                                                                "Login":pseudo,
                                                                "Password":password
                                                                }
                                                                },
                                                                upsert=False) 
                if reponse:
                    messagebox.showinfo("Confirmation","Les MAJ sont faite")                                                
            else :
                reponse = CreationDB.collectionSecretaire.update_one({"NumSecretaire":self.numeroCompte},
                                                                {"$set":
                                                                {"Nom":nom,
                                                                "Prenom":prenom,
                                                                "Numero-telephone":numeroT,
                                                                "Date-naissance":date,
                                                                "Adresse":adresse,
                                                                "Login":pseudo,
                                                                "Password":password
                                                                }
                                                                },
                                                                upsert=False)                                                     
                if reponse:
                    messagebox.showinfo("Confirmation","Les MAJ sont faite")



    def modifier(self,requete):

        if  self.cadrevide==False: 

            self.cadre.destroy()
            self.cadreTitre.destroy()
            self.cadrebouton2.destroy()
            self.cadre = Frame(self.fenetre)
            self.cadreTitre = Frame(self.fenetre)
            self.cadrebouton2 = Frame(self.fenetre)
            self.cadrevide=True

        self.label_titre = Label(self.cadreTitre, text="Modifier Un Compte  ",width=20,font=("bold", 20))
        self.label_titre.pack()
        self.cadreTitre.pack(pady=20)    

        #Nom
        self.label_nom = Label(self.cadre, text=" Nom :" ,width=20,font=("bold", 10))
        self.label_nom.grid(row=1,column=0)
        self.input_nom = Entry(self.cadre) 
        nom = requete["Nom"]
        self.input_nom.insert(0,nom)
        self.input_nom.grid(row=1,column=1)

        #Prenom
        self.label_prenom = Label(self.cadre, text=" Prenom :",width=20,font=("bold", 10))
        self.label_prenom.grid(row=2,column=0)
        self.input_prenom = Entry(self.cadre)
        prenom = requete["Prenom"]
        self.input_prenom.insert(0,prenom)
        self.input_prenom.grid(row=2,column=1)

        #Date Naissance
        self.label_ddn = Label(self.cadre, text=" Date Naissance :",width=20,font=("bold", 10))
        self.label_ddn.grid(row=3,column=0)
        self.input_ddn = DateEntry(self.cadre,width=18)
        self.input_ddn.delete(0,'end')
        date = requete["Date-naissance"]
        self.input_ddn.insert(0,date)
        self.input_ddn.grid(row=3,column=1) 
        #self.bulle_ddn.bind(self.input_ddn,"Format : jj/dd/aaaa")

        #Numero Telephone
        self.label_nt= Label(self.cadre, text=" Numero Telephone :",width=20,font=("bold", 10))
        self.label_nt.grid(row=6,column=0)
        self.input_nt = Entry(self.cadre)
        numeroT = requete["Numero-tele"]
        self.input_nt.insert(0,numeroT)
        self.input_nt.grid(row=6,column=1)
        #self.bulle_numerot.bind(self.input_nt,"Format : 06xxxxxxxx")

        
        #Adresse
        self.label_add= Label(self.cadre, text=" Adresse :",width=20,font=("bold", 10))
        self.label_add.grid(row=7,column=0)
        self.input_add = Entry(self.cadre)
        adresse = requete["Adresse"]
        self.input_add.insert(0,adresse)
        self.input_add.grid(row=7,column=1)

        #Pseudo
        self.label_pseudo= Label(self.cadre, text=" Pseudo :",width=20,font=("bold", 10))
        self.label_pseudo.grid(row=10,column=0)
        self.input_pseudo = Entry(self.cadre)
        pseudo = requete["Login"]
        self.input_pseudo.insert(0,pseudo)
        self.input_pseudo.grid(row=10,column=1)
        
        #Mot de Pass  
        self.label_mdp= Label(self.cadre, text=" Mot De Passe :",width=20,font=("bold", 10))
        self.label_mdp.grid(row=11,column=0)
        self.input_mdp = Entry(self.cadre)
        password = requete["Password"]
        self.input_mdp.insert(0,password)
        self.input_mdp.grid(row=11,column=1) 


        #Boutton Pour Envoyer    
        self.boutonC = Button(self.cadrebouton2, text='Modifier',width=20,bg='brown',fg='white',command=self.modifierSession)
        self.boutonC.grid(row=14,column=0)
        
        #Boutton Pour Annulation    
        self.boutonA = Button(self.cadrebouton2, text='Annuler',width=20,bg='brown',fg='white',command=self.annuler)
        self.boutonA.grid(row=14,column=1,padx=5)
        
        self.cadre.pack()
        self.cadrebouton2.pack(pady=20)
        self.cadrevide = False

    def Supprimer(self): 

        if  self.cadrevide==False: 
            self.cadre.destroy()
            self.cadreTitre.destroy()
            self.cadrebouton2.destroy()
            self.cadre = Frame(self.fenetre)
            self.cadreTitre = Frame(self.fenetre)
            self.cadrebouton2 = Frame(self.fenetre)
            self.cadrevide=True
        
        self.label_titre = Label(self.cadreTitre, text="Supprimer Un Compte  ",width=20,font=("bold", 20))
        self.label_titre.pack()
        self.cadreTitre.pack(pady=20)

        self.label_numeroCompte = Label(self.cadre,text=" Numero Compte : ")
        self.champ_numeroCompte = Entry(self.cadre)
        self.label_sessioncompte = Label(self.cadre, text=" Session :",width=20,font=("bold", 10))
        self.vs = StringVar()
        self.radiomedecin = Radiobutton(self.cadre, text="Medecin",padx = 5,variable= self.vs , value = "M")       
        self.radioseceretaire = Radiobutton(self.cadre, text="Secretaire",padx = 20,variable= self.vs , value = "S")
        self.label_numeroCompte.grid(row=0,column=0)
        self.champ_numeroCompte.grid(row=0,column=1)
        self.label_sessioncompte.grid(row=1,column=0)
        self.radiomedecin.grid(row=1,column=1)
        self.radioseceretaire.grid(row=2,column=1)
        self.boutonSupprimer = Button(self.cadre,text="Supprimer",width=20,bg='brown',fg='white',command=self.supprimerCompte)
        self.boutonSupprimer.grid(row=3,column=1)
        self.cadre.configure(pady=30)
        self.cadre.pack()
        self.cadrevide = False
          
    

    def valider(self):   
        #Cette Fonction sert a verifier la validite des champs entree et si l'utilisateur a entre tous les champs
        #Recuperation des champs saisie    
        numeroT = self.input_nt.get()  
        pseudo = self.input_pseudo.get() 
        typesession = self.valeursession.get() 
        nom = self.input_nom.get() 
        prenom = self.input_prenom.get()
        ddn = Fonction_Affichage_RDV.convertisseurDate(self.input_ddn.get()) 
        mdp = self.input_mdp.get() 
        sexe = self.valeursexe.get() 
        addr = self.input_add.get()
        # test pour verifier les deux champs de nom et prenom
        test_nom_prenom = (any( char.isdigit() for char in nom)) or (any( char.isdigit() for char in prenom)) or (nom == '' or prenom == '' )
        # test  pour verifier l'egalite des champs mdp et confirmation mdp 
        test_mdp = mdp != self.input_cmdp.get() or ( len(mdp)==0 or  len(self.input_cmdp.get()) == 0)  
        #  test pour verifier la syntaxe de champ numero telephone
        test_numerot = Fenetre_inscription.testNumero(numeroT)  
        # test pour verifier la validite du champ date de naissance on fais appel a la fonction testDate
        test_ddn =  not (Fenetre_inscription.testDate(ddn,18))   
        # test pour verifier la validite du champ pseudo
        test_pseudo = len(pseudo) == 0  or pseudo[:1].isdigit() or len(pseudo) > 15   
        # ces tests pour verifier est-ce que la combinaison du pseudo mot de passe est deja dans la Database
        test_pseudo_medecin = CreationDB.collectionMedecin.find_one({"$and":[{"Login":pseudo},{"Password":mdp}]},{})
        test_pseudo_secretaire = CreationDB.collectionSecretaire.find_one({"$and":[{"Login":pseudo},{"Password":mdp}]},{}) 
        test_pseudo_mdp =  bool(test_pseudo_medecin) or bool(test_pseudo_secretaire)
        # test pour verifier le champ d adresse 
        test_adresse = len(addr)==0  
        # test pour verifier le champ de sexe 
        test_sexe = sexe == '' 
        # test pour verifier le champ type de session 
        test_type =  typesession== ''

        if   test_nom_prenom or test_mdp or  test_numerot or test_ddn or test_pseudo or test_adresse or test_sexe or test_type: 
           
            messagebox.showerror("Error", "Veuillez bien remplir les champs !!")  

        elif  test_pseudo_mdp == True : 

            messagebox.showerror("Error", " La combinaison du Login et password deja utilise")

        else: 

            if typesession == "M": 
                id = Fonction_Affichage_RDV.GenererID("Medecin")
                requete = {"NumMed":id,"Login":pseudo,"Password":mdp,"Nom":nom,"Prenom":prenom,"Date-naissance":ddn,"Numero-tele":numeroT,"Sexe":sexe,"Adresse":addr}
                testInsertion = CreationDB.collectionMedecin.insert_one(requete) 
            else:
                id = Fonction_Affichage_RDV.GenererID("Secretaire")
                requete = {"NumSecretaire":id,"Login":pseudo,"Password":mdp,"Nom":nom,"Prenom":prenom,"Date-naissance":ddn,"Numero-tele":numeroT,"Sexe":sexe,"Adresse":addr}
                testInsertion = CreationDB.collectionSecretaire.insert_one(requete)


            if testInsertion: 

             
                messagebox.showinfo("Confirmation d'ajout","Votre compte est bien ajoutee avec le numero "+str(id))
                self.input_nom.delete(0,'end')
                self.input_prenom.delete(0,'end')
                self.input_add.delete(0,'end')
                self.input_add.delete(0,'end')
                self.input_mdp.delete(0,'end')
                self.input_cmdp.delete(0,'end')
                self.input_nt.delete(0,'end')
                self.input_pseudo.delete(0,'end')
                self.input_ddn.delete(0,'end')

            else:

                print("Probleme lors de l'ajoute ")

    def annuler(self):

        self.fenetre.destroy() 
        Fenetre_Login.FenetreLogin().fenetre 

    def supprimerCompte(self):

        chainenumeroCompte = self.champ_numeroCompte.get()
        testChampNumero = chainenumeroCompte.isdigit() and len(chainenumeroCompte)!=0 
        typesession = self.vs.get()
        testsession = len(typesession) !=0 or typesession !=""
        numeroCompte = int(chainenumeroCompte)
        if testChampNumero and testsession:
            reponserequete = None
            if typesession == "M":
                reponserequete = CreationDB.collectionMedecin.delete_one({"NumMed":numeroCompte})
            else:
                reponserequete = CreationDB.collectionSecretaire.delete_one({"NumSecretaire":numeroCompte})

            if reponserequete:
                messagebox.showinfo("Confirmation","Le Compte Est Supprimer")
            else:
                messagebox.showerror("Erreur","Erreur Lors De La Suppresion")    
        else:
             messagebox.showerror("Erreur","Donnee mal")   


        
    @staticmethod
    def testDate(date,agemin):
        
            jour = int(date[8:])
            mois = int(date[5:7])
            annee = int(date[:4]) 

           
            nvdate = datetime(annee,mois,jour).strftime('%Y-%m-%d')
            # pour verifier que au moins la personne a 18 ans 
            dateactuel = (datetime.now() - timedelta(365*agemin)).strftime('%Y-%m-%d')
              
            if dateactuel > nvdate: 
                return 1 
            else:
                return 0

           

    @staticmethod
    def testNumero(tele):
        return  not ( tele.isdigit() and len(tele) == 10 and tele[:1] == '0')

          




if __name__ == '__main__':   

    f = Fenetre_inscription()
    f.fenetre.mainloop() 

    

