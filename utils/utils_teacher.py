from config.constants import ESPACE_PROFESSEUR
from services.service_professeur import Gestion_teachers
import sys

def gestion_teacher():

    teacher = Gestion_teachers()

    while True:

        print(ESPACE_PROFESSEUR)

        choix = input("Votre choix : ")

        if choix == "1":
            teacher.ajouter_note()
            retour_ou_quitter()


        elif choix == "2":
           teacher.modifier_note()
           retour_ou_quitter()


        elif choix == "3":
            for note in teacher.grades.Lire():
                print(note)
            retour_ou_quitter()
        
        elif choix == "4":
            teacher.afficher_etudiants()
            for etudiant in teacher.afficher_etudiants:
                print(etudiant)
            retour_ou_quitter()

        elif choix == "5":
            etudiant = teacher.student.rechercher()
        
        

        elif choix == "6":
            teacher.ajouter_absence()
            retour_ou_quitter()

        elif choix == "7":
            for absence in teacher.absences.Lire():
                print(absence)
            retour_ou_quitter()

        elif choix == "8":
            teacher.supprimer_notes_etudiant()
            
            liste_eleves = teacher.afficher_etudiants()
            if liste_eleves:
                for etudiant in liste_eleves:
                    print(etudiant)
                    
            retour_ou_quitter()
    
        
        elif choix == "0":
            print("Déconnexion...")
            break

        else:
            print("Choix invalide.")


def retour_ou_quitter():
    print("\n1. Retour au menu")
    print("0. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "0":
        print("Au revoir !")
        sys.exit()
