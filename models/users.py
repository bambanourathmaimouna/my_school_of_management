from database.bd import ManageBD
import sqlite3

class userModel(ManageBD):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, prenom, role, user_name, password):
        self.curseur.execute("""
            INSERT INTO users(nom, prenom, role, user_name, password)
            VALUES (?, ?, ?, ?, ?)
        """, (nom, prenom, role, user_name, password))
        lastid = self.curseur.lastrowid
        self.conexion.commit()
        return lastid

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
        return self.curseur.fetchone()


    def supprimer(self,id_users):
        self.curseur.execute(
            "DELETE FROM users WHERE id = ?", 
            (id_users,))
        self.conexion.commit()


    def verification(self, user_name, password):
          
        self.curseur.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (user_name, password))
                
        utilisateur = self.curseur.fetchone() 
        return utilisateur

    


    def drop_users(self):
        try:
            self.curseur.execute("DROP TABLE IF EXISTS users;")
            self.conexion.commit()
            print("La table 'users' a été supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de la table : {e}")


    def close(self): 
        self.conexion.close()


