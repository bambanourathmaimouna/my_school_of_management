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
        print("Note ajoutée avec succès")

    # -----------------------------
    # 2. MODIFIER NOTES
    # ----------------------------- 
    def modifier_note(self):
        id_note = input("Entrez l'id de la note : ")
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
            print(f"{nom} {prenom} | Matière : {matiere} | Note : {note}")
        else:
           print("Aucune note trouvée.")



           
    # -----------------------------
    # 3. supprimer_notes_etudiant
    # -----------------------------
    def supprimer_notes_etudiant(self):

        student_id = input("Entrez l'ID de l'étudiant pour supprimer toutes ses notes : ")
    
        if student_id.isdigit():
           
            self.grades.supprimer_note(student_id)
            
            print(f"Toutes les notes de l'étudiant ID {student_id} ont été supprimées avec succès.")
            logging.info(f"Suppression complète des notes effectuée pour l'étudiant ID {student_id}.")
        else:
            print("ID invalide. L'ID doit être un nombre.")
            logging.warning(f"Tentative de suppression de notes avec un ID invalide : '{student_id}'")
    # -----------------------------
    # 4. LISTER MES ÉTUDIANTS
    # -----------------------------
    
    def afficher_etudiants(self):
        
        etudiants = self.student.Lire(self.classe) 
        
        if etudiants:
            return etudiants 
        else:
            print("Aucun étudiant trouvé dans cette classe.")
            return []
        
    # -----------------------------
    # 5. RECHERCHER UN ÉTUDIANT
    # -----------------------------
    
    def rechercher_etudiant(self):
        nom = input("Entrez le nom de l'étudiant : ")
        etudiants = self.student.Rechercher(nom)
        if etudiants:
           for e in etudiants:
            print(e)
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
            print(a)