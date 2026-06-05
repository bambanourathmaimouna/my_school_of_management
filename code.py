# import sqlite3

# conexion = sqlite3.connect("My_school.db")

# curseur  =conexion.cursor()


# curseur.execute("""
# CREATE TABLE IF NOT EXISTS etudiants(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                nom TEXT NOT NULL,
#                prenom TEXT NOT NULL,
#                age INTEGER NOT NULL,
#                matricule TEXT NOT NULL,
#                classe TEXT NOT NULL  )
                      
            
#                """)
# curseur.execute("INSERT INTO etudiants(nom,prenom,age,matricule,classe) VALUES(?,?,?,?,?)",("BAMBA","NOURATH MAIMOUNA","20","18711589F","licence1"))

# conexion.commit()



# def Ajouter():
#     nom = input("veuillez renseigner votre nom : ")
#     prenom = input("veuillez renseigner votre prenom : ")
#     age =int( input("Merci d'indiquer votre age : "))
#     matricule = input("Saisissez votre matricule : ")
#     classe = input("Merci d'indiquer votre classe : ")
    
#     conexion.execute("""
#                     INSERT INTO etudiants(nom,prenom,age,matricule,classe)
#                     VALUES(?,?,?,?,?)
#                     """,(nom,prenom,age,matricule,classe))
#     conexion.commit()
# Ajouter()





# def lire():
#     conexion.execute("SELECT * FROM etudiants")
#     students = curseur.fetchall()
#     for student in students:
#         print(student)
#     conexion.commit()
    


# def Modification():
#     new_nom = input("veuillez renseigner votre nom : ")
#     new_prenom = input("veuillez renseigner votre prenom : ")
#     new_age =int( input("Merci d'indiquer votre age : "))
#     new_matricule = input("Saisissez votre matricule : ")
#     new_classe = input("Merci d'indiquer votre classe : ")
    
#     conexion.execute(
#         """UPDATE etudiants SET nom = ?,prenom = ?,age = ?,matricule = ?,classe = ?  "
#                      WHERE id = ?
#                    """,(new_nom,new_prenom,new_age,new_matricule,new_classe))
#     conexion.commit()


# def supprimé():
#     matricule = input("veuillez entrer le matricule de l'etudiant à suprimer : ")

#     conexion.execute(
#         """
#         DELETE FROM etudiants
#         WHERE matricule = ?    
          
#         """,(matricule,)
#     )

# conexion.commit() 


# def recherche():
    

#     conexion.execute(
#         """SELECT * FROM etudiants 
#         WHERE matricule LIKE ?
#    """ ,())

















# conexion.close()
