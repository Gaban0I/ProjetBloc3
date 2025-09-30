# Projet de Prédiction du Churn Client

## 1. Contexte du Projet

Ce projet a pour objectif de développer un modèle de Machine Learning capable de prédire le churn (résiliation d'abonnement) de clients pour une entreprise de télécommunications. En analysant les données des clients, nous cherchons à identifier les principaux facteurs qui mènent à un churn et à construire un modèle prédictif performant.

Le jeu de données utilisé est le "Telco Customer Churn" disponible sur Kaggle.

## 2. Structure du Projet

Le projet est organisé de la manière suivante :

```
.  
├── data/                # Contient les données brutes et traitées
├── notebooks/           # Contient les notebooks Jupyter pour l'analyse et la modélisation
│   ├── 1_-_Analyse_Exploratoire.ipynb
│   ├── 2_-_Feature_Engineering.ipynb
│   ├── 3_-_Modelisation.ipynb
│   └── 4_-_Presentation_des_Resultats.ipynb
├── src/                 # Contient les scripts Python
│   └── prepare_data.py
├── run_pipeline.py      # Script pour exécuter l'ensemble du pipeline
├── requirements.txt     # Liste des dépendances du projet
└── README.md            # Ce fichier
```

## 3. Installation

Pour exécuter ce projet, vous devez avoir Python 3 installé. Ensuite, installez les bibliothèques nécessaires via pip :

```bash
pip install -r requirements.txt
```

## 4. Utilisation

Il y a deux manières de lancer le projet :

### Méthode 1 : Script Automatisé (Recommandé)

Un script Python a été créé pour exécuter l'ensemble du pipeline, de la préparation des données à l'exécution de tous les notebooks.

1.  Ouvrez un terminal à la racine du projet.
2.  Lancez la commande suivante :

    ```bash
    python run_pipeline.py
    ```

Le script mettra à jour les notebooks avec les derniers résultats.

### Méthode 2 : Exécution Manuelle

Si vous préférez exécuter chaque étape manuellement :

1.  Lancez JupyterLab depuis votre terminal :

    ```bash
    jupyter lab
    ```

2.  Ouvrez et exécutez les notebooks depuis l'interface de JupyterLab, **dans l'ordre suivant** :
    *   `notebooks/1_-_Analyse_Exploratoire.ipynb`
    *   `notebooks/2_-_Feature_Engineering.ipynb`
    *   `notebooks/3_-_Modelisation.ipynb`
    *   `notebooks/4_-_Presentation_des_Resultats.ipynb`

## 5. Étapes du Projet et Documentation

La documentation détaillée de chaque étape se trouve directement dans les notebooks Jupyter correspondants, sous forme de cellules de texte (Markdown) expliquant le code et les résultats.

*   **Étape 1 : Préparation des Données (`src/prepare_data.py`)**
    *   Ce script télécharge le jeu de données depuis Kaggle, le décompresse et effectue un premier nettoyage de la colonne `TotalCharges`.

*   **Étape 2 : Analyse Exploratoire des Données (`notebooks/1_-_Analyse_Exploratoire.ipynb`)**
    *   Ce notebook charge les données nettoyées, effectue une analyse descriptive et visualise les distributions des variables et leurs relations avec la variable cible `Churn`.

*   **Étape 3 : Feature Engineering (`notebooks/2_-_Feature_Engineering.ipynb`)**
    *   Ce notebook gère la préparation finale des données pour la modélisation : encodage des variables catégorielles, division du jeu de données en ensembles d'entraînement et de test, et mise à l'échelle des variables numériques.

*   **Étape 4 : Modélisation et Évaluation (`notebooks/3_-_Modelisation.ipynb`)**
    *   Ce notebook est le cœur du projet. Il entraîne plusieurs modèles (Régression Logistique, Arbre de Décision, Forêt Aléatoire), compare leurs performances, et procède à une optimisation des hyperparamètres du meilleur modèle (Random Forest) via `GridSearchCV`.
    *   Enfin, il évalue le modèle final sur le jeu de test et analyse l'importance des différentes caractéristiques pour prédire le churn.

*   **Étape 5 : Présentation des Résultats (`notebooks/4_-_Presentation_des_Resultats.ipynb`)**
    *   Ce notebook présente les performances du modèle final, les facteurs clés de churn identifiés et des recommandations stratégiques basées sur l'analyse.

## 6. Conclusion

Le modèle final, une Forêt Aléatoire (Random Forest) optimisée, atteint de bonnes performances pour la prédiction du churn. L'analyse a montré que les facteurs les plus influents pour la résiliation sont le type de contrat (`Contract`), l'ancienneté du client (`tenure`) et le montant des frais mensuels (`MonthlyCharges`).
