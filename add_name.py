from fastapi import FastAPI
from pydantic import BaseModel  # Importez BaseModel pour définir des modèles de données
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = FastAPI()

# Définissez un modèle Pydantic pour représenter les données attendues dans le corps de la requête
class PatientInput(BaseModel):
    nom: str

@app.post("/verifier_et_ajouter_patient/")
def verifier_et_ajouter_patient_api(patient: PatientInput):
    # Votre fonction vérification et ajout de patient
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]    
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    feuille_patients = client.open("caller's names").get_worksheet(1)
    colonne_noms = feuille_patients.col_values(1)

    if patient.nom in colonne_noms:
        return {"message": "Vous êtes déjà notre patient."}
    else:
        nouveau_patient = [patient.nom]
        feuille_patients.append_row(nouveau_patient)
        return {"message": "Vous avez été ajouté avec succès dans notre base de données."}
