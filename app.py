import streamlit as st
import pickle
import os

st.title("House Price Prediction")

# Correct relative path
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

st.write("Looking for model at:", model_path)
st.write("File exists:", os.path.exists(model_path))

model = pickle.load(open(model_path, "rb"))

area = st.number_input("Enter area")

if st.button("Predict"):
    result = model.predict([[area]])
    st.success(f"Price: ₹ {int(result[0])}")