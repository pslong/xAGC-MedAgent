import numpy as np
import gradio as gr
import tensorflow as tf
from tensorflow import keras
import os

import predict_ecg
# import predict_deep_ecg
import fake_predict_deep_ecg as predict_deep_ecg

def predict_ecg_model():
    return predict_ecg.predict()

def predict_deep_ecg_model():
    return predict_deep_ecg.predict()

# TODO:
def predict(input):
    print(input)
    if input == 'predict_ecg':
        return predict_ecg_model()
    elif input == 'predict_deep_ecg':
        return predict_deep_ecg_model()
    else:
        return predict_ecg_model()

iface = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text"
)

iface.launch(share=True)
