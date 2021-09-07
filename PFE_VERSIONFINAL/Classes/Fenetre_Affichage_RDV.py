from Lien_DB import CreationDB 
from tkinter import Tk,Label,Entry,Frame,SUNKEN,CENTER,Text,DISABLED


 #TODO : Insere un tableau 
class Fenetre_Affichage_Soin(): 

    def __init__(self,NumeroPatient): 

        self.fenetre = Tk()
        self.fenetre.title("Information du RDV : ")
        color='#99ffff'
        largeurEcran = self.fenetre.winfo_screenwidth() 
        hauteurEcran = self.fenetre.winfo_screenheight() 
        self.fenetre.geometry("+{}+{}".format((largeurEcran // 2) -250 ,(hauteurEcran // 2) - 250))
        self.fenetre.configure(background=color)
        self.fenetre.resizable(width=False, height=False)
        self.cadre = Frame(self.fenetre,bg=color, borderwidth=1,relief='solid')
        self.cadre.pack(padx=2,pady=3) 
        
        #reponserequete = CreationDB.collectionPatient.find_one({"NPatient":NumeroPatient},{"_id":0})
       
        # tb = Table(self.fenetre,
        #                state='disabled',
        #                width=50,
        #                titlerows=1,
        #                rows=5,
        #                cols=4,
        #                colwidth=20)
        # self.tableauVar = ArrayVar(self.fenetre)
        # columns = ['Breed','Price','Location','Age'] 
        # values = [['Doodle','1500','Chicago','1'],
        #       ['Pug','700','Kansas City','2'],
        #       ['Westie','1000','Lincoln','1'],
        #       ['Poodle','900','Atlanta','2']]
        # colonne =0 
        # ligne = 0
        # for col in columns:
        #     index = "%i , %i" % (ligne,colonne)
        #     self.tableauVar[index] = col 
        #     colonne+=1   
        # tb['variable']= self.tableauVar
        # tb.pack()    

        self.fenetre.mainloop()


if __name__ == "__main__": 
     Fenetre_Affichage_Soin(1).fenetre

