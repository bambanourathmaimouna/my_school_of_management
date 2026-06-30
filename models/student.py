from database.bd import ManageBD

class EtudiantModel(ManageBD):
    def __init__(self):
        super().__init__()



    def Ajouter(self, nom, prenom, age, matricule, classe, user_id):
        self.curseur.execute(
            """
            INSERT INTO students (nom, prenom, age, matricule, classe, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """, 
            (nom, prenom, age, matricule, classe, user_id))
        self.conexion.commit()


    def Lire(self):
        self.curseur.execute("SELECT * FROM students")
        return self.curseur.fetchall()
    

    def Modifier(self, id_etudiant, nom, prenom, age, matricule, classe):
        self.curseur.execute("""
        UPDATE students
        SET 
        nom=?,prenom=?,age=?,matricule=?,classe=?
        WHERE id=?
        """, (nom, prenom, age, matricule, classe, id_etudiant))
        self.conexion.commit()



    def supprimer(self,id_etudiants):
        self.curseur.execute(
            "DELETE FROM students WHERE id = ?", 
            (id_etudiants,))
        self.conexion.commit()



    def rechercher(self, matricule):
        self.curseur.execute(
        "SELECT * FROM students WHERE matricule = ?",
        (matricule,))
        return self.curseur.fetchall()



    def existe(self, id_etudiant):
        self.curseur.execute(
        "SELECT 1 FROM students WHERE id = ?",
        (id_etudiant,))
        return self.curseur.fetchall() is not None

    def get_student_id_from_user_id(self, user_id):
        self.curseur.execute(
        "SELECT id FROM students WHERE user_id = ?",
        (user_id,))
        return self.curseur.fetchone()



    def ajouter_colonne(self):
        self.curseur.execute("ALTER TABLE students ADD COLUMN user_id INTEGER;")

    def close(self):
        self.conexion.close()
    





