import pymongo  

# On cree tout d'abord le lien vers notre base de donnees

lienBD = pymongo.MongoClient("mongodb://localhost:27017/")
BD = lienBD["Cabinet"]

# puis on cree les collections 

collectionMedecin  =  BD["Medecin"] 
collectionPatient =  BD["Patient"]
collectionSecretaire  =  BD["Secretaire"] 
collectionRDV = BD["RDV"] 
collectionSoin = BD["Soin"]  
collectionRapport = BD["Rapport"]
collectionConsultation = BD["Consultation"]
collectionDevis = BD["Devis"]
collectionFacture = BD["Facture"]
collectionPaiement = BD["Paiement"]
collectionAdmin = BD["Admin"] 
collectionCompteur = BD["Compteur"] 


# requete = [{ "entite":"Patient",
#                   "id_dispo":0
#                   },{ 
#                   "entite":"Medecin",
#                   "id_dispo":0
#                   },{ 
#                   "entite":"RDV",
#                   "id_dispo":0
#                   },{ 
#                   "entite":"Secretaire",
#                   "id_dispo":0
#                  },{ 
#                   "entite":"Rapport",
#                   "id_dispo":0
#                   }
#                 ]
# collectionCompteur.insert_many(requete)
 

 
# new_posts = [{"Nom":"Détartrage", 
#                   "Duree":"3 seance", 
#                    "Description":"Le détartrage a pour but d'enlever la plaque dentaire (composée de morceaux d'aliments et de bactéries). À l'aide d'un petit instrument pointu, le dentiste enlève le tartre visible et celui qui se cache sous la gencive",
#                    "prix":"450 DH"},
#                    {"Nom":"Dévitalisation", 
#                    "Duree":" 2 seance",
#                   "Description":"Lorsque la carie est trop profonde, et une fois la pulpe dentaire atteinte,on ne pourra malheureusement pas conserver la dent vivante. Il faut, pour empêcher la douleur (et la rage de dents inévitable)" ,
#                    "prix":"400 DH"},
#                    {"Nom":"Traitement d'une carie",
#                    "Duree":"4 seance",
#                    "Description":"Lorsqu'elle est cariée, la dent se déminéralise petit à petit, se creuse et il convient d'empêcher une atteinte du nerf",
#                    "prix":"700 DH" }]
# collectionSoin.insert_many(new_posts) 

# collectionAdmin.insert_one({"pseudo":"root","password":"root"})

