# app.py

import sqlite3

print("\nApplication de Gestion de contacte avec Python et Sqlite3\n")

try:

  with sqlite3.connect("cont@ct.db") as connection:
      cursor = connection.cursor()

  # Partie d'Idenfitication 

  class User():
    """
    cette classe definie l'identifiant de l'utulisateur
    """

    def __init__(self, nom = input("Veuiller entrer votre prenom :\n"), 
                      prenom = input("Veuillez entrer votre nom :\n") ,
                ):
      
      self.prenom = prenom
      self.nom = nom
    

    def Menuprincipal(self):

      option = 1 # sa seras l'option ou entrer de l'utulisateur

      while (option != 0):
    # creation de la fonction Menu
        print("\nMenu des suivis de Gestion de contact :\n")
        print(" 1. Ajouter un  numero ")
        print(" 2. Modifier un contact")
        print(" 3. Supprimer un contact")
        print(" 4. Afficher la liste de tous les contacts")
        print(" 5. Rechercher un contact par son numéro de téléphone")
        print(" 0. Exit ")
        try:
          option = int(input("Choisis une option:\n "))
        except ValueError:
          print("\nOption saisis non recommender !\nVeuiller saisir une des principaux options proposer dans le menu !!!\n")
          continue
        else:
          print("Mise en place d'une plateforeme de getion de contact\n")
        
        if option == 0:
          print("\tSortie du programme\n\n \tA BIENTOT !!!")
          break
        

        elif ValueError and option not in (1, 2, 3, 4, 5):
          print("\noption non recommander !!!\n")

        elif option == 1:
          print("Ajout de numero de telephone  !!!")

          new_number = (input("Veuiller entrer votre  numero de tephone :\n"))
          nam_user = input(" Veuiller entrer le nom pour le numero de telephone suivant " +(new_number)+ " :\n")
          
          with sqlite3.connect("cont@ct.db") as connection:
            cursor = connection.cursor()

          new_user = (cursor.lastrowid, new_number , nam_user)

          cursor.execute(
          "CREATE TABLE IF NOT EXISTS GestionDeContact  (id INTEGER PRIMARY KEY AUTOINCREMENT,number_contact TEXT , User_Name TEXT )")
          

          cursor.execute('INSERT INTO GestionDeContact VALUES(?,?,?)', new_user)

          print("De nouvelle donner sont ajouter !!!")

          connection.commit()
        
        elif option == 2:
          print("Modification du contact ")

          with sqlite3.connect("cont@ct.db") as connection:
            cursor = connection.cursor()

          ancien_numero = input("Veuiller entrez le  numero que vous voulez modifier :\n" )
          nouveau_numero = input("Entrez le nouveau numero de :\n")

          cursor.execute(
              "UPDATE GestionDeContact SET number_contact = ? WHERE number_contact = ?",
              (ancien_numero, nouveau_numero)
          )

          connection.commit()

          print("Contact modifier !!!")

        elif option == 3:
          print("suppression de contact !!!\n ")

          with sqlite3.connect("cont@ct.db") as connection:
            cursor = connection.cursor()

          supression = input("Veuiller entrez le  numero que vous voulez suprimer\n" )
        
          cursor.execute(
              "DELETE FROM GestionDeContact WHERE number_contact = ?",
              (supression,)
            )
          print("\nContact supprimer !!!\n")

          connection.commit()

        elif option == 4:
          print("\nAffichage des listes de tout les contacts!!!\n")

          with sqlite3.connect("cont@ct.db") as connection:
            cursor = connection.cursor()

          aff = cursor.execute("SELECT * FROM GestionDeContact")
          for row in aff.fetchall():
            print(row)

          connection.close()

          print("\nVoici les listes de tout les contacts Enregistrer !!!\n")

        elif option == 5:
          print("Recherche de contact par son numéro de téléphone !!!")

          with sqlite3.connect("cont@ct.db") as connection:
            cursor = connection.cursor()
          
          phone_user = input("Veuillez entrer votre numero de telephone : \n",)

          cursor.execute('SELECT * FROM GestionDeContact WHERE number_contact = (?)', (phone_user,))

          print(f"L'info de cette contact est : {cursor.fetchone()}")

          connection.close()
          
  h1 = User()
  h2 = User()
  print("\n\t\t BIENVENUE *** {} *** dans Votre plateforme de gestion de contact ".format(h1.nom))



  # menu du programme 

  h1.Menuprincipal()

except Exception as e:
  print("[ERREUR]", e)
  connection.rollback()

finally :
      connection.close()