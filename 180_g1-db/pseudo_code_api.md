#  API PUBLIC // "Créer un compte" POST /account
 -> Bouton "Créer un compte"
 -> Boite saisie texte "Taper un nombre pour créer votre compte (minimum 8)"
      Caractères tapés valides ET minimum 8 caractères tapés (Integer) ? NON => HTTP 400 Paramètres invalides
      OUI
      Le compte est unique ? NON => HTTP 400 Paramètres invalides
      OUI
 -> Boite saisie texte "Indiquer le montant de votre solde"
      Montant tapé valide (Integer/Float) NON => Erreur 400 Paramètres invalides
      Montant positif ? NON => HTTP 400 Paramètres invalides
      OUI
      HTTP 200 Réussi (SI DEVISE PAR DEFAUT) 
  # Facultatif (par défaut devise = Euro)
  -> Boite saisie texte "Indiquer la devise de votre compte (EX: Euro => EUR; US Dollar => USD; Great Britain Pound => GBP etc... )"
      Caractères tapés valides (String) ? NON => HTTP 400 Paramètres invalides
      OUI
      Devise tapé exisante ? NON => HTTP 400 Paramètres invalides
      OUI
      HTTP 200 Réussi



# API PUBLIC // "Récupérer son solde" GET /account/{id_account}/balance
    Caractères tapés id_account valides ? NON => HTTP 400 Identifiant Invalide
    id_account existe ? NON => HTTP 404 Compte Introuvable
    OUI
    HTTP 200 Réussi



# API PUBLIC // "Récupérer son solde" GET /account/{id_account}/details
    Caractères tapés valides ? NON => HTTP 400 Identifiant Invalide
    A existe ? NON => HTTP 404 Compte Introuvable
    OUI
    HTTP 200 Réussi



# API PUBLIC // Effectuer un virement individu A -> B:
  Compte Destination: 
    Caractères tapés valides ? NON => HTTP 400 Identifiant Invalide
    B existe ? NON => Erreur 400 Paramètres Invalides
    OUI
  Libellé:
    Libellé du compte présent ?
    NON => Erreur 400 Paramètres Invalides
    OUI   
  Solde:
    Est-ce que solde A à l'argent ?
    NON => Erreur 400 Paramètres Invalides
    OUI
  Devise: 
    Devise compte A == devise compte B ?
      OUI
      - Debiter A
      - Crediter B
      - Maj BDD transaction
      NON
      - Conversion Solde Compte A avec devise Compte B
      - Debiter A
      - Crediter B
      - Maj BDD transaction
    HTTP 200 Réussi
    
  Carte:
    Libellé du commerçant présent ?
    NON => Erreur 400
    OUI=>  Devise compte A == devise compte B ?
      OUI
      - Debiter A
      - Crediter B
      - Maj BDD transaction
      NON
      - Conversion Solde Compte A avec devise Compte B
      - Debiter A
      - Crediter B
      - Maj BDD transaction
  Cheque:
    Devise compte A == devise compte B ?
      OUI
      - Debiter A
      - Crediter B
      - Maj BDD transaction
      NON
      - Conversion Solde Compte A avec devise Compte B
      - Debiter A
      - Crediter B
      - Maj BDD transaction



        Type de transaction:
    Virement
      Libellé du compte présent ?
      NON => Erreur 400
      OUI=>  Devise compte A == devise compte B ?
        OUI
        - Debiter A
        - Crediter B
        - Maj BDD transaction
        NON
        - Conversion Solde Compte A avec devise Compte B
        - Debiter A
        - Crediter B
        - Maj BDD transaction
    Carte:
      Libellé du commerçant présent ?
      NON => Erreur 400
      OUI=>  Devise compte A == devise compte B ?
        OUI
        - Debiter A
        - Crediter B
        - Maj BDD transaction
        NON
        - Conversion Solde Compte A avec devise Compte B
        - Debiter A
        - Crediter B
        - Maj BDD transaction
    Cheque:
      Devise compte A == devise compte B ?
        OUI
        - Debiter A
        - Crediter B
        - Maj BDD transaction
        NON
        - Conversion Solde Compte A avec devise Compte B
        - Debiter A
        - Crediter B
        - Maj BDD transaction