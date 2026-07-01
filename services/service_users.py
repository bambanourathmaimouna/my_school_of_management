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

        nom = input("Veuillez renseigner le nom de l'étudiant : ")
        prenom = input("Veuillez renseigner le prénom de l'étudiant : ")
        age = int(input("Merci d'indiquer l'âge de l'étudiant : "))
        matricule = (input("Saisissez le matricule : "))
        classe = input("Merci d'indiquer le niveau de l'étudiant : ")
      
        user_name = input("Définir un nom d'utilisateur (user_name) pour l'étudiant : ")
        password = input("Définir un mot de passe pour l'étudiant : ")  
      
        user_id  = self.users.Ajouter(nom, prenom, "étudiant", user_name, password)
        self.student.Ajouter(nom, prenom, age, matricule, classe, user_id)
        
        

        print(f"\nL'étudiant {nom} {prenom} a été ajouté avec succès !")

    def Lister_etudiant(self):
        print("\n--- LISTE DES ÉTUDIANTS ---")

        resultat = self.student.Lire() 
        if resultat:
            for i in resultat:
               print(f"ID : {i[0]}, NOM : {i[1]}, PRÉNOM : {i[2]}, AGE : {i[3]}, MATRICULE : {i[4]}, CLASSE : {i[5]}")
        else:
            print("Aucun étudiant trouvé.")


    def Modifier_etudiant(self):
        print("\n--- MODIFIER UN ÉTUDIANT ---")

        id_etudiant = input("Veuillez entrer l'ID de l'étudiant à modifier : ")
        new_nom = input("Veuillez renseigner le nouveau nom de l'étudiant : ")
        new_prenom = input("Veuillez renseigner le nouveau prénom de l'étudiant : ")
        new_age = int(input("Merci d'indiquer le nouvel âge de l'étudiant : "))
        new_matricule =int(input("Saisissez le nouveau matricule de l'étudiant : "))
        new_classe = input("Merci d'indiquer la nouvelle classe de l'étudiant : ")
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
            print(f"ID : {etudiant[0]}, NOM : {etudiant[1]}, PRÉNOM : {etudiant[2]}, AGE : {etudiant[3]}, MATRICULE : {etudiant[4]}, CLASSE : {etudiant[5]}")
        else:
           print("Aucun étudiant trouvé.")
    
    def get_student_id_from_user_id(user_id):
        pass

    # ==========================================
    # GESTION DES PROFESSEURS
    # ==========================================

    def Ajouter_professeur(self):
       print("\n--- AJOUTER UN PROFESSEUR ---")

       nom = input("Veillez entrer le nom du professeur : ")
       prenom = input("Veillez entrer le prénom du professeur : ")
       classe = input("Entrez la classe du professeur SVP : ")
       subject_id = input("Entrer l'id de la matière : ")
       user_name = input("Définir un nom d'utilisateur (user_name) pour le professeur  : ")
       password = input("Mot de passe du professeur : ")
       
       self.teachers.Ajouter(nom,prenom,classe,subject_id)
       self.users.Ajouter(nom, prenom, "professeur", user_name, password)
       print(f"Le professeur {nom} {prenom} a été ajouté avec succès.")



    def Lire_proffesseur(self):
        print("\n--- LISTE DES PROFESSEURS ---")

        resultat = self.teachers.Lire()
        if resultat:
            for proffesseur in resultat:
                print(f"ID : {proffesseur[0]}, NOM : {proffesseur[1]}, PRÉNOM : {proffesseur[2]}, MATIÈRE : {proffesseur[3]}, CLASSE : {proffesseur[4]}")
        else:
            print("Aucun étudiant trouvé.")


    def Modifier_proffesseur(self):
        print("\n--- MODIFIER UN PROFESSEUR ---")

        id_prof = input("Veuillez entrer l'ID du professeur à modifier : ")
        nom = input("Veuillez renseigner le nouveau nom du professeur : ")
        prenom = input("Veuillez renseigner le nouveau prénom du professeur: ")
        matiere = input("Veuillez entrer l'id de la nouvelle matière : ")
        self.teachers.Modifier(id_prof, nom, prenom, matiere)
        print("Modification effectuée avec succès !")


    def Supprimer_proffesseur(self):
        print("\n--- SUPPRIMER UN PROFESSEUR ---")

        id_prof = input("Veuillez entrer l'ID du professeur à supprimer : ")
        self.teachers.supprimer(id_prof)
        print(f"Le professeur ayant l'id {id_prof} a été supprimer avec succès !")


    def Rechercher_proffesseur(self):
        print("\n--- RECHERCHER UN PROFESSEUR ---")

        id_prof = int(input("Entrez l'ID du professeur recherché : "))
        resultat = self.teachers.rechercher(id_prof)
        
        if resultat:
            print(f"ID : {resultat[0]}, NOM : {resultat[1]}, PRÉNOM : {resultat[2]}, MATIÈRE : {resultat[3]}, CLASSE : {resultat[4]}")
        else:
            print("Aucun professeur trouvé.")


    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================
       
    def Ajouter_utilisateur(self):
        print("\n--- AJOUTER UN UTILISATEUR ---")

        nom = input("Veuillez renseigner le nom de l'utilisateur : ")
        prenom = input("Veuillez renseigner le prénom de l'utilisateur : ")
        
        role = input("Veuillez renseigner le rôle (admin/professeur/étudiant) : ").strip().lower()
        
        user_name = input("Définir un nom d'utilisateur (user_name) pour le professeur  : ")
        password = input("Merci de renseigner le mot de passe : ")
        
        self.users.Ajouter(nom, prenom, role, user_name, password)
        print(f"L'utilisateur {nom} {prenom} a été ajouté avec succès !")


    def Lire_utilisateur(self):
        print("\n--- LISTE DES UTILISATEURS ---")

        resultat = self.users.Lire() 
        for user in resultat:
            print(f"ID : {user[0]}, NOM : {user[1]}, PRÉNOM : {user[2]}, ROLE : {user[3]}, PASSWORD : {user[4]}")


    def Modifier_utilisateur(self):
        print("\n--- MODIFIER UN UTILISATEUR ---")

        id_user =int (input("Entrez l'id de l'utilisateur à modifier : "))
        role = input("Veillez entrer le nouveau rôle : ")
        password = input("Nouveau mot de passe : ")
        self.users.Modifier(id_user, role, password)
        print("Modification effectuée avec succès !")


    def Supprimer_utilisateur(self):
        print("\n--- SUPPRIMER UN UTILISATEUR ---")

        id_user = input("Veillez entrer l'id de l'utilisateur à supprimer : ")
        self.users.supprimer(id_user)
        print(f"l'utilisateur ayant {id_user} a été supprimer!")


    def Rechercher_utilisateur(self):
        print("\n--- RECHERCHER UN UTILISATEUR ---")

        id_users = int(input("Entrez l'ID de l'utilisateur : "))
        resultat = self.users.rechercher(id_users)
        if resultat:
           print(f"ID : {resultat[0]}, NOM : {resultat[1]}, PRÉNOM : {resultat[2]}, ROLE : {resultat[3]}, PASSWORD : {resultat[4]}")
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
            print(f"ID : {matière[0]}, NOM : {matière[1]}, NUMERO DU PROF : {matière[2]}")


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
            print(f"ID : {matiere[0]}, NOM : {matiere[1]},NUMERO DU PROF : {matiere[2]}")
        else:
            print("Aucune matière trouvée.")

    
    def Supprimer_matiere(self):
        print("\n--- SUPPRIMER UNE MATIÈRE ---")

        id_matiere = input("Entrez l'ID de la matière à supprimer : ")
        self.subjects.supprimer(id_matiere)
        print(f"La matière ayant l'id {id_matiere} supprimée avec succès !")



    def Affectation(self):
        print("\n--- AFFECTER UNE MATIÈRE ---")

        id_teacher = input("Entrez l'ID du professeur : ")
        id_matiere = input("Entrez l'ID de la matière : ")
        self.subjects.affecter(id_teacher, id_matiere)
        print("Matière affectée avec succès !")

   