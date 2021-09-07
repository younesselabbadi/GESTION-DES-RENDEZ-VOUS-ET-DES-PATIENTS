from tkinter import Label,Frame,Entry,ttk,messagebox,Button
from Lien_DB import CreationDB
import Fenetre_Creation_Rapport
from Fenetre_Consultation_Rapport import Fenetre_Consultation_Rapport
import pymongo
from operator import itemgetter as i 
from functools import cmp_to_key
import datetime,re





def Affichage_RDV_Medecin(cadreTab,reponserequete):
         
            
            color='#99ffff'
            label_Numero_RDV = Label(cadreTab, text="Numero RDV " ,width=20,font=("bold", 11),bg=color)
            label_Numero_Patient = Label(cadreTab, text=" N° Patient " ,width=20,font=("bold", 11),bg=color)
            label_Motif = Label(cadreTab, text=" Motif " ,width=20,font=("bold", 11),bg=color)
            label_Date = Label(cadreTab, text=" Date " ,width=20,font=("bold", 11),bg=color)
            label_Heure = Label(cadreTab, text=" Heure " ,width=20,font=("bold", 11),bg=color)
            label_Numero_RDV.grid(row=1,column=1)
            label_Numero_Patient.grid(row=1,column=2)
            label_Motif.grid(row=1,column=3)
            label_Date.grid(row=1,column=4)
            label_Heure.grid(row=1,column=5)
            ligne =2 

            listRdv = multikeysort(reponserequete['RDV'],['Date','Heure'])
            for RDV in listRdv :    
                
            
                champ_Numero_RDV = Entry(cadreTab)
                champ_Numero_RDV.grid(row=ligne,column=1)
                champ_Numero_RDV.insert(0,RDV['NumRDV'])
                champ_Numero_RDV.configure(state='readonly')

                champ_Numero_Patient = Entry(cadreTab)
                champ_Numero_Patient.grid(row=ligne,column=2)
                champ_Numero_Patient.insert(0,RDV['NumPatient'])
                champ_Numero_Patient.configure(state='readonly')

                champ_Motif = Entry(cadreTab)
                champ_Motif.grid(row=ligne,column=3)
                champ_Motif.insert(0,RDV['Motif'])
                champ_Motif.configure(state='readonly')

                champ_Date = Entry(cadreTab)
                champ_Date.grid(row=ligne,column=4)
                champ_Date.insert(0,RDV['Date'])
                champ_Date.configure(state='readonly')

                champ_Heure = Entry(cadreTab)
                champ_Heure.grid(row=ligne,column=5)
                champ_Heure.insert(0,RDV['Heure'])
                champ_Heure.configure(state='readonly')

                ligne = ligne + 1


