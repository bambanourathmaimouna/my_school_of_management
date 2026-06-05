from database.bd import ManageBD


class userModel(ManageBD):
    def __init__(self):
        super().__init__(self)



    def Ajouter(self, nom, prenom):
        self.curseur.execute(
            "INSERT INTO users (nom, prenom,) VALUES (?, ?,)",
            (nom, prenom,)
        )
        self.conexion.commit()
        print(f"L'utilisateur {nom} {prenom} a été ajouté avec succès.")



    def Lire(self):
        self.curseur.execute("SELECT * FROM users")
        students = self.curseur.fetchall()
        for student in students:
            print(student)
        print("Lecture terminée.")




    def supprime(self,id_users):
        self.curseur.execute(
            "DELETE FROM users WHERE id = ?", 
            (id_users,)
        )
        self.conexion.commit()
        print(f"L'utilisateur avec l'id {id_users} a été supprimé.")

