from models.student import EtudiantModel
from models.teachers import teacherModel
from models.users import userModel
from models.subjects import SubjectModel
from models.grade import gradeModel
from models.absences import AbsenceModel

class Gestion_utisateurs:
    def __init__(self):
        self.student = EtudiantModel()
        self.teachers = teacherModel()
        self.users = userModel()
        self.subjects = SubjectModel()
        self.grades = gradeModel()
        self.absences = AbsenceModel()

    # ==========================================
    # GESTION DES ÉTUDIANTS
    # ==========================================

    def Ajouter_etudiant(self):
        print("\n--- AJOUTER UN ÉTUDIANT ---")

        nom = input("Veuillez renseigner le nom : ")
        prenom = input("Veuillez renseigner le prénom : ")
        age = int(input("Merci d'indiquer l'âge : "))
        matricule = input("Saisissez le matricule : ")
        classe = input("Merci d'indiquer la classe : ")
        password = input("Définir un mot de passe : ")
        print("Étudiant ajouté avec succès !")
        self.student.Ajouter(nom,prenom,age,matricule,classe)
        self.users.Ajouter(nom,prenom,password,"étudiant")
       


    def Lister_etudiant(self,classe):
        print("\n--- LISTE DES ÉTUDIANTS ---")
        resultat = self.student.Lire(classe) 
        if resultat:
            for i in resultat:
                print(i)
        else:
            print("Aucun étudiant trouvé.")


    def Modifier_etudiant(self):
        print("\n--- MODIFIER UN ÉTUDIANT ---")
        id_etudiant = input("Veuillez entrer l'ID de l'étudiant à modifier : ")
        new_nom = input("Veuillez renseigner le nouveau nom : ")
        new_prenom = input("Veuillez renseigner le nouveau prénom : ")
        new_age = int(input("Merci d'indiquer le nouvel âge : "))
        new_matricule =int(input("Saisissez le nouveau matricule : "))
        new_classe = input("Merci d'indiquer la nouvelle classe : ")
        self.student.Modifier(id_etudiant, new_nom, new_prenom, new_age, new_matricule, new_classe)
        print("Modification enregistrée avec succès!")

        
    def Supprimer_etudiant(self):
        print("\n--- SUPPRIMER UN ÉTUDIANT ---")
        id_etudiant = input("Veuillez entrer l'ID de l'étudiant à supprimer : ")
        self.student.supprimer(id_etudiant)
        print(f"L'étudiant ayant l'id {id_etudiant} a été supprimer!")


    def Rechercher_etudiant(self):
        print("\n--- RECHERCHER UN ÉTUDIANT ---")
        matricule = input("Entrez le matricule de l'élève que vous cherchez : ")
        resultat = self.student.rechercher(matricule)
        if resultat:
           for etudiant in resultat:
            print(etudiant)
        else:
           print("Aucun étudiant trouvé.")

    # ==========================================
    # GESTION DES PROFESSEURS
    # ==========================================

    def Ajouter_professeur(self):

       print("\n--- AJOUTER UN PROFESSEUR ---")
       nom = input("Veillez entrer le nom du professeur : ")
       prenom = input("Veillez entrer le prénom du professeur : ")
       classe = input("Entrez la classe SVP : ")
       subject_id = input("Entrer l'id de la matière : ")
       password = input("Mot de passe : ")
       
       self.teachers.Ajouter(nom,prenom,classe,subject_id)
       self.users.Ajouter(nom,prenom,password,"professeur")
       print(f"\nLe professeur {nom} {prenom} a été ajouté avec succès.")



    def Lire_proffesseur(self):
        print("\n--- LISTE DES PROFESSEURS ---")
        resultat = self.teachers.Lire()
        if resultat:
            for proffesseur in resultat:
                print(proffesseur)
        else:
            print("Aucun étudiant trouvé.")


    def Modifier_proffesseur(self):
        print("\n--- MODIFIER UN PROFESSEUR ---")
        id_prof = input("Veuillez entrer l'ID du professeur : ")
        nom = input("Veuillez renseigner le nouveau nom : ")
        prenom = input("Veuillez renseigner le nouveau prénom : ")
        matiere = input("Veuillez entrer l'id de la nouvelle matière : ")
        self.teachers.Modifier(id_prof, nom, prenom, matiere)
        print("Modification effectuée avec succès !")


    def Supprimer_proffesseur(self):
        print("\n--- SUPPRIMER UN PROFESSEUR ---")
        id_prof = input("Veuillez entrer l'ID du professeur à supprimer : ")
        self.teachers.supprimer(id_prof)
        print("Professeur supprimé avec succès !")


    def Rechercher_proffesseur(self):
        print("\n--- RECHERCHER UN PROFESSEUR ---")
        id_prof = int(input("Entrez l'ID du professeur recherché : "))
        resultat = self.teachers.rechercher(id_prof)
        if resultat:
           for proffesseur in resultat:
            print(proffesseur)
        else:
           print("Aucun proffesseur trouvé.")


    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================
       
    def Ajouter_utilisateur(self):
        print("\n--- AJOUTER UN UTILISATEUR ---")
        nom = input("Veuillez renseigner le nom de l'utilisateur : ")
        prenom = input("Veuillez renseigner le prénom de l'utilisateur : ")
        role = input("Veuillez renseigner le rôle (admin/professeur/étudiant) : ")
        password = input("Merci de renseigner le mot de passe : ")
        self.users.Ajouter(nom, prenom, password, role)
        print("Utilisateur ajouté avec succès !")


    def Lire_utilisateur(self):
        print("\n--- LISTE DES UTILISATEURS ---")
        resultat = self.users.Lire() 
        for user in resultat:
            print(user)


    def Modifier_utilisateur(self):
        print("\n--- MODIFIER UN UTILISATEUR ---")
        id_user = input("ID de l'utilisateur : ")
        role = input("Nouveau rôle : ")
        password = input("Nouveau mot de passe : ")
        self.users.Modifier(id_user, role, password)
        print("Modification effectuée avec succès !")


    def Supprimer_utilisateur(self):
        print("\n--- SUPPRIMER UN UTILISATEUR ---")
        id_user = input("ID de l'utilisateur à supprimer : ")
        self.users.supprimer(id_user)
        print("l'utilisateur ayant {id_user} a été supprimer!")


    def Rechercher_utilisateur(self):
        print("\n--- RECHERCHER UN UTILISATEUR ---")
        id_users = int(input("Entrez l'ID de l'utilisateur : "))
        resultat = self.users.rechercher(id_users)
        if resultat:
           print(resultat)
        else:
            print("Utilisateur introuvable.")
    # ==========================================
    #        GESTION DES MATIÈRES
    # ==========================================

    def Ajouter_matiere(self):
        print("\n--- AJOUTER UNE MATIÈRE ---")
        nom = input("Veillez entrer le nom de la matière : ")
        self.subjects.Ajouter(nom)
        print("Matière ajoutée avec succès !")
    

    def Lister_matiere(self):
        print("\n--- LISTER UNE MATIÈRE ---")
        resultat = self.subjects.Lire() 
        for matière in resultat:
            print(matière)


    def Modifier_matiere(self):
        print("\n--- MODIFIER UNE MATIÈRE ---")
        id_matiere = input("Entrez l'id de la matière : ")
        matiere = input("Entrez le nouveau nom de la matière : ")
        self.subjects.Modifier(id_matiere, matiere)
        print("Matière modifiée avec succès !")


    def Rechercher_matiere(self):
        print("\n--- RECHERCHER UNE MATIÈRE ---")
        id_matiere = input("Entrez l'ID de la matière : ")
        resultat = self.subjects.rechercher(id_matiere)
        if resultat:
           for matiere in resultat:
            print(matiere)
        else:
            print("Aucune matière trouvée.")

    
    def Supprimer_matiere(self):
        print("\n--- SUPPRIMER UNE MATIÈRE ---")
        id_matiere = input("Entrez l'ID de la matière à supprimer : ")
        self.subjects.supprimer(id_matiere)
        print("Matière supprimée avec succès !")



    def Affectation(self):
        print("\n--- AFFECTER UNE MATIÈRE ---")

        id_teacher = input("Entrez l'ID du professeur : ")
        id_matiere = input("Entrez l'ID de la matière : ")
        self.subjects.affecter(id_teacher, id_matiere)
        print("Matière affectée avec succès !")

   