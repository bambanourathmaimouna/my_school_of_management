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


    def verification(self, user_name, password):
          
        self.curseur.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (user_name, password))
                
        utilisateur = self.curseur.fetchone() 
        return utilisateur

    

    
    def supprimer_toutes_les_notes(self):
        """Supprime absolument TOUTES les notes de la table users"""
        self.curseur.execute("DELETE FROM users")
        self.conexion.commit()

    def ajouter_colonne(self):
        try:
            # 1. On ajoute la colonne sans la contrainte UNIQUE directe
            self.curseur.execute("ALTER TABLE students ADD COLUMN user_name TEXT;")
            
            # 2. On crée l'index unique pour appliquer la contrainte d'unicité
            self.curseur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_students_user_name ON students (user_name);")
            
            # 3. On valide les changements
            self.conexion.commit()
            print("Colonne 'user_name' et son index unique ajoutés avec succès.")
            
        except sqlite3.OperationalError as e:
            # Au cas où la colonne existe déjà si vous relancez le script
            if "duplicate column name" in str(e):
                print("La colonne 'user_name' existe déjà.")
            else:
                raise e


    def drop_users(self):
        try:
            self.curseur.execute("DROP TABLE IF EXISTS users;")
            # On utilise 'conexion' ici aussi
            self.conexion.commit()
            print("La table 'users' a été supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de la table : {e}")


    def close(self): 
        self.conexion.close()


