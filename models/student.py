from database.bd import ManageBD

class EtudiantModel(ManageBD):
    def __init__(self):
        super().__init__()



    def Ajouter(self, nom, prenom, age, matricule, classe):
        self.curseur.execute(
            """
            INSERT INTO students (nom, prenom, age, matricule, classe)
            VALUES (?, ?, ?, ?, ?)
            """, 
            (nom, prenom, age, matricule, classe)
        )
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

        print("Modification effectuée avec succès.")



    def supprimer(self,id_etudiants):
        self.curseur.execute(
            "DELETE FROM students WHERE id = ?", 
            (id_etudiants,)
        )
        self.conexion.commit()
        print(f"L'étudiant avec l'id {id_etudiants} a été supprimé.")



    def rechercher(self, matricule):
        self.curseur.execute(
        "SELECT * FROM students WHERE matricule = ?",
        (matricule,)
    )
        return self.curseur.fetchall()

    def close(self):
        self.conexion.close()
    





