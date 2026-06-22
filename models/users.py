from database.bd import ManageBD


class userModel(ManageBD):
    def __init__(self):
        super().__init__()



    def Ajouter(self, nom, prenom,role, password):
        self.curseur.execute(
            "INSERT INTO users (nom, prenom,role, password) VALUES (?,?,?,?)",
            (nom, prenom,role,password)
        )
        self.conexion.commit()
        print(f"L'utilisateur {nom} {prenom} a été ajouté avec succès.")



    def Lire(self):
        self.curseur.execute("SELECT * FROM users")
        return self.curseur.fetchall()
    

    def Modifier(self, id_user, role, password):
        self.curseur.execute(
        """
        UPDATE users
        SET role = ?, password = ?
        WHERE id = ?
        """,
        (role, password, id_user)
    )
        self.conexion.commit()
       


    def rechercher(self,id_users):
        self.curseur.execute("SELECT * FROM users WHERE id = ?",(id_users)),
        return self.curseur.fetchall()


    def supprimer(self,id_users):
        self.curseur.execute(
            "DELETE FROM users WHERE id = ?", 
            (id_users,)
        )
        self.conexion.commit()
        print(f"L'utilisateur avec l'id {id_users} a été supprimé.")


    def verification(self, nom, password):
        self.curseur.execute(
            "SELECT * FROM users WHERE nom = ? AND password = ?", (nom, password)
        )
        
        utilisateur = self.curseur.fetchone() 
        return utilisateur

    
    def close(self): 
        self.conexion.close()


