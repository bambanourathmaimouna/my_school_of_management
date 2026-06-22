from services.authentification import option_user
from utils.util_students import gestions_users
from utils.util_students import retour_ou_quitter
from database.bd import ManageBD

def main():

    user=ManageBD()
    auto = option_user() 

    # On vérifie qu'un compte a bien été retourné
    if auto: 
        role = auto[3] # On extrait le rôle (l'index 3) de la variable

        if role == 'admin':
            gestions_users()
            
        elif role == 'professeur':
            print("Mode Professeur")
            
        elif role == 'etudiant':
            print("Mode Étudiant")
            
        else:
            print("Rôle non reconnu. Fin du programme.")
if __name__ == "__main__":
    main()