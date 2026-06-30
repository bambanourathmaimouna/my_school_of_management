from database.bd import ManageBD


class teacherModel(ManageBD):
    def __init__(self):
        super().__init__()



    def Ajouter(self, nom,prenom,classe,subjects_id):
       self.curseur.execute("""
        INSERT INTO teachers(nom, prenom, classe, subjects_id)
        VALUES (?, ?, ?, ?)
        """, (nom, prenom, classe, subjects_id))
       self.conexion.commit()
       

    def Lire(self):
        self.curseur.execute("SELECT * FROM teachers")
        return self.curseur.fetchall()
    

    def Modifier(self, id_prof, nom, prenom, subjects_id):
        self.curseur.execute(
        """
        UPDATE teachers
        SET nom = ?, prenom = ?, subjects_id = ?
        WHERE id = ?
        """,
        (nom, prenom, subjects_id, id_prof))
        self.conexion.commit()
       

    def supprimer(self, id_teacher):
        self.conexion.execute(
        """
        DELETE FROM teachers
        WHERE id = ?
        """,
        (id_teacher,))
        self.conexion.commit()
        

    def rechercher(self, id_prof):
        self.curseur.execute(
        "SELECT * FROM teachers WHERE id = ?",
        (id_prof,)
    )
        return self.curseur.fetchone()
    

    def recuperer_classe(self, teacher_id):
        self.curseur.execute("""
            SELECT classe
            FROM teachers
            WHERE id = ?
        """, (teacher_id,))

        return self.curseur.fetchone()


    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table teachers"""
        self.curseur.execute("DELETE FROM teachers")
        self.conexion.commit()


    def close(self):
        self.conexion.close()
    
