# 🧠 Application Deep Learning - Classification de sentiments dans des textes

##  ✅ 1. Description

Ce projet propose une application de classification automatique de sentiments à partir de textes en langage naturel, rédigés en français ou en anglais.
L’objectif est de construire un pipeline complet de deep learning, de la collecte des données à l’entraînement du modèle, jusqu’à la mise en ligne d’une interface utilisateur interactive via Streamlit.

L’utilisateur peut saisir une opinion, une critique ou un commentaire dans l’une des deux langues.
Le modèle prédit alors si le sentiment exprimé est positif ou négatif, avec une réponse instantanée.

## ✅ 2. Modalité et cas d’usage


- **Modalité** : Texte

- **Cas d’usage** : Classification de sentiments (analyse d’opinions positives ou négatives)

- **Langues supportées** : Français et Anglais

- **Données utilisées** :
  - Un fichier CSV personnalisé de phrases contenant des opinions en français et en anglais, annotées manuellement comme `positive` ou `negative`
  - Les données couvrent des critiques de films, des avis émotionnels et des commentaires courts

- **Modèle entraîné** :
  - ** Support Vector Machine linéaire (LinearSVC)** 
  
 ## ✅ 3. Les étapes réalisées dans le projet

  
  
  - 🧠 Compréhension du traitement automatique du langage naturel (NLP)
  
  -  🧹 Compréhension du traitement automatique du langage naturel (NLP)
  - 🧮 Vectorisation des données textuelles avec TF-IDF
  - 🤖 Entraînement d’un modèle de classification binaire avec LinearSVC
  - 📊 Évaluation de performances à l’aide de métriques classiques (accuracy, F1-score)
  - 🌐 Déploiement de l’application via Streamlit Cloud, permettant un hébergement facile et une interface utilisateur accessible en ligne pour tester des prédictions en temps réel
## ✅ 3. Architecture du projet

![Texte alternatif](https://github.com/salma1232/sentiment-app/blob/c5a3f663ab440adb2e1a583ca2cd6037d3dc52c7/captureprojet.PNG)

Le projet est organisé autour de trois fichiers principaux :
  
  - sentiment_data.csv :

  Fichier de données contenant les phrases en français et en anglais, annotées manuellement avec les labels positive ou negative. Ces données servent à entraîner et évaluer le modèle.
  - train_model.py :

  Script Python qui effectue la préparation des données, la vectorisation avec TF-IDF, puis l’entraînement du modèle de classification binaire **(LinearSVC)** . Ce script sauvegarde ensuite à la fois le modèle entraîné (model_svm.pkl) et le vectoriseur TF-IDF **(vectoriser.pkl)**, nécessaires pour transformer les nouveaux textes lors des prédictions.
  - app.py : 

Application Streamlit qui charge le modèle et le vectoriseur sauvegardés, puis propose une interface utilisateur interactive. L’utilisateur peut saisir un texte en français ou en anglais, qui est d’abord vectorisé avant que le modèle ne prédise si le sentiment est positif ou négatif.

## 📊 Résultats

Après toutes ces étapes, y compris l'entraînement du modèle et l'hébergement via Streamlit Cloud, j’ai obtenu une application que tout le monde peut utiliser directement en ligne grâce à une URL publique.

![Texte alternatif](https://github.com/salma1232/sentiment-app/blob/589dfb0376dea5c5d91337a3046bc7bcfb80950d/Capturedd.PNG)
![Texte alternatif](https://github.com/salma1232/sentiment-app/blob/aff8eded67b95e45e781ef83985224e615d656c7/Capturej.PNG)



