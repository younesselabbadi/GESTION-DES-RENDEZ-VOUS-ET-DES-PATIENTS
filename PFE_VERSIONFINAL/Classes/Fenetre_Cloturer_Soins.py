from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED,messagebox,Button 
from Patient import Patient
import Fonction_Affichage_RDV
from RDV import RDV 
from Lien_DB import CreationDB
from reportlab.pdfgen import canvas 
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from textwrap import wrap
from  PyPDF2  import PdfFileReader,PdfFileWriter
import os, sys, stat


class Fenetre_Cloturer_Soins(): 

    def __init__(self): 

        self.fenetre = Tk()
        self.fenetre.title("Fenetre Cloturation du soins")
        self.color='#99ffff'
        self.cadrevide=True
        self.fenetre.configure(background=self.color) 
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.fenetre.resizable(width=True, height=True)
        self.cadre = Frame(self.fenetre,bg=self.color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=5) 
        self.label_numero_rdv = Label(self.cadre,text="Numero de RDVs : ",width=20,font=("bold", 10),bg=self.color)
        self.champ_numero_rdv = Entry(self.cadre)
        self.bouton_envoyer = Button(self.cadre,text="Valider",command=self.Cloturation) 
        self.label_numero_rdv.grid(row=0,column=0)
        self.champ_numero_rdv.grid(row=0,column=2)
        self.bouton_envoyer.grid(row=0,column=3,padx=2) 
        self.cadre_dossier = Frame(self.fenetre,bg=self.color)

    def Cloturation(self):
        numRDV=int(self.champ_numero_rdv.get())
        reponserdv=CreationDB.collectionRDV.find_one({"NumRDV":numRDV},{"_id":0}) 
       
 
        if not reponserdv:
            messagebox.showerror("error","Soin non trouve")
        else: 
            numero=reponserdv['NumPatient']
          
            reponsepatient=CreationDB.collectionPatient.find_one({"NumPat":numero},{"_id":0})  
          
            nom=reponsepatient['Nom']
            
            prenom=reponsepatient['Prenom']
            c = canvas.Canvas(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+str(numRDV)+".pdf")
            c.setFont('Helvetica',78)
            c.drawString(100,400,"Fin Du Soin")
            c.save() 
            
            Fenetre_Cloturer_Soins.ajouterAuxRapport(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(numRDV)+".pdf",".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+str(numRDV)+".pdf")
            os.chmod(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(numRDV)+".pdf", stat.S_IRGRP )
            os.remove(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+str(numRDV)+".pdf")
            
                                                      
            

    @staticmethod
    def ajouterAuxRapport(chemine,page):

        output = PdfFileWriter()
        fichier = open(page, "rb")
        pdfajoutee = PdfFileReader(fichier) 
        pdforiginale = PdfFileReader(open(chemine,"rb"))

        if pdforiginale.isEncrypted:
            pdforiginale.decrypt('')
        if pdfajoutee.isEncrypted:
            pdfajoutee.decrypt('')
        
         
        nombrepages = pdforiginale.getNumPages()

        for i in range(0,nombrepages) : 
            output.addPage(pdforiginale.getPage(i))  
           

        output.addPage(pdfajoutee.getPage(0))    

        outputStream = open(chemine, "wb")
        
        output.write(outputStream)
        outputStream.close() 
        fichier.close() 
        messagebox.showinfo("Cloturation","Soin Clôture" )        

if __name__ == "__main__": 
    Fenetre_Cloturer_Soins().fenetre.mainloop()        