import pytest
import requests
import streamlit as st

from app import post_get_predict


def test_ping():
    url = "http://0.0.0.0:8000/ping"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_get_predict():
    response = post_get_predict([0, 0, 0, 0])
    assert response == {'flower_class': 'Iris Setosa'}


def test_get_predict_2():
    response = post_get_predict([3, 5, 3.2, 4.4])
    assert response == {'flower_class': 'Iris Virginica'}

