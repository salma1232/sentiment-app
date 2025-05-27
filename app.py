import streamlit as st
import joblib

# Charger le modèle et le vectoriseur
model = joblib.load(r"C:\Users\USER\Documents\monprojetmaching\model_svm.pkl")
vectorizer = joblib.load(r"C:\Users\USER\Documents\monprojetmaching\vectorizer.pkl")

st.set_page_config(page_title="Prédiction d'Opinion", layout="centered")
st.title("🧠 Prédiction d'Opinion (SVM)")

st.write("Entrez un texte pour prédire s’il est positif ou négatif.")

# Entrée utilisateur
user_input = st.text_area("Votre texte ici :", "")

# Bouton prédiction
if st.button("Prédire"):
    if user_input.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        vect_text = vectorizer.transform([user_input])
        prediction = model.predict(vect_text)
        st.success(f"✅ Opinion prédite : **{prediction[0]}**")
