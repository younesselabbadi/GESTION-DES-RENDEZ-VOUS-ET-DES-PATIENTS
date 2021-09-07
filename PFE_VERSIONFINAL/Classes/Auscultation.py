#Classe Auscultation herite de Motif


from Motif import Motif

class Auscultation(Motif): 

    def __init__(self,prix=300):
         super().__init__(prix)
    