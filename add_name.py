import gspread
from oauth2client.service_account import ServiceAccountCredentials

def verifier_et_ajouter_patient(nom):
    # Configuration de l'authentification avec la clé API
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]    
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    
    # Autorisation du client avec les identifiants
    client = gspread.authorize(creds)
    
    # Sélection de la feuille contenant les informations des patients (sheet2)
    feuille_patients = client.open("caller's names").get_worksheet(1)  # Sélectionnez la deuxième feuille (index 1)
    
    # Récupérer toutes les valeurs de la colonne "Nom_Prenom"
    colonne_noms = feuille_patients.col_values(1)  # Colonne 1 = Nom_Prenom
    
    # Vérifier si le nom est déjà présent dans la colonne "Nom_Prenom"
    if nom in colonne_noms:
        return "Vous êtes déjà notre patient."
    else:
        # Ajouter le nom à la liste des patients
        nouveau_patient = [nom]
        feuille_patients.append_row(nouveau_patient)  # Ajouter une nouvelle ligne avec le nom
        
        return "Vous avez été ajouté avec succès dans notre base de données."

# Utilisation de la fonction pour vérifier et ajouter un patient
nom_a_verifier = "Jean Dupont"
resultat = verifier_et_ajouter_patient(nom_a_verifier)
print(resultat)
