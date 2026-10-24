import streamlit as st
import numpy as np
import joblib
import pickle
from sklearn.datasets import load_iris

# Load the trained model (works for both joblib and pickle files)
@st.cache_resource
def load_model():
    try:
        return joblib.load('model.pkl')
    except Exception:
        with open('model.pkl', 'rb') as f:
            return pickle.load(f)

model = load_model()
iris = load_iris()

# Title
st.title("🌸 Iris Flower Species Prediction")
st.write("Enter flower measurements to predict the species.")

# User inputs
sepal_length = st.slider('Sepal length (cm)', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal length (cm)', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal width (cm)', 0.1, 2.5, 0.2)

# Prepare input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict
if st.button('Predict'):
    prediction = model.predict(input_data)
    predicted_class = iris.target_names[int(prediction[0])]
    st.success(f"🌼 Predicted Iris Species: **{predicted_class}**")