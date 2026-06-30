from services.authentification import option_user
from utils.util_user import gestions_users
from utils.utils_teacher import gestion_teacher
from utils.util_student import gestion_student
from utils.logger import logging
from database.bd import ManageBD
from models.users import userModel
from models.student import EtudiantModel

def main():

    auto = option_user()

    if auto:

        role = auto[3]

        if role == "admin":
            gestions_users()

        elif role == "professeur":
            gestion_teacher()

        elif role == "étudiant":

            etudiant = EtudiantModel()
            id_etudiant = etudiant.get_student_id_from_user_id(auto[0])
            gestion_student(id_etudiant[0])
    else:
        print("Rôle non reconnu")

#   vr=ManageBD()
#   vr.users()
# print(f"Erreur lors de la suppression de la table :")

if __name__ == "__main__":
    logging.info("DEMARAGE DE L'APPLICATION")
    main()