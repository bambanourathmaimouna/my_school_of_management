from models.student import EtudiantModel
from models.subjects import SubjectModel
from models.grade import gradeModel
from models.absences import AbsenceModel
import logging
class Gestion_teachers:

    def __init__(self):

        self.student = EtudiantModel()
        self.subjects = SubjectModel()
        self.grades = gradeModel()
        self.absences = AbsenceModel()


    

    # -----------------------------
    # 1. AJOUTER NOTES
    # -----------------------------
    def ajouter_note(self):
        id_etudiant = input("Veillez entrer l'id de l'étudiant : ")
        id_matiere = input("Entrer l'id de matière : ")
        note = float(input("Entre la note : "))
        self.grades.Ajouter(id_etudiant, id_matiere, note)
        print("Note ajoutée avec succès!")


    # -----------------------------
    # 2. MODIFIER NOTES
    # ----------------------------- 
    def modifier_note(self):
        id_note = int(input("Entrez l'id de la note : "))
        nouvelle_note = int(input(" Entrez la nouvelle note : "))
        self.grades.Modifier(id_note, nouvelle_note)
        print("Note modifiée avec succès")


    # -----------------------------
    # 3. LISTER LES NOTES
    # -----------------------------
    def afficher_notes(self):
        notes = self.grades.Lister(self.classe)
        if notes:
           for nom, prenom, matiere, note in notes:
            print(f"ID : {notes[0]}, ID_ETUDIANT : {note[1]}, ID_MATIÈRE : {notes[2]}, NOTE : {notes[3]}")
        else:
           print("Aucune note trouvée.")


    # -----------------------------
    # 4. LISTER MES ÉTUDIANTS
    # -----------------------------
    
    def afficher_etudiants(self):
        etudiants = self.student.Lire()

        if etudiants:
            print("\n--- LISTE DES ÉTUDIANTS ---")
            for etudiant in etudiants:
                print(f"ID : {etudiant[0]}, Nom : {etudiant[1]}, Prénom : {etudiant[2]}, Âge : {etudiant[3]}, Matricule : {etudiant[4]}, Classe : {etudiant[5]}")
        else:
            print("Aucun étudiant trouvé.")


    # -----------------------------
    # 5. RECHERCHER UN ÉTUDIANT
    # -----------------------------
    
    def rechercher_etudiant(self):
        matricule = input("Entrez le matricule de l'étudiant : ")
        etudiants = self.student.rechercher(matricule)
        if etudiants:
            for e in etudiants:
                print(f"ID : {e[0]}, Nom : {e[1]}, Prénom : {e[2]}, Âge : {e[3]}, Matricule : {e[4]}, Classe : {e[5]}")
        else:
           print("Aucun étudiant trouvé.")


    # -----------------------------
    # 6. AJOUTER UNE ABSENCE
    # -----------------------------
    def ajouter_absence(self):
        id_etudiant = input("Veillez entrer l'id de étudiant : ")
        date = (input("Entrer la date (Jour-Mois-année) : "))
        motif = input("Veillez entrer le motif : ")
        self.absences.Ajouter(id_etudiant, date, motif)
        print("Absence enregistrée avec succès!")


    # -----------------------------
    # 7. LISTER LES ABSENCES
    # -----------------------------
    def afficher_absences(self):
        absences = self.absences.Lire()
        for a in absences:
            print(f"ID : {a[0]}, ID_ÉTUDIANT : {a[1]}, DATE : {a[2]}, MOTIF : {a[3]}")


    # -----------------------------
    # 8. supprimer_notes_etudiant
    # -----------------------------
    def supprimer_notes_etudiant(self):
        student_id = input("Entrez l'ID de l'étudiant pour supprimer  ses notes : ")
        if student_id.isdigit():
            self.grades.supprimer_note(student_id)
            print(f"Les notes de l'étudiant ID {student_id} ont été supprimées avec succès.")
            logging.info(f"Suppression complète des notes effectuée pour l'étudiant ID {student_id}.")
        else:
            print("ID invalide,l'id n'existe pas.")
            logging.warning(f"Tentative de suppression de notes avec un ID invalide : '{student_id}'")