def Affichage_RDV_Patient(cadreTab,reponserequete,numpatient,medecin):
         
            
            color='#99ffff'
            label_Numero_RDV = Label(cadreTab, text="Numero RDV " ,width=20,font=("bold", 11),bg=color)
            label_Numero_Medecin = Label(cadreTab, text=" N° Medecin " ,width=20,font=("bold", 11),bg=color)
            label_Motif = Label(cadreTab, text=" Motif " ,width=20,font=("bold", 11),bg=color)
            label_Date = Label(cadreTab, text=" Date " ,width=20,font=("bold", 11),bg=color)
            label_Heure = Label(cadreTab, text=" Heure " ,width=20,font=("bold", 11),bg=color)
            label_Numero_RDV.grid(row=1,column=1)
            label_Numero_Medecin.grid(row=1,column=2)
            label_Motif.grid(row=1,column=3)
            label_Date.grid(row=1,column=4)
            label_Heure.grid(row=1,column=5)
            ligne =2 
           

            
            listRdv = multikeysort(reponserequete['RDV'],['Date','Heure'])
            listboutonajouter = list()
            listboutonconsulter = list()
            indicebutton = 0
            for RDV in  listRdv:
                
            
                champ_Numero_RDV = Entry(cadreTab)
                champ_Numero_RDV.grid(row=ligne,column=1)
                champ_Numero_RDV.insert(0,RDV['NumRDV'])
                champ_Numero_RDV.configure(state='readonly')

                champ_Numero_Medecin = Entry(cadreTab)
                champ_Numero_Medecin.grid(row=ligne,column=2)
                champ_Numero_Medecin.insert(0,RDV['NumMed'])
                champ_Numero_Medecin.configure(state='readonly')

                champ_Motif = Entry(cadreTab)
                champ_Motif.grid(row=ligne,column=3)
                champ_Motif.insert(0,RDV['Motif'])
                champ_Motif.configure(state='readonly')

                champ_Date = Entry(cadreTab)
                champ_Date.grid(row=ligne,column=4)
                champ_Date.insert(0,RDV['Date'])
                champ_Date.configure(state='readonly')

                champ_Heure = Entry(cadreTab)
                champ_Heure.grid(row=ligne,column=5)
                champ_Heure.insert(0,RDV['Heure'])
                champ_Heure.configure(state='readonly') 
                if medecin:
                    listboutonajouter.append(Button(cadreTab,text="Ajouter un Rapport",padx=3,bg='brown',command=lambda numrdv=RDV['NumRDV'],numpat=numpatient,nummed=RDV['NumMed']: appelCreation(numrdv,numpat,nummed)))
                    listboutonajouter[indicebutton].grid(row=ligne,column=6)
                listboutonconsulter.append(Button(cadreTab,text="Consulter les rapports",bg='brown',command=lambda numrdv=RDV['NumRDV'],numpat=numpatient,nummed=RDV['NumMed']: appelConsultation(numrdv,numpat,nummed)))
                listboutonconsulter[indicebutton].grid(row=ligne,column=7)

                ligne = ligne + 1
                indicebutton = indicebutton + 1
def appelCreation(numrdv,numpatient,nummed): 
    
    Fenetre_Creation_Rapport.Fenetre_Creation_Rappot(numpatient,nummed,numrdv).fenetre.mainloop()

def appelConsultation(numrdv,numpatient,nummed): 
    
    Fenetre_Consultation_Rapport(numrdv,numpatient,nummed)





def Affichage_RDV_Journee(cadreTab,date_courante):
         
            
            color='#99ffff'
            label_Numero_RDV = Label(cadreTab, text="Numero RDV " ,width=20,font=("bold", 11),bg=color)
            label_Numero_Patient = Label(cadreTab, text=" N° Patient " ,width=20,font=("bold", 11),bg=color)
            label_Numero_Medecin = Label(cadreTab, text=" N° Medecin " ,width=20,font=("bold", 11),bg=color)
            label_Motif = Label(cadreTab, text=" Motif " ,width=20,font=("bold", 11),bg=color)
            label_Heure = Label(cadreTab, text=" Heure " ,width=20,font=("bold", 11),bg=color)
            label_Numero_RDV.grid(row=1,column=1)
            label_Numero_Patient.grid(row=1,column=2)
            label_Numero_Medecin.grid(row=1,column=3)
            label_Motif.grid(row=1,column=4)
            label_Heure.grid(row=1,column=5)
            
            reponserequete = CreationDB.collectionRDV.find({"Date":str(date_courante)},{"_id":0})
        
            if reponserequete == None  : 
                messagebox.showerror("Error", "Erreur lors de l'acces a la BD Resseayer plus tard")
            if  reponserequete.count() == 0 : 
                messagebox.showerror("Error", "Aucune Rendez-Vous Prevu Pour Cette Journee")   
        
            if reponserequete != None: 
                ligne =2 
               
                
                for RDV in multikeysort(reponserequete,['Date','Heure']):    
                    
                    
                    champ_Numero_RDV = Entry(cadreTab)
                    champ_Numero_RDV.grid(row=ligne,column=1)
                    champ_Numero_RDV.insert(0,RDV['NumRDV'])
                    champ_Numero_RDV.configure(state='readonly')

                    champ_Numero_Patient = Entry(cadreTab)
                    champ_Numero_Patient.grid(row=ligne,column=2)
                    champ_Numero_Patient.insert(0,RDV['NumPatient'])
                    champ_Numero_Patient.configure(state='readonly')

                    champ_Numero_Medecin = Entry(cadreTab)
                    champ_Numero_Medecin.grid(row=ligne,column=3)
                    champ_Numero_Medecin.insert(0,RDV['NumMed'])
                    champ_Numero_Medecin.configure(state='readonly')

                    champ_Motif = Entry(cadreTab)
                    champ_Motif.grid(row=ligne,column=4)
                    champ_Motif.insert(0,RDV['Motif'])
                    champ_Motif.configure(state='readonly')

                    champ_Heure = Entry(cadreTab)
                    champ_Heure.grid(row=ligne,column=5)
                    champ_Heure.insert(0,RDV['Heure'])
                    champ_Heure.configure(state='readonly')

                    ligne = ligne + 1


