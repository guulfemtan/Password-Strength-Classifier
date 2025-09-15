import streamlit as st
import joblib

model, vectorizer = joblib.load("password_strength_model.pkl")

strength_map = {0: "Weak", 1: "Medium", 2: "Strong"}

st.title("Password Strength Checker")
password = st.text_input("Enter a password to check its strength:")

if password:
    vect = vectorizer.transform([password])
    pred = model.predict(vect)
    st.success(f"Predicted Strength: {strength_map[pred[0]]}")