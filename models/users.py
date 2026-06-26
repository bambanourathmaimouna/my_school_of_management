from database.bd import ManageBD


class userModel(ManageBD):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, prenom, password, role):
        self.curseur.execute(
        """
        INSERT INTO users (nom, prenom, password, role)
        VALUES (?, ?, ?, ?)
        """,
        (nom, prenom, password, role))
        self.conexion.commit()

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
        (role, password, id_user))
        self.conexion.commit()
       

    def rechercher(self, id_users):
       
        self.curseur.execute("SELECT * FROM users WHERE id = ?", (id_users,))
        return self.curseur.fetchall()


    def supprimer(self,id_users):
        self.curseur.execute(
            "DELETE FROM users WHERE id = ?", 
            (id_users,))
        self.conexion.commit()


    def verification(self, nom, password):
        self.curseur.execute(
            "SELECT * FROM users WHERE nom = ? AND password = ?", (nom, password)
        )
        
        utilisateur = self.curseur.fetchone() 
        return utilisateur

    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table users"""
        self.curseur.execute("DELETE FROM users")
        self.conexion.commit()
    
    def close(self): 
        self.conexion.close()


