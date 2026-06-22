import sys
from models.users import userModel
from config.constants import MENU_connect, MENU_PRINCIPALE, OPTION_PRINCIPALE


def option_user():

    while True:

        print(MENU_connect)

        choix = input("Choisissez une option (1 pour se connecter, 0 pour quitter) : ")

        if choix == '1':

            nom = input("Veuillez entrer votre nom : ")
            password = input("Veuillez entrer votre mot de passe : ")

            liaison = userModel()

            compte = liaison.verification(nom, password)
            liaison.close()

            if compte:

                nom_users = compte[1]
                role_users = compte[3]

                print(f"\nBienvenue sur votre espace {nom_users} ({role_users})")
                return compte

            else:

                print("\n Nom ou mot de passe incorrect.")
                print("Veuillez réessayer.\n")

        elif choix == '0':

            print("Au revoir !")
            sys.exit()

        else:

            print(" Option invalide.\n")