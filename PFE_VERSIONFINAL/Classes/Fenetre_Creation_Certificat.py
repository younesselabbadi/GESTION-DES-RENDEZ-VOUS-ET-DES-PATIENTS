from tkinter import Tk,Frame,Label,Entry,Button,Text,messagebox
import Fonction_Affichage_RDV,Fenetre_inscription
from reportlab.pdfgen import canvas 
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from textwrap import wrap
from  PyPDF2  import PdfFileReader,PdfFileWriter
from Lien_DB import CreationDB
import os
from tkcalendar import DateEntry


class Fenetre_Creation_Certificat():
    def __init__(self): 
        self.estvide = True
        self.fenetre = Tk()
        self.fenetre.title("Rediger une Certificat")
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.cadre=Frame(self.fenetre)
        
        self.cadre.pack()

        self.label_numero_patient = Label(self.cadre,text="Numero  Patient:") 
        self.champ_numero_patient = Entry(self.cadre)

        self.label_rdv= Label(self.cadre,text="Numero RDV") 
        self.champ_rdv = Entry(self.cadre)

        # self.label_numero_Seance = Label(self.cadre,text="Numero  de Seance:") 
        # self.champ_numero_Seance = Entry(self.cadre)
        
        self.label_date = Label(self.cadre,text="Date") 
        self.champ_date = DateEntry(self.cadre,width=18)
        self.champ_date.configure(state='disabled')
        
        self.label_Redaction_Rapport = Label(self.cadre, text="Certificat  :" ,width=20,font=("bold", 10))
        self.champ_Redaction_Rapport= Text(self.cadre,width=80,height=20)

        self.bouton_Ajouter =Button(self.cadre,width=10,height=1,text="Confirmer",bg='brown',command=self.envoyer)

        
        self.label_numero_patient.grid(row=1,column=2)
        self.champ_numero_patient.grid(row=2,column=2)
        #self.label_rdv.grid(row=3,column=2)
        #self.champ_rdv.grid(row=4,column=2) 
        # self.label_numero_Seance.grid(row=5,column=2)
        # self.champ_numero_Seance.grid(row=6,column=2)
        self.label_date.grid(row=3,column=2)
        self.champ_date.grid(row=4,column=2)
        self.label_Redaction_Rapport.grid(row=5,column=2)
        self.champ_Redaction_Rapport.grid(row=6,column=2)
        self.bouton_Ajouter.grid(row=7,column=2)

    def envoyer(self): 
        numero=self.champ_numero_patient.get()
        rapport=self.champ_Redaction_Rapport.get("1.0","end-1c")
        Date=self.champ_date.get()
        #numRDV=self.champ_rdv.get()
        # numeroseance=self.champ_numero_Seance.get()
        
        

        #test sur champ numero patient
        testnumero = (len(numero) == 0 or numero.isdigit()==False)
        #test ur champ numero seance
        #testnumeros = (len(numeroseance) == 0 or numeroseance.isdigit()==False)
        #test sur champ rapport   
        testrapp = (len(rapport) == 0)
        #test sur la date 
        #testDate = Fenetre_inscription.Fenetre_inscription.testDate(Date,0)

        #pour recupere le nom et prenom du patient
        reponsepatient=CreationDB.collectionPatient.find_one({"NumPat":int(numero)}) 
       
        if not reponsepatient:
            messagebox.showerror("error","Patient non trouve")
        else:    
            #ttt
            nom=reponsepatient['Nom']
            prenom=reponsepatient['Prenom']
            
            

            if testnumero or testrapp :    
                messagebox.showerror("Error", "Veuillez bien remplir les champs !!")
            else:
            
                c = canvas.Canvas(".//DossierdesPatients//"+nom+"_"+prenom+"//Certificat//Certificat_"+nom+"_"+prenom+"_.pdf")
                #insertion de entete

                c.drawString(60,780,"CABINET DENTAIRE AJAYOU")
                c.drawString(75,765, "Avenue Med V RABAT")
                c.drawString(73,750,"Tel:(+212)5 37 53 52 48")
                c.line(50,730,560,730)
                    
                #insertion de date
                c.setFont('Helvetica',12)
                c.drawString(400,680,"Date : ")
                c.drawString(450,680,Date)  
                #insertion de la seance
                c.setFont('Helvetica',12)
                                   
                #insertion du rapport
                t = c.beginText()
                t.setTextOrigin(100, 580)
                d="\n".join(wrap(rapport,80))
                t.textLines(d)  
                c.drawText(t)
                # signature
                c.drawString(400,80,"Signature : ")
                #Rapport
                c.setFont( 'Times-Roman', 25 )
                c.setFillColor("Blue")  
                c.drawString(180,620,'CERTIFICAT MEDICAL')
                c.save()
                messagebox.showinfo("Confirmation d'ajout","Certificat Ajoute")
        
                    
                    

                



       


if __name__ == '__main__':   

    f = Fenetre_Creation_Certificat()
    f.fenetre.mainloop()