def GenererID(collection):  
    idGenere = False
    if collection == "Patient":
        reponse = CreationDB.collectionCompteur.find_one(
                                                        {"entite":
                                                        "Patient"},
                                                        {"_id":0
                                                        }
                                                        )  
        if reponse != None: 
            idGenere =  reponse['id_dispo']
            CreationDB.collectionCompteur.update(
                                                {"entite":"Patient"},
                                                {'$inc': 
                                                {'id_dispo': 1
                                                }
                                                }
                                                )
            
    if collection == "Medecin":
            reponse = CreationDB.collectionCompteur.find_one(
                                                            {"entite":
                                                            "Medecin"},
                                                            {"_id":0
                                                            }
                                                            )  
            if reponse != None: 
                CreationDB.collectionCompteur.update(
                                                    {'entite':"Medecin"
                                                    },
                                                    {'$inc':
                                                    {'id_dispo':1
                                                    }
                                                    }
                                                    )
                idGenere =  reponse['id_dispo']
    if collection == "RDV":
            reponse = CreationDB.collectionCompteur.find_one(
                                                            {"entite":"RDV"
                                                            },
                                                            {
                                                            "_id":0
                                                            }
                                                            )  
            if reponse != None: 
                CreationDB.collectionCompteur.update(
                                                    {'entite':"RDV"
                                                    },
                                                    {
                                                    '$inc':
                                                    {
                                                    'id_dispo': 1
                                                    }
                                                    }
                                                    )
                idGenere =  reponse['id_dispo']  
    if collection == "Secretaire":
            reponse = CreationDB.collectionCompteur.find_one(
                                                            {"entite":"Secretaire"
                                                            },
                                                            {
                                                            "_id":0
                                                            }
                                                            )  
            if reponse != None: 
                CreationDB.collectionCompteur.update(
                                                    {'entite':"Secretaire"
                                                    },
                                                    {
                                                    '$inc':
                                                    {
                                                    'id_dispo': 1
                                                    }
                                                    }
                                                    )
                idGenere =  reponse['id_dispo']  
    if collection == "Rapport":
            reponse = CreationDB.collectionCompteur.find_one(
                                                            {"entite":
                                                            "Rapport"
                                                            },
                                                            {
                                                            "_id":0
                                                            }
                                                            )  
            if reponse != None: 
                CreationDB.collectionCompteur.update(
                                                    {'entite':
                                                    "Rapport"},
                                                    {'$inc':
                                                    {
                                                    'id_dispo': 1
                                                    }
                                                    }
                                                    )
                idGenere =  reponse['id_dispo']                         
                
    return idGenere   



def multikeysort(items, columns):
    comparers = [
        ((i(col[1:].strip()), -1) if col.startswith('-') else (i(col.strip()), 1))
        for col in columns
    ]
    def comparer(left, right):
        comparer_iter = (
            cmp(fn(left), fn(right)) * mult
            for fn, mult in comparers
        )
        return next((result for result in comparer_iter if result), 0)
    return sorted(items, key=cmp_to_key(comparer))
               
def cmp(a,b):
    return (a > b) - (a < b)

def convertisseurDate(date):

    if re.compile("[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]").match(date):
         return date
    else: 
        return date[6:]+"-"+date[3:5]+"-"+date[:2]


if __name__ == "__main__":
   
        
    print(convertisseurDate("1998-01-20"))



