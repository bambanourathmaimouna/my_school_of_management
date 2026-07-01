import sys
import logging  
from models.users import userModel
from config.constants import MENU_connect


def option_user():

    while True:

        print(MENU_connect)

        choix = input("Choisissez une option (1 pour se connecter, 0 pour quitter) : ")

        if choix == '1':

            user_name = input("Veuillez entrer votre user_name : ")
            password = input("Veuillez entrer votre mot de passe : ")

            liaison = userModel()

            compte = liaison.verification(user_name, password)
            liaison.close()

            if compte:
                nom_users = compte[4]
                role_users = compte[3]

                print(f"\nBienvenue sur votre espace {nom_users} ({role_users})")
                logging.info(f"Connexion réussie pour l'utilisateur : {nom_users} (Rôle : {role_users})")
            
                return compte
            else:
                print("\nNom ou mot de passe incorrect.")
                print("Veuillez réessayer.\n")
                logging.warning(f"Tentative de connexion échouée pour le nom d'utilisateur : '{user_name}'")

        elif choix == '0':

            print("Au revoir !")
            logging.info("L'utilisateur a quitté l'application depuis le menu de connexion.")
            sys.exit()

        else:

            print("Option invalide.\n")
            logging.warning(f"Option invalide saisie dans le menu de connexion : '{choix}'")