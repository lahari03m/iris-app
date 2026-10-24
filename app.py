import streamlit as st
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Iris Predictor", page_icon="🌸")

@st.cache_resource
def train_model():
    iris = load_iris()
    model = RandomForestClassifier(random_state=42)
    model.fit(iris.data, iris.target)
    return model, iris

model, iris = train_model()

st.title("🌸 Iris Flower Species Prediction")
st.write("Enter flower measurements to predict the species.")

sepal_length = st.slider('Sepal length (cm)', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal length (cm)', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal width (cm)', 0.1, 2.5, 0.2)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

if st.button('Predict'):
    prediction = model.predict(input_data)
    predicted_class = iris.target_names[int(prediction[0])]
    st.success(f"🌼 Predicted Iris Species: **{predicted_class}**")
