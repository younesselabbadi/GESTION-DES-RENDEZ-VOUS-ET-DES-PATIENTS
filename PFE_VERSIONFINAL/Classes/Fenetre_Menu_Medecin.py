from Lien_DB import CreationDB
from tkinter import Tk,Label,Button,font,messagebox,Frame 
from tkinter.font import Font
from tkinter import PhotoImage
import Fenetre_Login,Fenetre_Affichage_Dossier_Patient
import Fenetre_Consultation_Rapport,Fenetre_Creation_Certificat,Fenetre_Modifier_Dossier_Patient
import Fenetre_Creation_Rapport,Fenetre_Creation_Certificat,Fenetre_Affichage_RDV_Medecin,Fenetre_Cloturer_Soins

class Fenetre_Menu_Medecin(): 

    def __init__(self):  
        #initialisation de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("Fenetre Menu Medecin")
        self.fenetre.iconbitmap("Classes\\IHM\\logo.ico")
        self.fenetre.state("zoomed")
        self.fenetre.resizable(width=False,height=False)
        self.largeur = self.fenetre.winfo_screenwidth()
        self.hauteur = self.fenetre.winfo_screenheight()
        self.cadre = Frame(self.fenetre)
       
        self.cadre.grid(row=0,column=0,padx=7,pady=(self.hauteur//7))
        
        color = '#388ce4'
        font = Font(weight='bold',size=14)
        #Bouton pour rediger un rappot
        #self.bouton_rdv = Button(self.cadre, text='Rediger Un Rapport',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Creation_Rapport.Fenetre_Creation_Rappot)
        #self.bouton_rdv.grid(row=1,column=1,padx=3,pady=3)

        #Bouton pour cloturer un soin
        self.bouton_emp_med = Button(self.cadre, text='Cloture Un Soin',width=(self.largeur//37),height=11,bg=color,fg='white',font=font,bd=3,command=Fenetre_Cloturer_Soins.Fenetre_Cloturer_Soins)
        self.bouton_emp_med.grid(row=1,column=1,padx=3,pady=3)

        #Bouton pour consulter les dossiers
        self.bouton_emp_jou = Button(self.cadre, text='Consulter Les Dossiers \n des Patients',width=(self.largeur//37),height=11,bg=color,fg='white',font=font,bd=3,command=lambda :Fenetre_Affichage_Dossier_Patient.Fenetre_Affichage_Dossier_Patient(True))
        self.bouton_emp_jou.grid(row=1,column=2,padx=3,pady=3)

        #Bouton pour consulter les rapports
        #self.bouton_info_soins = Button(self.cadre, text='Consultation Des Rapports',width=(self.largeur//50),height=10,bg=color,fg='white',font=font,bd=3,command=Fenetre_Consultation_Rapport.Fenetre_Consultation_Rapport)
        #self.bouton_info_soins.grid(row=1,column=4,padx=3,pady=3) 

        #Bouton pour consulter ses rdv
        self.bouton_cons_doss = Button(self.cadre, text='Emplois  Des RDVs',width=(self.largeur//37),height=11,bg=color,fg='white',font=font,bd=3,command=Fenetre_Affichage_RDV_Medecin.Fenetre_Affichage_RDV_Medecin)
        self.bouton_cons_doss.grid(row=1,column=3,padx=3,pady=3)
        
            
        #Bouton pour Editer les informations d'un patient
        self.bouton_editer_information = Button(self.cadre, text='Editer les informations',width=(self.largeur//37),height=11,bg=color,fg='white',font=font,bd=3,command=Fenetre_Modifier_Dossier_Patient.Fenetre_Modifier_Dossier_Patient)
        self.bouton_editer_information.grid(row=2,column=1,padx=3,pady=3)
        
        #Bouton Certificat Medical
        self.bouton_certificat_medical = Button(self.cadre, text='Certfificat Medical',width=(self.largeur//37),height=11,bg=color,fg='white',font=font,bd=3,command=Fenetre_Creation_Certificat.Fenetre_Creation_Certificat)
        self.bouton_certificat_medical.grid(row=2,column=2,padx=3,pady=3)
        
        #Bouton Logout
        self.bouton_exit = Button(self.cadre, text='Quitter',width=(self.largeur//37),height=11,bg='brown',fg='white',font=font,bd=3,command=self.quitter)
        self.bouton_exit.grid(row=2,column=3,padx=3,pady=3)

        
       

        self.fenetre.mainloop()
    def quitter(self): 
        
        self.fenetre.destroy()
        f = Fenetre_Login.FenetreLogin()
        f.fenetre
        


if __name__ == '__main__':   

    f = Fenetre_Menu_Medecin()
    f.fenetre.mainloop()     