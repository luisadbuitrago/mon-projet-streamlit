Présentation du projet

Ce projet est une application web interactive développée avec **Streamlit**, dans le cadre de ma formation en analyse de données. 
L'objectif est de montrer, dans une même application, plusieurs compétences : la structuration d'une interface, la lecture et 
le filtrage de données avec Pandas, la création de visualisations (Seaborn, Plotly) et la mise en place d'un accès sécurisé.

L'application comprend :

- Une page de connexion qui vérifie les identifiants dans le fichier `accounts.csv`.
- Une barre latérale avec un message de bienvenue, un bouton de déconnexion et un menu de navigation.
- Une page Accueil réservée aux utilisateurs connectés.
- Une galerie photos affichée sur 3 colonnes.

Créer l'environnement virtuel (venv):

L'environnement virtuel est un dossier isolé qui contient sa propre copie de Python et ses propres bibliothèques. Il évite les conflits entre projets.

Dans le terminal, à la racine du projet, exécutez :

Windows :
powershell
python -m venv venv


Mac / Linux :
bash
python3 -m venv venv

Connexion de test

Utilisateur - Mot de passe 
utilisateur - mdp123       
admin       - admin123     
