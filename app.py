import requests
import streamlit as st
from PIL import Image


@st.cache_data
def init_app():
    # print("Initializing app")
    iris = Image.open('media/iris.png')
    setosa = Image.open('media/setosa.png')
    versicolor = Image.open('media/versicolor.png')
    virginica = Image.open('media/virginica.png')
    return iris, setosa, versicolor, virginica


def post_get_predict(a):
    # URL = 'http://0.0.0.0:8000/predict_flower'
    # URL = 'https://7ecd-89-179-65-195.eu.ngrok.io/predict_flower'
    URL = st.secrets["URL"]
    response = requests.post(URL, json={"sepal_length": a[0],
                                        "sepal_width": a[1],
                                        "petal_length": a[2],
                                        "petal_width": a[3]})
    return response.json()


def test_if_backend_is_working():
    URL = st.secrets["URL"]
    response = requests.get(URL)
    return response.status_code == 200


def show_sidebar():
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

            submitted1 = st.form_submit_button(label='Predict flower 2 🔎')
    return params, submitted1


def main():
    iris, setosa, versicolor, virginica = init_app()

    st.title("Iris flower species Classification App")
    st.image(iris)

    params, submitted1 = show_sidebar()

    if submitted1:
        result: dict = post_get_predict(params)
        st.write(result["flower_class"])
        if result["flower_class"] == "Iris Setosa":
            st.image(setosa)
        if result["flower_class"] == "Iris Versicolour":
            st.image(versicolor)
        if result["flower_class"] == "Iris Virginica":
            st.image(virginica)


if __name__ == '__main__':
    main()
