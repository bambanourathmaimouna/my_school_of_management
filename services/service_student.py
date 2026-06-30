import logging
from models.subjects import SubjectModel
from models.absences import AbsenceModel
from models.grade import gradeModel

class Gestion_student:

    def __init__(self):
        self.subjects = SubjectModel()
        self.grades = gradeModel()
        self.absences = AbsenceModel()

    # ==========================
    # CONSULTER MES NOTES
    # ==========================
    def consulter_mes_notes(self, student_id):
        
        print("DEBUG ID :", student_id)

        notes = self.grades.lire_par_etudiant(int(student_id))

        print("DEBUG NOTES RAW :", notes)

        print("\n--- MES NOTES ---")
        if notes:
            for note in notes:
                print(f"ID_MATIÈRE : {note[2]}, Note : {note[3]}/20")
        else:
            print("Aucune note disponible !.")
            
    # ==========================
    # VOIR MA MOYENNE
    # ==========================
    def voir_ma_moyenne(self, student_id):
        moyenne = self.grades.moyenne_par_etudiant(int(student_id))
        logging.info(f"L'étudiant ID {student_id} a consulté sa moyenne générale.")
        
        print("\n--- MA MOYENNE GÉNÉRALE ---")
        if moyenne and moyenne[0] is not None:
            print(f"Moyenne générale : {moyenne[0]:.2f}/20")
        else:
            print("Aucune note disponible pour calculer la moyenne.")

    # ==========================
    # CONSULTER MES ABSENCES
    # ==========================
    def consulter_mes_absences(self, student_id):
        absences = self.absences.lire_par_etudiant(int(student_id))
        logging.info(f"L'étudiant ID {student_id} a consulté ses absences.")
        
        print("\n--- MES ABSENCES ---")
        if absences:
            for absence in absences:
                print(f"Date : {absence[0]} | Statut : {absence[1]}")
        else:
            print("Aucune absence enregistrée. Félicitations !")
           
    # ==========================
    # CONSULTER MES MATIÈRES
    # ==========================
    def consulter_mes_matieres(self):
        logging.info("Consultation de la liste des matières globales.")
        
        print("\n--- MES MATIÈRES ---")
        matieres = self.subjects.Lire()
        if matieres:
            for matiere in matieres:
                print(f"- {matiere}")
        else:
            print("Aucune matière enregistrée.")