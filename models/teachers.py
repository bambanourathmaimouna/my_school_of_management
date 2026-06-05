from database.bd import ManageBD


class teacherModel(ManageBD):
    def __init__(self):
        super().__init__(self)



    def Ajouter(self, nom,prenom,matiere):
        self.curseur.execute(" INSERT INTO teachers (nom,prenom,matiere) VALUES(?,?,?)", (nom,prenom,matiere))
                           
        self.conexion.commit()
        print("Le proffesseur a été ajouter avec succès")



    def Modification(self):
        new_nom = input("veuillez renseigner votre nom : ")
        new_prenom = input("veuillez renseigner votre prenom : ")
        matiere =input("veillez entrez la matiere")

    
        self.conexion.execute(
         """UPDATE teachers SET nom = ?,prenom = ?, ) "
                      WHERE id = ?
                    """,(new_nom,new_prenom,matiere))
        self.conexion.commit()
        print("Modification effectuée avec succès")


    def supprimé(self,nom,prenom):
        matricule = input("veuillez entrer  à suprimer : ")

        self.conexion.execute(         """
        DELETE FROM teachers
        WHERE id = ?    
                  """,(id,)     )

        self.conexion.commit() 
        print(f"Le proffesseur {nom} {prenom},a été supprimer")



    def recherche(self):
    
        self.conexion.execute(
         """SELECT * FROM teachers 
         WHERE matricule LIKE ?
        """ ,("matricule",))

        self.conexion.commit()
        print("teachers")
