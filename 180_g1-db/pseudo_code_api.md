#  API PUBLIC // "Créer un compte" POST /account
  id_account:
    Caractères tapés valides (Integer)? NON => HTTP 400 Paramètres invalides
    OUI
    Le id_account est unique ? NON => HTTP 400 Paramètres invalides
    OUI
  solde: 
    Montant tapé valide (Integer/Float) NON => Erreur 400 Paramètres invalides
    Montant positif ? NON => HTTP 400 Paramètres invalides
    OUI
    HTTP 200 Réussi (SI PAS GESTION DEVISE) 
  Devise:
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



# API PUBLIC // "Effectuer un virement individu A -> B" POST /account/{id_account}/transfer
  Compte Destination: 
    Caractères tapés valides ? NON => HTTP 400 Paramètres Invalide
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




#  API PRIVE // "Vérifier qu'un compte existe" GET /account/{id_account}/exists
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    id_account existe ? NON => HTTP 404 Le compte n'existe pas
    OUI
    HTTP 200 Le compte existe
 


#  API PRIVE // "Est-ce que la devise est valide ?" GET /currency/{currency_code}/allowed
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    La devise est acceptée ? NON => HTTP 404 Le devise n'est pas acceptée
    OUI
    A t'elle était implémenté ? NON => HTTP 501 La devise n'a pas encore été implémenté
    OUI 
    HTTP 200 La devise est accepté



#  API PRIVE // "Fixe le taux de conversion d'une devise" POST /currency/{currency_code}/rate
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    A t'elle était implémenté ? NON => HTTP 501 La devise n'a pas encore été implémenté
    OUI 
    HTTP 200 Le taux est pris en compte




#  API PRIVE // "Transaction par carte A -> B" POST /transaction/card
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    Solde compte A suffisant ? NON => HTTP 401 La transaction est rejetée du fait d'un solde insuffisant.
    OUI
    Le compte A existe ? NON => HTTP 404 Compte inconnu
    Le compte B existe ? NON => HTTP 404 Compte inconnu
    OUI
    La devise est supporté ? NON => HTTP 406 La devises n'est pas supportée
    OUI
    HTTP 200 La transaction a été enregistré




#  API PRIVE // "Transaction par carte A -> B" POST /transaction/transfer
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    Solde compte A suffisant ? NON => HTTP 401 La transaction est rejetée du fait d'un solde insuffisant.
    OUI
    Le compte A existe ? NON => HTTP 404 Compte inconnu
    Le compte B existe ? NON => HTTP 404 Compte inconnu
    OUI
    La devise est supporté ? NON => HTTP 406 La devises n'est pas supportée
    OUI
    HTTP 200 La transaction a été enregistré



#  API PRIVE // "Transaction par cheque A -> B" POST /transaction/check (ATTENTION LEGERE DIFF AVEC LES AUTRES TRANSACTIONS)
    Le champ est saisie correctement ? NON => HTTP 400 Paramètres invalides
    OUI
    Le compte A existe ? NON => HTTP 404 Compte inconnu
    Le compte B existe ? NON => HTTP 404 Compte inconnu
    OUI
    La devise est supporté ? NON => HTTP 406 La devises n'est pas supportée
    OUI
    HTTP 200 La transaction a été enregistré

 