from Lien_DB import CreationDB
from tkinter import Tk,Label,Button,font,messagebox,Frame 
import Fenetre_Login,Fenetre_TypesSoins,Fenetre_Affichage_RDV_Journee,Fenetre_Affichage_Dossier_Patient,Fenetre_Affichage_RDV_Medecin
import Fenetre_Modifier_Dossier_Patient,Fenetre_Gerer_RDV,Fenetre_Consultation_Rapport,Fenetre_Ajouter_Patient
from tkinter.font import Font
from tkinter import PhotoImage



class Fenetre_Menu_Secretaire(): 

    def __init__(self):  

        #initialisation de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("Fenetre Menu Secrataire")
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        self.fenetre.state("zoomed")
        self.fenetre.resizable(width=False,height=False)
        self.largeur = self.fenetre.winfo_screenwidth()
        self.hauteur = self.fenetre.winfo_screenheight()
        self.cadre = Frame(self.fenetre)
       
        self.cadre.grid(row=0,column=0,padx=2,pady=(self.hauteur//6))
        
        color = '#388ce4'
        font = Font(weight='bold',size=14)

        #Bouton pour creer une RDV
        self.bouton_rdv = Button(self.cadre, text='Gestion des RDVs',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Gerer_RDV.Fenetre_Gerer_RDV)
        self.bouton_rdv.grid(row=1,column=1,padx=3,pady=3)

        #Bouton pour Aficher L'emploi du temps d'un Medecin
        self.bouton_emp_med = Button(self.cadre, text='Emploi Du Temps\n Des Medecines',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Affichage_RDV_Medecin.Fenetre_Affichage_RDV_Medecin)
        self.bouton_emp_med.grid(row=1,column=2,padx=3,pady=3)

        #Bouton pour afficher l'emploi de temp de la journee courante 
        self.bouton_emp_jou = Button(self.cadre, text='Emploi Du Temps De \nLa Journee',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command = Fenetre_Affichage_RDV_Journee.Fenetre_Affichage_RDV_Journee )
        self.bouton_emp_jou.grid(row=1,column=3,padx=3,pady=3)

        #Bouton pour afficher les informations sur un soin 
        self.bouton_info_soins = Button(self.cadre, text='Les Soins Disponibles ',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=self.appelSoin)
        self.bouton_info_soins.grid(row=1,column=4,padx=3,pady=3) 

        #Bouton pour consulter un dossier d'un patient 
        self.bouton_cons_doss = Button(self.cadre, text='Consulter les Dossiers des \n Patients',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=lambda : Fenetre_Affichage_Dossier_Patient.Fenetre_Affichage_Dossier_Patient(False))
        self.bouton_cons_doss.grid(row=2,column=1,padx=3,pady=3)
        
        #Bouton Consulter des rapports sans editer
        self.bouton_cons_rapp = Button(self.cadre, text='Ajouter Patient ',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Ajouter_Patient.Fenetre_Ajouter_Patient)
        self.bouton_cons_rapp.grid(row=2,column=3,padx=3,pady=3)
        
        #Bouton pour Editer les informations d'un patient 
        self.bouton_cons_rdv = Button(self.cadre, text='Modifier Un Dossier ',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Modifier_Dossier_Patient.Fenetre_Modifier_Dossier_Patient)
        self.bouton_cons_rdv.grid(row=2,column=2,padx=3,pady=3)
        
        #Bouton quitter
        self.bouton_quitter = Button(self.cadre, text='Quitter',width=(self.largeur//50),height=10,bg='brown',fg='white',font=font,bd=3,command=self.quitter)
        self.bouton_quitter.grid(row=2,column=4,padx=3,pady=3)
    
        self.fenetre.mainloop()
        
    def quitter(self): 
        
        self.fenetre.destroy()
        f = Fenetre_Login.FenetreLogin()
        f.fenetre
    def appelSoin(self):
         Fenetre_TypesSoins.Fenetre_TypesSoins().fenetre

 

if __name__ == '__main__':   

    f = Fenetre_Menu_Secretaire()
    f.fenetre.mainloop() 