from tkinter import Tk,Frame,Label,Entry,Button,Text,messagebox
import Fonction_Affichage_RDV,Fenetre_inscription
from reportlab.pdfgen import canvas 
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from textwrap import wrap
from  PyPDF2  import PdfFileReader,PdfFileWriter
from Lien_DB import CreationDB
import os,datetime


class Fenetre_Creation_Rappot():
    def __init__(self,NumPat,NumMed,NumRDV): 
        self.estvide = True
        self.fenetre = Tk()
        self.fenetre.title("Rediger un Rapport")
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.cadre=Frame(self.fenetre)
        self.numpat = NumPat
        self.nummed = NumMed 
        self.numrdv = NumRDV
        self.cadre.pack()

        self.label_numero_Seance = Label(self.cadre,text="Numero  de Seance:") 
        self.champ_numero_Seance = Entry(self.cadre)
    
        
        self.label_Redaction_Rapport = Label(self.cadre, text="Rapport :" ,width=20,font=("bold", 10))
        self.champ_Redaction_Rapport= Text(self.cadre,width=80,height=20)

        self.bouton_Ajouter =Button(self.cadre,width=10,height=1,text="Confirmer",bg='brown',command=self.envoyer)

        
        self.label_numero_Seance.grid(row=5,column=2)
        self.champ_numero_Seance.grid(row=6,column=2)
        self.label_Redaction_Rapport.grid(row=9,column=2)
        self.champ_Redaction_Rapport.grid(row=10,column=2)
        self.bouton_Ajouter.grid(row=11,column=2)

    def envoyer(self): 

        numeroseance= self.champ_numero_Seance.get()
        rapport=self.champ_Redaction_Rapport.get("1.0","end-1c")
        

        
        #test ur champ numero seance
        testnumeros = (len(numeroseance) == 0 or numeroseance.isdigit()==False)
        #test sur champ rapport   
        testrapp = (len(rapport) == 0)


        #pour recupere le nom et prenom du patient
        reponsepatient=CreationDB.collectionPatient.find_one({"NumPat":self.numpat}) 
       
        if not reponsepatient:
            messagebox.showerror("error","Patient non trouve")
        else:    
            #ttt
            
            nom=reponsepatient['Nom']
            prenom=reponsepatient['Prenom']
            date = datetime.datetime.now().strftime("%d-%m-%Y")
            dir_path = os.path.dirname(os.path.abspath(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+".pdf"))
            cheminabsolue = dir_path+"//"+nom+"_"+prenom+"_"+str(self.numrdv)+".pdf"

            if  testnumeros or testrapp :    
                messagebox.showerror("Error", "Veuillez bien remplir les champs !!")
            else:
                try :
                    open(cheminabsolue,"r")
                    self.estvide = False

                except FileNotFoundError:
                    self.estvide = True


                if self.estvide == True:

                    c = canvas.Canvas(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+".pdf")
                    #insertion de entete

                    c.drawString(60,780,"CABINET DENTAIRE AJAYOU")
                    c.drawString(75,765, "Avenue Med V RABAT")
                    c.drawString(73,750,"Tel:(+212)5 37 53 52 48")
                    c.line(50,730,560,730)
                    
                    #insertion de date
                    c.setFont('Helvetica',12)
                    c.drawString(400,680,"Date : ")
                    c.drawString(450,680,date)  
                    #insertion de la seance
                    c.setFont('Helvetica',12)
                    c.drawString(100,580,"Seance 1 :")               
                    #insertion du rapport
                    t = c.beginText()
                    t.setTextOrigin(100, 550)
                    d="\n".join(wrap(rapport,80))
                    t.textLines(d)  
                    c.drawText(t)
                    #Rapport
                    c.setFont( 'Times-Roman', 25 )
                    c.setFillColor("Blue")  
                    c.drawString(250,620,'RAPPORT')
                    c.save()
                    messagebox.showinfo("Confirmation d'ajout","Rapport Ajoute")
        
                    numRapport  = Fonction_Affichage_RDV.GenererID("Rapport")
             
                    reponseRapport = CreationDB.collectionRapport.insert_one(
                                                                            {
                                                                            "NumRapport":numRapport,
                                                                            "NumRDV":self.numrdv,
                                                                            "NumPat":self.numpat,
                                                                            "Chemine":cheminabsolue
                                                                            }
                                                                            )
                    reponseRDV = CreationDB.collectionRDV.update_one(
                                                                    {"NumRDV":int(self.numrdv)
                                                                    },
                                                                    {
                                                                    "$push":
                                                                    {
                                                                    "Rapport":
                                                                    {"NumRapport":numRapport,
                                                                    "NumRDV":self.numrdv,
                                                                    "NumPat":self.numpat,
                                                                    "Chemin":cheminabsolue
                                                                    }
                                                                    }
                                                                    })
            
                    if reponseRapport and reponseRDV:
                        messagebox.showinfo("Rapport","Rapport ajoute au bd")
                    else:
                        messagebox.showerror("erreur","Rapport n'est pas ajoute au bd")
                    self.estvide = False

                else:
                    if (os.access(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+".pdf",os.W_OK)):
                        c = canvas.Canvas(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+"_"+numeroseance+".pdf")  

                    #insertion du rapport
                                     
                    #insertion Date
                        c.setFont('Helvetica',12)
                        c.drawString(400,780,"Date : ")
                        c.drawString(450,780,date) 
                    #insertion Seance
                        c.drawString(100,680," Seance "+numeroseance)
                    
                    # insertion rapport 
                        t = c.beginText()
                        t.setTextOrigin(100, 660)
                        d=" \n ".join(wrap(rapport,80))
                        t.textLines(d)  
                        c.drawText(t)
                    # #Rapport
                    #c.setFont( 'Times-Roman', 25 )
                    #c.setFillColor("Blue")  
                    #c.drawString(250,620,'RAPPORT')
                        c.save() 
                        Fenetre_Creation_Rappot.ajouterAuxRapport(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+".pdf",
                                                                    ".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+"_"+numeroseance+".pdf")
                        os.remove(".//DossierdesPatients//"+nom+"_"+prenom+"//Rapport//"+nom+"_"+prenom+"_"+str(self.numrdv)+"_"+str(numeroseance)+".pdf")
                    else:
                        messagebox.showerror("Erreur","Soin deja cloture")

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
        messagebox.showinfo("Rapport","Rapport ajoute au bd")


if __name__ == '__main__':   

    f = Fenetre_Creation_Rappot(0,2,0)
    f.fenetre.mainloop()