from models.student import EtudiantModel


etudiant = EtudiantModel()

choix = input("choisissez une option : ")

if choix == "1":
    etudiant.Ajouter()

