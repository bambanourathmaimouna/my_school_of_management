from database.bd import ManageBD

class EtudiantModel(ManageBD):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, prenom, age, matricule, classe):
        self.curseur.execute(
            "INSERT INTO students (nom, prenom, age, matricule, classe) VALUES (?, ?, ?, ?, ?)",
            (nom, prenom, age, matricule, classe)
        )
        self.conexion.commit()
        print(f"L'étudiant {nom} {prenom} a été ajouté avec succès.")

    def Lire(self):
        self.curseur.execute("SELECT * FROM students")
        students = self.curseur.fetchall()
        for student in students:
            print(student)
        print("Lecture terminée.")

    def Modification(self, student_id):
        new_nom = input("Veuillez renseigner le nouveau nom : ")
        new_prenom = input("Veuillez renseigner votre prénom : ")
        new_age = int(input("Merci d'indiquer votre âge : "))
        new_matricule = input("Saisissez votre matricule : ")
        new_classe = input("Merci d'indiquer votre classe : ")
        
        self.curseur.execute(
            """UPDATE students 
               SET nom = ?, prenom = ?, age = ?, matricule = ?, classe = ? 
               WHERE id = ?""",
            (new_nom, new_prenom, new_age, new_matricule, new_classe, student_id)
        )
        self.conexion.commit()
        print("Modification effectuée avec succès.")

    def supprime(self,id_etudiants):
        self.curseur.execute(
            "DELETE FROM students WHERE id = ?", 
            (id_etudiants,)
        )
        self.conexion.commit()
        print(f"L'étudiant avec l'id {id_etudiants} a été supprimé.")

    def recherche(self,matricule):
        matricule = input("Entrez le matricule à rechercher : ")
        self.curseur.execute(
            "SELECT * FROM students WHERE matricule LIKE ?", 
            (f"{matricule}",)
        )
        results = self.curseur.fetchall()
        for row in results:
            print(row)

    def close(self):
        self.conexion.close()