from database.bd import ManageBD

class gradeModel(ManageBD):

    def __init__(self):
        super().__init__()

    def Ajouter(self, student_id, subject_id, note):
        self.curseur.execute(
            """
            INSERT INTO grades (student_id, subject_id, note)
            VALUES (?, ?, ?)
            """,
            (student_id, subject_id, note)
        )
        self.conexion.commit()

    def Lire(self):
        self.curseur.execute("SELECT * FROM grades")
        return self.curseur.fetchall()

    def Modifier(self, id_note, student_id, subject_id, note):
        self.curseur.execute(
            """
            UPDATE grades
            SET student_id = ?, subject_id = ?, note = ?
            WHERE id = ?
            """,
            (student_id, subject_id, note, id_note)
        )
        self.conexion.commit()

    def supprimer(self, id_note):
        self.curseur.execute(
            """
            DELETE FROM grades
            WHERE id = ?
            """,
            (id_note,)
        )
        self.conexion.commit()

    def rechercher(self, id_note):
        self.curseur.execute(
            """
            SELECT * FROM grades
            WHERE id = ?
            """,
            (id_note,)
        )
        return self.curseur.fetchall()

    def close(self):
        self.conexion.close()