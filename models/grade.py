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
            (int(student_id), int(subject_id), float(note))
        )
        self.conexion.commit()

    def Lire(self):
        self.curseur.execute("SELECT * FROM grades")
        return self.curseur.fetchall()

    def lire_par_etudiant(self, student_id):
        """Récupère explicitement la colonne 'note' pour l'étudiant donné"""
        self.curseur.execute(
            """
            SELECT note FROM grades 
            WHERE student_id = ?
            """, 
            (int(student_id),))
        return self.curseur.fetchall()

    def moyenne_par_etudiant(self, student_id):
        self.curseur.execute(
            """
            SELECT AVG(note)
            FROM grades
            WHERE student_id = ?
            """,
            (int(student_id),)
        )
        return self.curseur.fetchone()

    def Modifier(self, id_note, note):
        self.curseur.execute(
            """
            UPDATE grades
            SET note = ?
            WHERE id = ?
            """, 
            (float(note), int(id_note))
        )
        self.conexion.commit()
    
    def supprimer(self, id_note):
        self.curseur.execute(
            """
            DELETE FROM grades
            WHERE id = ?
            """,
            (int(id_note),)
        )
        self.conexion.commit()

    def rechercher(self, id_note):
        self.curseur.execute(
            """
            SELECT * FROM grades
            WHERE id = ?
            """,
            (int(id_note),)
        )
        return self.curseur.fetchall()

    def supprimer_note(self, student_id):
        """Supprime toutes les notes associées à un étudiant spécifique"""
        self.curseur.execute(
            """
            DELETE FROM grades
            WHERE student_id = ?
            """,
            (int(student_id),)
        )
        self.conexion.commit()
        
      
    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table grades"""
        self.curseur.execute("DELETE FROM grades")
        self.conexion.commit()
        



    def close(self):
        self.conexion.close()