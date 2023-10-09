# README - Projet Cluster Cassandra avec API

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Table des matières

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Objectifs](#Objectifs)
- [Arboresence](#Arboresence)
- [Guide étape par étape](#Guide-étape-par-étape)
- [Screenshot](#Screenshot)
- [Contributions](#contributions)

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Contexte du projet

Ce projet vise à démontrer la faisabilité de la mise en place d'un cluster Cassandra à l'aide de conteneurs Docker, ainsi que le développement d'une API pour tester l'accessibilité et les temps de réponse de la base de données Cassandra. En tant que développeur en Intelligence Artificielle, cette approche permet de créer un environnement de test et de développement efficace.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Modalités pédagogiques

### Prérequis

- Connaissance de base de Docker et Docker Compose.
- Compréhension de Cassandra et de son modèle de données.
- Maîtrise d'une langue de programmation pour développer l'API (par exemple, Python, Node.js, Java).

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

### Objectifs

En binôme, vous allez accomplir les tâches suivantes :

1. Préparation d'un fichier `docker-compose` pour déployer un cluster Cassandra avec 2 nœuds. Assurez-vous d'inclure un volume pour garantir la persistance des données.

2. Suivez les instructions pour créer la base de données Cassandra et importer les données au format CSV. Cette étape est cruciale pour que votre cluster soit opérationnel.

3. Développez une petite API qui offre les fonctionnalités suivantes :

   - **Obtenir les informations d'un restaurant à partir de son identifiant.**
   - **Récupérer la liste des noms de restaurants en fonction du type de cuisine.**
   - **Obtenir le nombre d'inspections d'un restaurant à partir de son identifiant.**
   - **Récupérer les noms des 10 premiers restaurants d'un grade donné.**

4. En bonus, intégrez cette API dans le fichier `docker-compose` pour une mise en place simplifiée.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Arboresence

Pour organiser le projet sur votre machine, suivez cette arboresence :

```bash
api-REST_Mongodb-CRUD
│ 
├─── client 
│   ├─── .streamlit
│   │   └─── config.toml
│   ├─── pages
│   │   ├─── 01_Create_Post.py
│   │   ├─── 02_Read_Get.py
│   │   ├─── 03_Update_Put.py
│   │   ├─── 04_Delete.py
│   │   └─── 05_Infos.py
│   ├─── client.py
│   └─── requirements_client.txt
│ 
├─── mongo
│   ├─── CO2_emission_by_countries.json
│   └─── Dockerfile
│
├─── server
│   ├─── connection_mongo.py
│   ├─── my_api.py
│   └─── requirements_api.txt
│
├─── .env 
├─── Dockerfile-serveur
├─── docker-compose.yml
└─── readme.md
```

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

### Guide étape par étape

1. **Mise en place du Cluster Cassandra avec Docker Compose**

   - Clonez ce dépôt dans votre environnement de développement.
   - Éditez le fichier `docker-compose.yml` pour définir les paramètres du cluster Cassandra, en veillant à configurer la persistance des données via un volume.
   - Exécutez `docker-compose up` pour démarrer le cluster.

2. **Création de la base de données et Importation des données**

   - Suivez les instructions spécifiques à Cassandra pour créer une base de données et importer les données au format CSV. Ces instructions varient en fonction de votre environnement et de votre modèle de données.

3. **Développement de l'API**

   - Créez une API en utilisant le langage de programmation de votre choix.
   - Implémentez les quatre fonctionnalités spécifiées dans le contexte du projet.
   - Assurez-vous que l'API communique correctement avec le cluster Cassandra déployé.

4. **Intégration de l'API dans le fichier `docker-compose` (Bonus)**

   - Si vous choisissez de réaliser ce bonus, assurez-vous que le service de votre API est également configuré dans le fichier `docker-compose.yml`. Cela permettra de déployer l'API automatiquement avec le cluster Cassandra.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Exécution du projet

1. Pour démarrer le cluster Cassandra, utilisez la commande suivante dans le répertoire du projet :

   ```shell
   docker-compose up
   ```

2. Une fois le cluster opérationnel, exécutez votre API en suivant les instructions spécifiques à votre langage de programmation.

3. Accédez à l'API via les URLs spécifiées dans votre code pour tester les fonctionnalités.

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Conclusion

Ce projet permet d'explorer les capacités de Cassandra en matière de gestion de données distribuées et de développer des compétences en développement d'API. N'hésitez pas à personnaliser ce README en fonction des détails spécifiques de votre implémentation. Bonne chance dans la réalisation de ce projet !

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

## Contributions

Merci au contributeurs de ce projet ! 

<div align=center>

<img src="https://media.giphy.com/media/VgCDAzcKvsR6OM0uWg/giphy.gif" width="50"> 

![image](https://github.com/ggwendall/ggwendall/assets/48108275/edb15cbf-f45a-472c-b934-44762886a231)

![Bottom](https://github.com/ggwendall/ggwendall/assets/48108275/1f58de6a-f411-45fd-86a6-e9aa673332e6)
