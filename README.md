# RadinPlanner

RadinPlanner est une application de suivi des dépenses permettant aux utilisateurs de gérer leurs finances en ajoutant, visualisant et filtrant leurs dépenses. L'application utilise Streamlit pour le frontend, FastAPI pour le backend, et Supabase pour la base de données.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fonctionnalités

- Ajouter des dépenses avec des détails tels que le montant, la catégorie, la description et la date.
- Visualiser les dépenses sous forme de tableau et de graphiques.
- Filtrer les dépenses par utilisateur.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/radinplanner.git
    cd radinplanner
    ```

2. Configurez les variables d'environnement :

    Créez un fichier .env à la racine du projet et ajoutez les variables suivantes :

    ```bash
    SUPABASE_URL=https://votre-supabase-url
    SUPABASE_KEY=votre-supabase-key
    ```

3. Construisez et démarrez les conteneurs Docker :

    ```bash docker-compose up --build```

## Utilisation
Une fois les conteneurs démarrés, vous pouvez accéder à l'application à l'adresse suivante : http://localhost:8501

Utilisez la barre latérale pour ajouter un utilisateur, puis ajoutez des dépenses pour cet utilisateur.
Visualisez les dépenses sous forme de tableau et de graphiques interactifs.

## Structure du Projet
Le projet est organisé comme suit :

```css
radinplanner/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml
```

* backend/ : Contient le code FastAPI pour le backend.
* frontend/ : Contient le code Streamlit pour le frontend.
* docker-compose.yml : Fichier de configuration Docker Compose pour orchestrer les conteneurs backend et frontend.

## Licence
Ce projet est sous licence MIT.

