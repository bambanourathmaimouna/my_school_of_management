import os
import sqlite3

class ManageBD:

    def __init__(self):
     
        self.conexion = sqlite3.connect("database/My_school.db")
        self.curseur  = self.conexion.cursor()

        self.users()
        self.students()
        self.teachers()
        self.subjects()
        self.grades()
        self.absences()
      
    def users(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('admin','professeur','étudiant')),
                user_name TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL        
            )
            """ 
        )
        self.conexion.commit()

    def students(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                age INTEGER NOT NULL,
                matricule TEXT NOT NULL,
                classe TEXT NOT NULL     
            )
            """)
        self.conexion.commit()

    def teachers(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS teachers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                subjects_id INTEGER,
                classe TEXT NOT NULL,
                FOREIGN KEY (subjects_id) REFERENCES subjects (id)
             )
            """ 
        )
        self.conexion.commit()

    def subjects(self):
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS subjects(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matiere TEXT NOT NULL,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            )
        """)
        self.conexion.commit()

    def grades(self):
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS grades(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                note REAL NOT NULL,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(subject_id) REFERENCES subjects(id)
            )
        """)
        self.conexion.commit()

    def absences(self):
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS absences(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY(student_id) REFERENCES students(id)
            )
        """)
        self.conexion.commit()

    # Correction B : Syntaxe corrigée pour réellement DROP la table si demandé
    def suprimer_table(self):
        try:
            self.curseur.execute("DROP TABLE IF EXISTS teachers;")
            self.conexion.commit()
            print("Table 'teachers' supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")