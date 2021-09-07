
from tkinter import Tk,Button,Frame,Label,Entry,ttk,messagebox,ttk
from tkinter.font import Font 
from tkcalendar  import DateEntry
from datetime import datetime
import re,time
from Lien_DB import CreationDB
import Fenetre_Ajouter_Patient 
import Fonction_Affichage_RDV  

class Fenetre_Gerer_RDV(): 

    def __init__(self):  

        #initialisation de la fenetre
        self.cadrevide = True
        self.fenetre = Tk()
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        self.fenetre.title("Editer RDVs: ")
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.fenetre.resizable(width=False, height=False)
        self.cadre = Frame(self.fenetre)  
        self.cadre.pack(pady=10)
        self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid')
        color = '#388ce4'
        font = Font(weight='bold',size=14)
        
        #Bouton pour Ajouter
        self.bouton_ajout_rdv = Button(self.cadre, text='Ajouter',bg=color,fg='white',font=font,bd=3,command=self.ajouter)
        self.bouton_ajout_rdv.grid(row=1,column=1,padx=3,pady=3)

        #Bouton pour Modifier
        self.bouton_modifier_rdv = Button(self.cadre, text='Modifier',bg=color,fg='white',font=font,bd=3,command=self.modifier)
        self.bouton_modifier_rdv.grid(row=1,column=2,padx=3,pady=3)

        #Bouton pour Supprimer
        self.bouton_supprimer_rdv = Button(self.cadre, text='Supprimer',bg=color,fg='white',font=font,bd=3,command=self.Supprimer)
        self.bouton_supprimer_rdv.grid(row=1,column=3,padx=3,pady=3)    

        self.cadreTitre = Frame(self.fenetre)
        self.fenetre.mainloop() 
        


    def ajouter(self):
        
        if  self.cadrevide==False: 
            self.cadreTab.destroy()
            self.cadreTitre.destroy()
            self.cadreTitre = Frame(self.fenetre)
            self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid')    
            self.cadrevide=True

        self.titre = Label(self.cadreTitre,text="Creation ",width=20,font=("bold", 20)) 
        self.titre.pack()
        self.Affichage_gerer_RDV(self.cadreTab)
        self.champ_numero_RDV.configure(state='readonly')
        self.bouton_Ajouter =Button(self.cadreTab,width=10,height=1,text="Confirmer",bg='brown',command=self.ajouterRDV)   
        self.bouton_Ajouter.grid(row=14,column=3,pady=5)
        self.bouton_Annuler =Button(self.cadreTab,width=10,height=1,text="Annuler",bg='brown')
        self.bouton_Annuler.grid(row=14,column=5)
        self.cadreTitre.pack(pady=20,padx=20)
        self.cadreTab.pack(pady=3)
        self.cadrevide=False
        



    def modifier(self):
        if  self.cadrevide==False: 
            self.cadreTab.destroy()
            self.cadreTitre.destroy()
            self.cadreTitre = Frame(self.fenetre)
            self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid')
            self.cadrevide=True

        self.titre = Label(self.cadreTitre,text="Modification ",width=20,font=("bold", 20)) 
        self.titre.pack()
        self.Affichage_gerer_RDV(self.cadreTab)
        self.champ_numero_Patient.configure(state='readonly')
        self.champ_list_Medecin.configure(state='disabled')
        self.champ_heure_RDV.configure(state='readonly')
        self.champ_date_RDV.delete(0,'end')
        self.champ_date_RDV.configure(state='disabled')
        self.champ_Motif.configure(state='disabled')
        self.bouton_recherche =Button(self.cadreTab,width=10,height=1,text="Recherche",bg='brown',command=self.rechercheRDV)   
        self.bouton_recherche.grid(row=14,column=5,pady=5) 
        self.cadreTitre.pack(pady=20,padx=20)
        self.cadreTab.pack(pady=3)
        self.cadrevide=False

    def Supprimer(self):
        if  self.cadrevide==False: 
            self.cadreTab.destroy()
            self.cadreTitre.destroy()
            self.cadreTitre = Frame(self.fenetre)
            self.cadreTab =Frame(self.fenetre, borderwidth=1,relief='solid')
            self.cadrevide=True

        self.titre = Label(self.cadreTitre,text="Suppression",width=20,font=("bold", 20 )) 
        self.titre.pack()
        self.label_numero_RDV_supprimer = Label(self.cadreTab,text="Numero  RDV:") 
        self.champ_numero_RDV_supprimer = Entry(self.cadreTab)    
        self.label_numero_RDV_supprimer.grid(row=1,column=2,columnspan=2,rowspan=2)
        self.champ_numero_RDV_supprimer.grid(row=1,column=4,columnspan=4,rowspan=2)

        self.label_numero_patient_supprimer = Label(self.cadreTab,text="Numero  Patient:") 
        self.champ_numero_patient_supprimer = Entry(self.cadreTab)    
        self.label_numero_patient_supprimer.grid(row=3,column=2,columnspan=2,rowspan=2)
        self.champ_numero_patient_supprimer.grid(row=3,column=4,columnspan=4,rowspan=2)

        self.label_numero_medecin_supprimer = Label(self.cadreTab,text="Medecin:") 
        listmed = Fenetre_Gerer_RDV.listeMedecin()   
        self.champ_list_medecin_supprimer = ttk.Combobox(self.cadreTab,values=listmed,width=17)   
        self.label_numero_medecin_supprimer.grid(row=5,column=2,columnspan=2,rowspan=2)
        self.champ_list_medecin_supprimer.grid(row=5,column=4,columnspan=4,rowspan=2)

        self.bouton_Valider =Button(self.cadreTab,width=10,height=1,text="Valider",bg='brown',command=self.supprimer)
        self.bouton_Valider.grid(row=7,column=2,pady=5,padx=35)
        self.bouton_Annuler =Button(self.cadreTab,width=10,height=1,text="Annuler",bg='brown')
        self.bouton_Annuler.grid(row=7,column=4)
        self.cadreTitre.pack(pady=20,padx=20)
        self.cadreTab.pack(pady=3)
        self.cadrevide=False

    def Affichage_gerer_RDV(self,cadreTab):

       

        self.label_numero_RDV = Label(cadreTab,text="Numero  RDV:") 
        self.champ_numero_RDV = Entry(cadreTab)
        
        listmed = Fenetre_Gerer_RDV.listeMedecin()
        self.label_numero_Medecin = Label(cadreTab,text=" Medecin :") 
        self.champ_list_Medecin = ttk.Combobox(cadreTab,values=listmed,width=17)    

        self.label_numero_Patient = Label(cadreTab,text="Numero Patient :") 
        self.champ_numero_Patient= Entry(cadreTab)

        self.label_date_RDV = Label(cadreTab,text=" Date RDV:")  
        self.champ_date_RDV = DateEntry(cadreTab,width=18) 

        #self.bulle_date.bind(self.champ_date_RDV,"Format : jj / mm / aaaa")
        
        self.label_heure_RDV = Label(cadreTab,text="Heure:") 
        self.champ_heure_RDV = Entry(cadreTab) 

        #self.bulle_heure.bind(self.champ_heure_RDV,"Format : hh : mm")
        
        listsoin = Fenetre_Gerer_RDV.listeSoin()
        self.label_Motif = Label(cadreTab,text="Soin :") 
        self.champ_Motif = ttk.Combobox(cadreTab,values=listsoin,width=17)
              
        
            
        self.label_numero_RDV.grid(row=2,column=2,columnspan=2,rowspan=2)
        self.champ_numero_RDV.grid(row=2,column=4,columnspan=4,rowspan=2)
        
        self.label_numero_Medecin.grid(row =4 , column= 2,columnspan=2,rowspan=2) 
        self.champ_list_Medecin.grid(row=4 ,column = 4,columnspan=4,rowspan=2)
        
        self.label_numero_Patient.grid(row=6,column =2,columnspan=2,rowspan=2)
        self.champ_numero_Patient.grid(row=6,column=4,columnspan=4,rowspan=2)
        
        self.label_date_RDV.grid(row=8,column=2,columnspan=2,rowspan=2)
        
        self.champ_date_RDV.grid(row=8,column=4,columnspan=2,rowspan=2)
        
        self.label_heure_RDV.grid(row=10,column=2,columnspan=2,rowspan=2)
        self.champ_heure_RDV.grid(row=10,column=4,columnspan=4,rowspan=2)
        
        self.label_Motif.grid(row=12,column=2,columnspan=2,rowspan=2)
        self.champ_Motif.grid(row=12,column=4,columnspan=4,rowspan=2)
  
    
    def ajouterRDV(self): 
       
        numeroPatient = self.champ_numero_Patient.get()
        if  numeroPatient != "" and numeroPatient.isdigit():

            reponse = CreationDB.collectionPatient.find_one({"NumPat":int(numeroPatient)},{"_id":0}) 

            if reponse == None:
                messagebox.showerror("Error", "patient introuvable Veuillez ajouter le patient")
                Fenetre_Ajouter_Patient.Fenetre_Ajouter_Patient().fenetre.mainloop()

            nomMedecin = self.champ_list_Medecin.get()[3:]
            date = Fonction_Affichage_RDV.convertisseurDate(self.champ_date_RDV.get())
            heure = self.champ_heure_RDV.get() 
            motif = self.champ_Motif.get()
            
            testChamp = self.verification(date,heure,motif)
            
            numeroMedecin = CreationDB.collectionMedecin.find_one({"Nom":nomMedecin},{"_id":0})["NumMed"]

            if not(Fenetre_Gerer_RDV.estDispo(heure,date,numeroMedecin)):
                messagebox.showerror("Erreur","La date est deja occupe")
            else:
                if testChamp :
                    numRDV  = Fonction_Affichage_RDV.GenererID("RDV")
                    reponsePatient = CreationDB.collectionPatient.update_one(
                                                                            {"NumPat":int(numeroPatient)},
                                                                            {"$push":
                                                                            {"RDV":
                                                                            {"NumRDV":numRDV,
                                                                            "NumPatient":int(numeroPatient),
                                                                            "NumMed":numeroMedecin,
                                                                            "Motif":motif,
                                                                            "Date":date,
                                                                            "Heure":heure
                                                                            }
                                                                            }
                                                                            }
                                                                            ) 
                    reponseMedecin = CreationDB.collectionMedecin.update_one(
                                                                            {"NumMed":int(numeroMedecin)},
                                                                            {"$push":
                                                                            {"RDV":
                                                                            {"NumRDV":numRDV,
                                                                            "NumPatient":int(numeroPatient),
                                                                            "NumMed":numeroMedecin,
                                                                            "Motif":motif,
                                                                            "Date":date,
                                                                            "Heure":heure
                                                                            }
                                                                            }
                                                                            }
                                                                            )
                    reponseRDV = CreationDB.collectionRDV.insert_one(
                                                                    {"NumRDV":numRDV,
                                                                    "NumPatient":int(numeroPatient),
                                                                    "NumMed":int(numeroMedecin),
                                                                    "Motif":motif,
                                                                    "Date":date,
                                                                    "Heure":heure
                                                                    }
                                                                    ) 
                    if not(reponsePatient) or not(reponseMedecin) or not(reponseRDV) :
                        messagebox.showerror("Erreur", "Erreur lors de l'ajout\n Veuillez ressayer")
                    else:
                        messagebox.showinfo("Confirmation","Le Rendez-vous est bien ajoutee")   
        else:
            messagebox.showerror("Champ Numero Patient est errone","Veuillez bien remplir le champ numero de patient")            

        
    def rechercheRDV(self):
        numeroRDV = int(self.champ_numero_RDV.get())
        reponserequete = CreationDB.collectionRDV.find_one({"NumRDV":numeroRDV},{"_id":0})
        if not(reponserequete):
             messagebox.showerror("Erreur", "Non RDV avec le numero "+str(numeroRDV))    
        else:
            self.champ_numero_RDV.configure(state='readonly')
            self.champ_numero_Patient.configure(state='normal')
            self.champ_numero_Patient.insert(0,reponserequete['NumPatient'])
            self.champ_list_Medecin.configure(state='normal')
            numeromedecin = reponserequete['NumMed']
            rep = CreationDB.collectionMedecin.find_one({"NumMed":numeromedecin},{"_id":0})
            nom = rep['Nom']
            self.champ_list_Medecin.insert(0,"Dr:"+nom)
            self.champ_heure_RDV.configure(state='normal')
            self.champ_heure_RDV.insert(0,reponserequete['Heure'])
            self.champ_date_RDV.configure(state='normal')
            self.champ_date_RDV.insert(0,reponserequete['Date'])
            self.champ_Motif.configure(state='normal')
            self.champ_Motif.insert(0,reponserequete['Motif'])
            self.bouton_modifier = Button(self.cadreTab,width=10,height=1,text="Valider",bg='brown',command=self.modifierRDV) 
            self.bouton_modifier.grid(row=14,column=5,pady=5)

        

    def modifierRDV(self):

        numeroRDV = int(self.champ_numero_RDV.get())
        numeroPatient = int(self.champ_numero_Patient.get())
        nomMedecin = self.champ_list_Medecin.get()[3:]
        heure = self.champ_heure_RDV.get()
        date = Fonction_Affichage_RDV.convertisseurDate(self.champ_date_RDV.get())
        motif = self.champ_Motif.get()
        test = self.verification(date,heure,motif)
        numeroMedecin = CreationDB.collectionMedecin.find_one({"Nom":nomMedecin},{"_id":0})["NumMed"]
        reponse = CreationDB.collectionPatient.find_one({"NumPat":numeroPatient},{"id":0})

        if not(reponse) or not(test):

            messagebox.showerror("Erreur","Veulliez bien remplir les champs")

        else:

            if Fenetre_Gerer_RDV.estDispoModif(heure,date,numeroMedecin) and Fenetre_Gerer_RDV.testDate(date,heure):
                
                reponseMedecin = CreationDB.collectionMedecin.update_one(
                                                                        {"NumMed":numeroMedecin,"RDV.NumRDV":numeroRDV},
                                                                        {"$set":{"RDV.$.NumRDV":numeroRDV,"RDV.$.NumMed":numeroMedecin,"RDV.$.NumPatient":numeroPatient,"RDV.$.Date":date,"RDV.$.Heure":heure,"RDV.$.Motif":motif}}
                                                                        )
                reponsePatient = CreationDB.collectionPatient.update_one(
                                                                        {"NumPat":numeroPatient,"RDV.NumRDV":numeroRDV},
                                                                        {"$set":{"RDV.$.NumRDV":numeroRDV,"RDV.$.NumMed":numeroMedecin,"RDV.$.NumPatient":numeroPatient,"RDV.$.Date":date,"RDV.$.Heure":heure,"RDV.$.Motif":motif}}
                                                                        )                                                                      
                reponseRDV = CreationDB.collectionRDV.update_one({"NumRDV":numeroRDV},{"$set":{"NumMed":numeroMedecin,"NumPatient":numeroPatient,"Date":date,"Heure":heure,"Motif":motif}})     

                if reponseMedecin and reponseRDV and reponsePatient:
                    messagebox.showinfo(" Mise a Jour Avec Succes ","La Modification Est Faite")
            else:
                messagebox.showerror("Erreur","Horaire occupe")

    def supprimer(self):

        numeroRDV = self.champ_numero_RDV_supprimer.get()
        numeroPatient = self.champ_numero_patient_supprimer.get()
        nommedecin = self.champ_list_medecin_supprimer.get()[3:]
        reponse = CreationDB.collectionMedecin.find_one({"Nom":nommedecin},{"_id":0})
        
        if numeroRDV.isdigit() and len(numeroRDV) != 0 and numeroPatient.isdigit() and len(numeroPatient) != 0 and len(nommedecin) != 0 :
            idRDV = int(numeroRDV)
            idmedecin = reponse["NumMed"]
            idpatient = int(numeroPatient)
            reponseRDV = CreationDB.collectionRDV.remove({"NumRDV":idRDV}) 
            reponseMedecin = CreationDB.collectionMedecin.update_one(
                                                                {"NumMed":idmedecin,"RDV.NumRDV":idRDV},
                                                                {"$unset":
                                                                {"RDV.$":1  
                                                                }
                                                                },False,True
                                                                )

            # Pour enlever les valeurs null qui reste quand on supprimer un champs dans la BD    
                                                            
            CreationDB.collectionMedecin.update({"NumMed":idmedecin},{'$pull':{"RDV":None}},True)
            reponsePatient = CreationDB.collectionPatient.update_one(
                                                                {"NumPat":idpatient,"RDV.NumRDV":idRDV},
                                                                {"$unset":
                                                                {"RDV.$":1
                                                                }
                                                                },False,True
                                                                )  
            CreationDB.collectionPatient.update({"NumPat":idpatient},{'$pull':{"RDV":None}},True)                                                    
            if reponseRDV and reponseMedecin and reponsePatient:
                messagebox.showinfo("La supression est faite avec succes","Le rendez vous numero : "+str(idRDV)+" est Supprimee ") 
            else: 
                messagebox.showerror("Erreur lors de la supression ","Ressayer plus tard ")

    def verification(self,date,heure,motif):
           
        testD = Fenetre_Gerer_RDV.testDate(date,heure)
        testH = Fenetre_Gerer_RDV.testHeure(heure) 

        if (not motif):
            messagebox.showerror("Error","Veuillez choisir un motif") 
            return False
        if (not testD):
            messagebox.showerror("Error","Date invalide")  
            return False
        if (not testH):
            messagebox.showerror("Error","Heure Invalide")  
            return False                   
        return True

    
    @staticmethod
    def testHeure(heure):
        try:
            time.strptime(heure,'%H:%M')      
            return True 
        except ValueError:
            return False

    @staticmethod
    def testDate(date,heure):

       

            jour = int(date[8:])
            mois = int(date[5:7])
            annee = int(date[:4]) 

          
            nvdate = datetime(annee,mois,jour).strftime('%Y-%m-%d')
               # pour verifier que la secretaire ne donne pas une date dans le passe
            dateactuel = datetime.now().strftime('%Y-%m-%d')

            if dateactuel < nvdate : 
                return 1 

            elif dateactuel == nvdate:
                    
                if Fenetre_Gerer_RDV.testHeure(heure):
                    
                    heureactuel = time.strftime('%H:%M')
                      
                    if heure > heureactuel:
                        return 1
                    else:
                        return 0
                else:
                   return 0



    @staticmethod
    def estDispo(heure,date,numeroMedecin):

        reponserequete = CreationDB.collectionRDV.find_one({"$and":[{"Heure":heure ,"Date":date,"NumMed":numeroMedecin}]})
        if reponserequete:
            return False
        else:
            return True
    @staticmethod
    def estDispoModif(heure,date,numeroMedecin):
        reponse = CreationDB.collectionRDV.find_one({"Heure":heure},{"_id":0})
        if reponse:
            if heure == reponse["Heure"]:
                return True
            else:
                reponserequete = CreationDB.collectionRDV.find_one({"$and":[{"Heure":heure ,"Date":date,"NumMed":numeroMedecin}]})
                if reponserequete:
                    return False
        else:
            return True
    @staticmethod
    def listeMedecin(): 
        listMedecin = list()
        reponserequete = CreationDB.collectionMedecin.find()
        if reponserequete:
            for medecin in reponserequete:
                # besh n enregistre le rapport b numero de medecin hanb9a nakhed mn position 2 tal lkher o ncherchi 3liha f bd 
                listMedecin.append("Dr."+medecin["Nom"])
            return listMedecin
        else: 
            messagebox.showerror("Erreur ","Veuillez ressayer plus tard !!")

    @staticmethod
    def listeSoin(): 
        listSoin = list()
        reponserequete = CreationDB.collectionSoin.find()
        if reponserequete:
            for soin in reponserequete:
                # besh n enregistre le rapport b numero de medecin hanb9a nakhed mn position 2 tal lkher o ncherchi 3liha f bd 
                listSoin.append(soin["Nom"])
            return listSoin
        else: 
            messagebox.showerror("Erreur ","Veuillez ressayer plus tard !!")






        
if __name__ == '__main__':   

        f =Fenetre_Gerer_RDV()
        f.fenetre.mainloop()  
       
      
    
       
       
      