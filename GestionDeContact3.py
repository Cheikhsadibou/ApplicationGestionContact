import sqlite3

with sqlite3.connect("Repertoire.db") as connection:
  cursor = connection.cursor()

  cursor.execute(
      "CREATE TABLE IF NOT EXISTS ContactClient (id INTEGER PRIMARY KEY AUTOINCREMENT , prenom VARCHAR (50)NOT NULL,  number INT (50)NOT NULL ,nom VARCHAR(50)NOT NULL ,email VARCHAR(50)NOT NULL,  Adress VARCHAR (50)NOT NULL)"
      )

  def Creer_Contact():
      print("Ajouter une contacte :")
      Name_User  = input("Entrer le nom de votre contact: \n")
      number      = input("Veuiller entre le numero de telephone :\n")
      cursor.execute(
        "INSERT INTO ContactClient(prenom ,number) VALUES(?, ?)", (Name_User, number,))
      connection.commit()
      print("Contact Ajouter\n")

  def Modifier_Contact():
      print("modifier Contact ")
      id_Contact = input("Entrer le numero de la contact que vous voulez modifier :\n")
      New_number= input(" Veuiller entrer le nouveau numero pour le numero de telephone suivant " +(id_Contact)+ " :\n")
      cursor.execute("UPDATE ContactClient SET number = ?  WHERE number = ? ",
                    (int(New_number), int(id_Contact)))
      connection.commit()
      print("Contact modifier")

  def Supprimer_Contact():
      print("Suppression de contact :")
      id_Contact = input("Le nom de la Contact  que vous voulez supprimer : \n ")
      cursor.execute(
        "DELETE FROM ContactClient WHERE prenom = ?", (str(id_Contact), ))
      connection.commit()
      print(f"Contact avec comme nom {id_Contact} supprimer")


  def Rechercher_Contact():
      print("Recherche de contact par son numéro de téléphone !!!")
      id_Contact = input("Veuillez entrer votre numero de telephone : \n",)
      Contact = cursor.execute('SELECT * FROM ContactClient WHERE number = (?)', (id_Contact,)
        ).fetchone()
      print(f"L'info de cette contact est : ID = {Contact[0]} , Nom = {Contact[1]} , numbert = {Contact[4]}")
    

  def Afficher_les_Contact():
      print("Afichage de toute les taches")
      Contactes = cursor.execute(
          "SELECT * FROM ContactClient "
          ).fetchall()
      for contact in Contactes:
          print(f"ID : {contact[0]} , Nom : {contact[1]} , numbert : {contact[4]} ")

  def Menu_principal():
      print("=======================================================")
      print("========= Application de Gestion de Contact ===========")
      print("=======================================================")
      print("           1. Ajouter un  numero ")
      print("           2. Modifier un contact")
      print("           3. Supprimer un contact")
      print("           4. Afficher la liste de tous les contacts")
      print("           5. Rechercher un contact par son numéro de téléphone")
      print("           0. Exit ")

      option = int(input("Choisis une option:\n "))

      
      if option == 1 :
        Creer_Contact()
        Menu_principal()

      elif option == 2 :
        Modifier_Contact()
        Menu_principal()

      elif option == 3 :
        Supprimer_Contact()
        Menu_principal()

      elif option == 4 :
        Afficher_les_Contact()
        Menu_principal()
        Menu_principal()

      elif option == 5 :
        Rechercher_Contact()
        Menu_principal()

      elif option == 0 :
        print("Quitter")
        exit()
      else:
          print("Choix non reconnu")
          exit()

Menu_principal()