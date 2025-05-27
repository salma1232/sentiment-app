import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# Charger les données
df = pd.read_csv(r'C:\Users\USER\Documents\monprojetmaching\sentiment_data.csv')  # Assure-toi d'avoir une colonne 'text' et 'label'

# Nettoyage simple du texte
df['text'] = df['text'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

# Vectorisation TF-IDF
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Séparer les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraîner le modèle SVM
model = LinearSVC()
model.fit(X_train, y_train)

# Prédictions et évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle et du vectoriseur
joblib.dump(model, r'C:\Users\USER\Documents\monprojetmaching\model_svm.pkl')
joblib.dump(vectorizer, r'C:\Users\USER\Documents\monprojetmaching\vectorizer.pkl')

