from database.bd import ManageBD

class AbsenceModel(ManageBD):

    def __init__(self):
        super().__init__()


    def Ajouter(self, student_id, date, status):
        self.curseur.execute(
            """
            INSERT INTO absences (student_id, date, status)
            VALUES (?, ?, ?)
            """,
            (student_id, date, status))
        self.conexion.commit()

    
    def Lire(self):
        self.curseur.execute("SELECT * FROM absences")
        return self.curseur.fetchall()


    def Modifier(self, id_absence, student_id, date, status):
        self.curseur.execute(
            """
            UPDATE absences
            SET student_id = ?, date = ?, status = ?
            WHERE id = ?
            """,
            (student_id, date, status, id_absence))
        self.conexion.commit()

    
    def supprimer(self, id_absence):
        self.curseur.execute(
            """
            DELETE FROM absences
            WHERE id = ?
            """,
            (id_absence,))
        self.conexion.commit()

    
    def rechercher(self, id_absence):
        self.curseur.execute(
            """
            SELECT * FROM absences
            WHERE id = ?
            """,
            (id_absence,))
        return self.curseur.fetchall()

    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table absences"""
        self.curseur.execute("DELETE FROM absences")
        self.conexion.commit()
   
    def close(self):
        self.conexion.close()