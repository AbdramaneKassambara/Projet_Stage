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
    
    @staticmethod
    def recuperer_utilisateur_par_nom(cursor, nom_utilisateur):
        try:
            cursor.execute("""
                SELECT * FROM Utilisateurs
                WHERE nom_utilisateur=%s
            """, (nom_utilisateur,))
            row = cursor.fetchone()
            if row:
                # Retournez tous les détails de l'utilisateur
                return row
        except Exception as e:
            print(f"Erreur lors de la récupération de l'utilisateur par nom : {e}")
        return None
    
    def create(self, cursor):
        try:
            # Vérifier si l'utilisateur existe déjà
            existing_user = Utilisateur.recuperer_utilisateur_par_nom(cursor, self.get_nom_utilisateur())
            if existing_user:
                print("L'utilisateur existe déjà.")
            else:
                # L'utilisateur n'existe pas
                cursor.execute("""
                    INSERT INTO Utilisateurs (nom_utilisateur, mot_de_passe, role_utilisateur, nom_complet, email, domaine_specialite, compte_active)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (self.get_nom_utilisateur(), self.get_mot_de_passe(), self.get_role_utilisateur(),
                    self.get_nom_complet(), self.get_email(), self.get_domaine_specialite(), self.get_compte_active()))
                print("Utilisateur ajouté avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur dans la base de données : {e}")

    @staticmethod
    def login_utilisateur(cursor, nom_utilisateur, mot_de_passe, role_utilisateur):
        try:
            cursor.execute("""
                SELECT * FROM Utilisateurs
                WHERE nom_utilisateur=%s AND mot_de_passe=%s AND role_utilisateur=%s
            """, (nom_utilisateur, mot_de_passe, role_utilisateur))
            row = cursor.fetchone()
            if row:
                # Retournez tous les détails de l'utilisateur
                return row
        except Exception as e:
            print(f"Erreur lors de la tentative de connexion : {e}")
        return None
    
    @staticmethod
    def recuperer_professeur_par_domaine(cursor, domaine_specialite):
        try:
            cursor.execute("""
                SELECT * FROM Utilisateurs
                WHERE role_utilisateur='Professeur' AND domaine_specialite=%s
            """, (domaine_specialite,))
            rows = cursor.fetchall()
            if rows:
                # Retournez tous les détails des professeurs dans le domaine spécifié
                return rows
        except Exception as e:
            print(f"Erreur lors de la récupération des professeurs par domaine : {e}")
        return None
    
    @staticmethod
    def modifier_informations(cursor, nom_utilisateur, mot_de_passe, new_nom, new_mot_de_passe, new_email, new_domaine):
        try:
            cursor.execute("""
                UPDATE Utilisateurs
                SET nom_utilisateur=%s, mot_de_passe=%s, email=%s, domaine_specialite=%s
                WHERE nom_utilisateur=%s AND mot_de_passe=%s
            """, (new_nom, new_mot_de_passe, new_email, new_domaine, nom_utilisateur, mot_de_passe))
            print("Informations mises à jour avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la modification des informations : {e}")
            return None
        
    @staticmethod
    def desactiver_compte(self, cursor):
        try:
            cursor.execute("""
                UPDATE Utilisateurs
                SET compte_active = FALSE
                WHERE nom_utilisateur = %s
            """, (self.get_nom_utilisateur(),))
            print("Compte désactivé avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la désactivation du compte : {e}")
            return None


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
    
    def create(self, cursor):
        try:
            # Vérifier si le professeur existe déjà
            existing_professor = Utilisateur.recuperer_utilisateur_par_nom(cursor, self.get_nom_utilisateur())
            if existing_professor:
                print("Le professeur existe déjà.")
            else:
                # Le professeur n'existe pas
                result = cursor.execute("""
                    INSERT INTO Utilisateurs (nom_utilisateur, mot_de_passe, role_utilisateur, nom_complet, email, domaine_specialite, compte_active)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (self.get_nom_utilisateur(), self.get_mot_de_passe(), self.get_role_utilisateur(),
                      self.get_nom_complet(), self.get_email(), self.get_domaine_specialite(), self.get_compte_active()))
                # Récupérer l'ID du nouvel utilisateur
                ret = cursor.execute("SELECT LAST_INSERT_ID()")
                print(ret)
                #id_new_user = Utilisateur.recuperer_utilisateur_par_nom(cursor,self.get_nom_utilisateur)
                #print (id_new_user)
                # Insérer les informations spécifiques au professeur
                # cursor.execute("""
                #     INSERT INTO Professeurs (id_utilisateur, cours_enseignes)
                #     VALUES (%s, %s)
                # """, (id_new_user, ",".join(self.get_cours_enseignes())))
                # print("Professeur ajouté avec succès.")
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du professeur dans la base de données : {e}")
            return None


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

