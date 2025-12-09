# Solution: Lancer et tester le projet Django avec Docker

## Table des matières

1. [Lancer le projet avec Docker et Makefile](#lancer-le-projet-avec-docker-et-makefile)
2. [Management commands utiles](#management-commands-utiles)
3. [Tests unitaires](#tests-unitaires)
4. [Remarques](#remarques-importantes)
5. [Résumé des workflows](#résumé-des-workflows)
6. [Outils de développement](#outils-de-développement)


---

## 1. Lancer le projet avec Docker et Makefile

Le projet est configuré pour s’exécuter avec **Docker** et une base **PostgreSQL**.  
Des scripts `Makefile` facilitent les opérations courantes pour le développement et les tests.

### Commandes à exécuter:

1 - **Démarrer les conteneurs Docker**  
  `make docker-up`

2 - **Accéder à l’interface Django admin**  
  [Django admin](http://127.0.0.1:8001/admin)

3 - **Créer des données d’exemple**  
  `make docker-create-data`

4 - **Créer un superutilisateur Django**  
  `make docker-superuser`

5 - **Update un utilisateur de test**  
  `make docker-user-test`

6 - **Assigner les permissions aux utilisateurs non-driver**  
  `make docker-assign-perms`

7 - **Se connecter avec l’utilisateur de test** :

  - `username = "andreechretien"`  
  - `password = "test12356"`

8 - **Faire les tests sur l'interface admin Django `Add bus shift`**

9 - **Exécuter les tests unitaires**  
  `make docker-test`

---

## 2. Management commands utiles

- **Arrêter les conteneurs Docker**  
  `make docker-down`

- **Accéder au shell du conteneur web**  
  `make docker-sh`

- **Appliquer les migrations de la base de données**  
  `make docker-migrate`

---

## 3. Tests unitaires

- Les tests sont contenus dans `test_bus_shift_service.py`.  
- Ils couvrent la validation métier et la logique de calcul des temps pour BusShift et BusStop.  
- Les tests sont isolés et utilisent `setUp` pour créer des entités réutilisables (Bus, Driver, Place).  
- Représente un exemple clair de tests unitaires pour un service métier.

---

## 4. Remarques

### create_test_user.py

- Permet de créer ou modifier le mot de passe d’un utilisateur de test.
- Utilisation: choisir un utilisateur de la base de donnée **non driver** par exemple :  
  - `username = "andreechretien"`  
  - `password = "test12356"`

---

## 5. Résumé des workflows

1. Démarrer les conteneurs Docker → `make docker-up`  
2. Créer les données et superutilisateur → `make docker-create-data` + `make docker-superuser`  
3. Assigner les permissions → `make docker-assign-perms`  
4. Créer et utiliser l’utilisateur de test  
5. Exécuter les tests → `make docker-test`  
6. Accéder à l’admin Django → [Django admin](http://127.0.0.1:8001/admin)

---

# 6 Outils de développement : formatage et linting

Le projet inclut des outils pour garantir la qualité et la cohérence du code :

- **black** : formatage automatique du code Python  
- **isort** : tri cohérent des imports  
- **flake8** : vérification du style et détection d’erreurs courantes  
- **pre-commit** : exécution automatique des hooks avant chaque commit  

## Installation

```bash
pip install -r dev-requirements.txt
pre-commit install
```

## Utilisation
- Chaque commit exécutera automatiquement les outils configurés dans .pre-commit-config.yaml.
- Les corrections automatiques seront appliquées si possible.