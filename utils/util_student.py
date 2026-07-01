import sys
import logging
from config.constants import ESPACE_ETUDIANT
from services.service_student import Gestion_student
from utils.logger import logging

def retour_ou_quitter():
    print("\n1. Retour au menu")
    print("0. Quitter")

    choix = input("\nVotre choix : ")
    if choix == "0":
        logging.info("L'utilisateur a quitté l'application via le sous-menu.")
        print("AU REVOIR,À BIENTOT !")
        sys.exit()


def gestion_student(id_etudiant):
    student = Gestion_student()
    
    logging.info(f"Session ouverte pour l'étudiant ID : {id_etudiant}")

    while True:
        print(ESPACE_ETUDIANT)
        choix = input("Votre choix : ")

        if choix == "1":
            student.consulter_mes_notes(id_etudiant)
            retour_ou_quitter()

        elif choix == "2":
            student.voir_ma_moyenne(id_etudiant)
            retour_ou_quitter()

        elif choix == "3":
            student.consulter_mes_absences(id_etudiant)
            retour_ou_quitter()

        elif choix == "4":
            student.consulter_mes_matieres()
            retour_ou_quitter()

        elif choix == "0":
            logging.info(f"L'étudiant ID {id_etudiant} s'est déconnecté volontairement.")
            print("Déconnexion...")
            break

        else:
            logging.warning(f"Tentative de choix invalide dans le menu par l'étudiant ID {id_etudiant} : '{choix}'")
            print("Choix invalide. Veuillez réessayer.")