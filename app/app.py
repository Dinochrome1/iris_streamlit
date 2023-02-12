import requests
import streamlit as st
from PIL import Image

# URL = 'http://0.0.0.0:8000/predict_flower'
URL = 'https://7ecd-89-179-65-195.eu.ngrok.io/predict_flower'

iris = Image.open('app/media/iris.png')
setosa = Image.open('app/media/setosa.png')
versicolor = Image.open('app/media/versicolor.png')
virginica = Image.open('app/media/virginica.png')


def post_get_predict(a):
    response = requests.post(URL, json={"sepal_length": a[0],
                                        "sepal_width": a[1],
                                        "petal_length": a[2],
                                        "petal_width": a[3]})
    return response.json()


st.title("Iris flower species Classification App")
st.image(iris)

st.sidebar.title("Features")
parameter_list = ['Sepal length (cm)',
                  'Sepal Width (cm)',
                  'Petal length (cm)',
                  'Petal Width (cm)']

parameter_default_values = ['5.2', '3.2', '4.2', '1.2']
params = []
st.write('\n\n')

with st.form(key='Form1'):
    with st.sidebar:
        for parameter, parameter_df in zip(parameter_list, parameter_default_values):
            value = st.slider(label=parameter,
                              key=parameter,
                              value=float(parameter_df),
                              min_value=0.0,
                              max_value=8.0,
                              step=0.1)
            params.append(value)

        submitted1 = st.form_submit_button(label='Predict flower 1 🔎')


if submitted1:
    result: dict = post_get_predict(params)
    st.write(result["flower_class"])
    if result["flower_class"] == "Iris Setosa":
        st.image(setosa)
    if result["flower_class"] == "Iris Versicolour":
        st.image(versicolor)
    if result["flower_class"] == "Iris Virginica":
        st.image(virginica)
