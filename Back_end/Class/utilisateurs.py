class Utilisateur:
    def __init__(self, nom_utilisateur, mot_de_passe, role_utilisateur, nom_complet=None, email=None, domaine_specialite=None):
        self.__nom_utilisateur = nom_utilisateur
        self.__mot_de_passe = mot_de_passe
        self.__role_utilisateur = role_utilisateur
        self.__nom_complet = nom_complet
        self.__email = email
        self.__domaine_specialite = domaine_specialite
        self.__compte_active = True

    def get_compte_active(self):
        return self.__compte_active
    
    def desactiver_compte(self):
        self.__compte_active = False

    def get_nom_utilisateur(self):
        return self.__nom_utilisateur

    def get_mot_de_passe(self):
        return self.__mot_de_passe

    def get_role_utilisateur(self):
        return self.__role_utilisateur

    def get_nom_complet(self):
        return self.__nom_complet

    def get_email(self):
        return self.__email

    def get_domaine_specialite(self):
        return self.__domaine_specialite
    
    def modifier_information(self, nom_complet=None, email=None, domaine_specialite=None):
        if nom_complet is not None:
            self.__nom_complet = nom_complet
        if email is not None:
            self.__email = email
        if domaine_specialite is not None:
            self.__domaine_specialite = domaine_specialite

class ChefDepartement(Utilisateur):
    def __init__(self, nom_utilisateur, mot_de_passe, nom_complet=None, email=None, domaine_specialite=None, departement=None):
        super().__init__(nom_utilisateur, mot_de_passe, "ChefDepartement", nom_complet, email, domaine_specialite)
        self.__departement = departement

    def get_departement(self):
        return self.__departement


class Professeur(Utilisateur):
    def __init__(self, nom_utilisateur, mot_de_passe, nom_complet=None, email=None, domaine_specialite=None, cours_enseignes=None):
        super().__init__(nom_utilisateur, mot_de_passe, "Professeur", nom_complet, email, domaine_specialite)
        self.__cours_enseignes = cours_enseignes or []

    def get_cours_enseignes(self):
        return self.__cours_enseignes


class Etudiant(Utilisateur):
    def __init__(self, nom_utilisateur, mot_de_passe, nom_complet=None, email=None, domaine_specialite=None, cours_inscrits=None):
        super().__init__(nom_utilisateur, mot_de_passe, "Etudiant", nom_complet, email, domaine_specialite)
        self.__cours_inscrits = cours_inscrits or []

    def get_cours_inscrits(self):
        return self.__cours_inscrits
    
class Tuteur(Utilisateur):
    def __init__(self, nom_utilisateur, mot_de_passe, nom_complet=None, email=None, domaine_specialite=None, matieres_tutorat=None, disponibilites=None):
        super().__init__(nom_utilisateur, mot_de_passe, "Tuteur", nom_complet, email, domaine_specialite)
        self.__matieres_tutorat = matieres_tutorat or []
        self.__disponibilites = disponibilites or []

    def get_matieres_tutorat(self):
        return self.__matieres_tutorat

    def get_disponibilites(self):
        return self.__disponibilites

    def ajouter_matiere_tutorat(self, matiere):
        self.__matieres_tutorat.append(matiere)

    def ajouter_disponibilite(self, disponibilite):
        self.__disponibilites.append(disponibilite)

from ..Config.connexion import connect_to_snowflake
from ..Config.table import create_all_tables

conn = connect_to_snowflake()
create_all_tables(conn)