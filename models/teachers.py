from database.bd import ManageBD


class teacherModel(ManageBD):
    def __init__(self):
        super().__init__()



    def Ajouter(self, nom,prenom,subjects_id):
        self.curseur.execute(
            """
            INSERT INTO teachers (nom,prenom,subjects_id)
            VALUES(?,?,?)
            """, 
            (nom,prenom,subjects_id)) 
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
        (id_teacher,)
    )

        self.conexion.commit()

        print(f"Le professeur avec l'id {id_teacher} a été supprimé.") 
        


    def rechercher(self, id_teacher):
        self.curseur.execute(
            """
            SELECT * FROM teachers WHERE id = ?
            """, (id_teacher,)
        )
        return self.curseur.fetchall()


    def close(self):
        self.conexion.close()
    
