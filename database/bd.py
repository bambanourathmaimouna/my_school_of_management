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
                role TEXT NOT NULL            
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
            """ 
        )
        self.conexion.commit()

    def teachers(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS teachers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                matiere TEXT NOT NULL  
            )
            """ 
        )
        self.conexion.commit()

    def subjects(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                note INTEGER NOT NULL
            )
            """ 
        )   
        self.conexion.commit()  

    def grades(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS grades(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                teacher_id TEXT NOT NULL
            )
            """ 
        )   
        self.conexion.commit()

    def absences(self):
        self.curseur.execute(
            """
            CREATE TABLE IF NOT EXISTS absences(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """ 
        )
        self.conexion.commit()


