from services.authentification import option_user
from utils.util_user import gestions_users
from utils.utils_teacher import gestion_teacher
from utils.util_student import gestion_student
from utils.logger import logging
from models.users import userModel
def main():

    auto = option_user()

    if auto:

        role = auto[3]

        if role == "admin":
            gestions_users()

        elif role == "professeur":
            gestion_teacher()

        elif role == "étudiant":
            id_etudiant = auto[0]
            gestion_student(id_etudiant)
    else:
        print("Rôle non reconnu")

  
if __name__ == "__main__":
    logging.info("DEMARAGE DE L'APPLICATION")
    main()