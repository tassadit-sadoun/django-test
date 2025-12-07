# Solution

## Lancer le projet avec Docker et Makefile

Le projet est configuré pour s’exécuter avec **Docker** et une base **PostgreSQL**.  
Des scripts `Makefile` facilitent les opérations courantes pour le développement et les tests.

### Commandes Docker / Makefile

- **Démarrer les conteneurs Docker**  
  `make docker-up`

- **Arrêter les conteneurs Docker**  
  `make docker-down`

- **Accéder au shell du conteneur web**  
  `make docker-sh`

- **Appliquer les migrations de la base de données**  
  `make docker-migrate`

- **Créer des données d’exemple**  
  `make docker-create-data`

- **Créer un superutilisateur Django**  
  `make docker-superuser`

- **Lancer le serveur de développement Django**  
  `make docker-run`

- **Assigner les permissions aux utilisateurs non-driver**  
  `make docker-assign-perms`

- **Créer un utilisateur de test**  
  `make docker-user-test`

- **Exécuter les tests unitaires**  
  `make docker-test`

---

## Management commands utiles

### update_non_drivers.py

- Configure tous les utilisateurs **non-driver** pour qu’ils puissent gérer les **BusShift** et **BusStop** dans l’interface Django admin.
- Tous les utilisateurs non-driver deviennent `staff`.
- Ils peuvent **créer, modifier et consulter** les trajets et arrêts depuis l’admin.

### create_test_user.py

- Permet de créer ou modifier le mot de passe d’un utilisateur de test.
- Exemple d’utilisation :  
  - `username = "moniquemasson"`  
  - `password = "test12356"`

---

## Tests unitaires

**Fichier :** `test_bus_shift_service.py`

- Les tests couvrent à la fois :  
  - **La validation métier** (nombre minimum d’arrêts, chevauchement de trajets)  
  - **La logique de calcul des temps** (start_time, end_time, duration)

- Les tests sont **isolés**, utilisant `setUp` pour créer des entités réutilisables :  
  - `Bus`, `Driver`, `Place`
