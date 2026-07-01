from database.bd import ManageBD

class SubjectModel(ManageBD):
    def __init__(self):
        super().__init__()

    def Ajouter(self, matiere):
        self.curseur.execute(
            "INSERT INTO subjects (matiere) VALUES (?)",
            (matiere,))
        self.conexion.commit()

    def Lire(self):
        self.curseur.execute("SELECT * FROM subjects")
        return self.curseur.fetchall()

    def Modifier(self, id_matiere, matiere):
        self.curseur.execute(
            """
            UPDATE subjects
            SET matiere = ?
            WHERE id = ?
            """,
            (matiere, id_matiere))
        self.conexion.commit()

    def supprimer(self, id_matiere):
        self.curseur.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (id_matiere,))
        self.conexion.commit()

    def rechercher(self, id_matiere):
        self.curseur.execute(
        "SELECT * FROM subjects WHERE id = ?",
        (id_matiere,))
        return self.curseur.fetchall()

    def affecter(self, teacher_id, subject_id):
        self.curseur.execute(
            """
            UPDATE subjects
            SET teacher_id = ?
            WHERE id = ?
            """,
            (teacher_id, subject_id))
        self.conexion.commit()


    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table subjects"""
        self.curseur.execute("DELETE FROM subjects")
        self.conexion.commit()



    def close(self):
        self.conexion.close()
    