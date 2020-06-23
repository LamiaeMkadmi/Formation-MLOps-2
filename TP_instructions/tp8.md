summary: TP8
id: tp8
categories: tp, api
tags: api, flask
status: Published
authors: OCTO Technology
Feedback Link: https://gitlab.com/octo-technology/octo-bda/cercle-formation/dsin2/-/issues/new

# TP8 - Monitoring

## Overview
Duration: 1

### À l'issue de cette section, vous aurez découvert : 

- Comment implémenter une sonde de monitoring de vos prédictions
- Comment créer et alimenter une DB avec les valeurs monitorées
- Comment créer un dashboard de monitoring dans Grafana 

## Monitoring des prédictions et enregistrement dans une DB

- Définir une sonde de monitoring sous forme de fonction Python

Dans le fichier `formation_indus_ds_avancee/monitoring.py`, créer une fonction `monitor` qui retournera la valeur de
votre choix à monitorer. Cette valeur sera enregistrée dans la DB PostreSQL grâce à la fonction `monitor_with_io` 
associée à une tâche Airflow.

- Spécifier la table postgreSQL dans laquelle enregistrer les valeurs à monitorer

Dans le fichier `config.py`, définir la constante `MONITORING_TABLE_NAME` avec un nom unique différent de celui des
autres participants. Cette table sera désormais alimentée par la tâche `monitor` d'Airflow.

- Relancer Airflow et le DAG de prédiction

La tâche `monitor` devrait s'exécuter. Il nous faut désormais créer un dashboard de suivi des valeurs renvoyées par
notre fonction.

## Affichage d'un dashboard de monitoring dans Grafana 

Nous souhaitons maintenant afficher nos valeurs monitorées dans Grafana à partir de la table postgreSQL.

- Accéder à Grafana sur le port `3000` et se connecter avec l'identifiant `admin` et le mot de passe `admin`

- Créer la connexion à la DB postgreSQL

La connexion à définir est la même pour l'ensemble des participants à la formation : cette tâche doit donc être réalisée
en mob programming avec les formateurs.

Nous allons ajouter une *Data Source* de type *postgreSQL* et spécifier les paramètres suivants :

![streamlit-embedded-model](./docs/tp8/data-source-grafana.png)

*Note : Dans le cadre du TP, le paramètre `Host` sera communiqué par le formateur.*

- Créer un simple dashboard de monitoring. 

Il vous suffit de cliquer sur *New dashboard* > *Add Query*, et de spécifier la connexion et la table postgreSQL 
(personnelle) créées lors des étapes précédentes.