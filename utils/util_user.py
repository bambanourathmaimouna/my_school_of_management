from config.constants import (
    MENU_PRINCIPALE, GESTION_DES_ETUDIANTS, GESTION_DES_PROFFESSEURS, 
    GESTION_DES_UTILISATEURS, GESTION_DES_MATIERES, GESTION_DES_NOTES, 
    GESTION_DES_ABSENCES, MENU_connect,OPTION_PRINCIPALE
)
from services.service_users import Gestion_utisateurs
import sys


def gestions_users():
    users = Gestion_utisateurs()
    
    while True:
        print(MENU_PRINCIPALE)
        print(OPTION_PRINCIPALE)
        choix = input("Choisissez une action : ")

        if choix == '1':
            print(GESTION_DES_ETUDIANTS)
            choix_etudiant = input("Choisissez une option : ")
            if choix_etudiant == "1":
                users.Ajouter_etudiant()
                retour_ou_quitter()

            elif choix_etudiant == "2":
                users.Lister_etudiant()
                retour_ou_quitter()

            elif choix_etudiant == "3":
                users.Modifier_etudiant()
                retour_ou_quitter()

            elif choix_etudiant == "4":
                users.Supprimer_etudiant()
                retour_ou_quitter()

            elif choix_etudiant == "5":
                users.Rechercher_etudiant()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")

        elif choix == '2':
            print(GESTION_DES_PROFFESSEURS)
            choix_proffesseur = input("Choisissez une action : ")
            if choix_proffesseur == "1":
                users.Ajouter_professeur()
                retour_ou_quitter()
            elif choix_proffesseur == "2":
                users.Lire_proffesseur()
                retour_ou_quitter()
            elif choix_proffesseur == "3":
                users.Modifier_proffesseur()
                retour_ou_quitter()
            elif choix_proffesseur == "4":
                users.Supprimer_proffesseur()
                retour_ou_quitter()
            elif choix_proffesseur == "5":
                users.Rechercher_proffesseur()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")
                      
        elif choix == '3':
            print(GESTION_DES_UTILISATEURS)
            choix_utilisateur = input("Choisissez une action : ")
            if choix_utilisateur == "1":
                users.Ajouter_utilisateur()
                retour_ou_quitter()
            elif choix_utilisateur == "2":
                users.Lire_utilisateur()
                retour_ou_quitter()
            elif choix_utilisateur == "3":
                users.Modifier_utilisateur()
                retour_ou_quitter()
            elif choix_utilisateur == "4": 
                users.Supprimer_utilisateur()
                retour_ou_quitter()
            elif choix_utilisateur == "5":
                users.Rechercher_utilisateur()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")
                      
        elif choix == "4":
            print(GESTION_DES_MATIERES)
            choix_matiere = input("Choisissez une action : ")
            if choix_matiere == "1":
                users.Ajouter_matiere()
                retour_ou_quitter()
            elif choix_matiere == "2":
                users.Lister_matiere()
                retour_ou_quitter()
            elif choix_matiere == "3":
                users.Modifier_matiere()
                retour_ou_quitter()
            elif choix_matiere == "4":
                users.Supprimer_matiere()
                retour_ou_quitter()
            elif choix_matiere == "5":
                users.Rechercher_matiere()
                retour_ou_quitter()
            elif choix_matiere == "6":
                users.Affectation()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")

        elif choix == "5":
            print(GESTION_DES_NOTES)
            choix_note = input("Choisissez une action : ")
            if choix_note == "1":
                users.Ajouter_note()
                retour_ou_quitter()
            elif choix_note == "2":
                users.Lister_note()
                retour_ou_quitter()
            elif choix_note == "3":
                users.Modifier_note()
                retour_ou_quitter()
            elif choix_note == "4":
                users.Supprimer_note()
                retour_ou_quitter()
            elif choix_note == "5":
                users.Rechercher_note()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")

        elif choix == "6":
            print(GESTION_DES_ABSENCES)
            choix_absence = input("Choisissez une action : ")
            if choix_absence == "1":
                users.Ajouter_absence()
                retour_ou_quitter()
            elif choix_absence == "2":
                users.Lister_absence()
                retour_ou_quitter()
            elif choix_absence == "3":
                users.Modifier_absence()
                retour_ou_quitter()
            elif choix_absence == "4":
                users.Supprimer_absence()
                retour_ou_quitter()
            elif choix_absence == "5":
                users.Rechercher_absence()
                retour_ou_quitter()
            else:
                print("Option invalide, veuillez réessayer.")

        elif choix == "0":
            print(MENU_connect)
            break

        else:
            print("Option invalide, veuillez réessayer.")



def retour_ou_quitter():
    print("\n1. Retour au menu")
    print("0. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "0":
        print("Au revoir !")
        sys.exit()


if __name__ == "__main__":
    gestions_users()
    retour_ou_quitter()
