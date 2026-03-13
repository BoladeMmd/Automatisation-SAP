# Pipeline-de-donn-es
Ce projet vise a définie un pipeline de données pour automatiser le traitement des données du système d'alerte précoce (SAP) de la Direction de la Réglementation et de la Supervision des Systèmes financiers décentralisés. 

L'objectif principal est d'ameliorer le processus de traitement du systeme d'alerte precoce afin 

Le pipeline de données a pour objectif d'extraire les donnees a partir d'un fichier excel , de le transformer (l'application des differentes regles metiers) et puis de charger les données transformer dans une base de données. Ces données transformés sont ensuite utilisés pour la visualisation. L'architecture proposé repose sur deux couches principales: une couche de processus ETL (backend) orchostré et une couche de visualisation (frontend). Apache airflow a ete utilisé pour orchestrer l'ensemble du processus ETL, python pour le traitement des données, docker pour conteneuriser apache airflow , postgreSQL comme systeme de stockage des bases de données et  streamlit pour la visualisation et l'interface utilisateur.

La solution proposée permet aux utilisateurs de charger le fichier d'entré ,de lancer le traitement automatisé , puis de visualiser les tableaux de bords une fois le traitement des données terminé. 




