import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

import load
import util

deep_ecg_mat = '/home/ubuntu/aimodel/ecg/dev-N.json'
deep_ecg_model_path = '/home/ubuntu/aimodel/dirichlet_model'

def predict():
    preproc = util.load(os.path.dirname(deep_ecg_model_path))
    dataset = load.load_dataset(deep_ecg_mat)
    x, y = preproc.process(*dataset)

    model = keras.models.load_model(deep_ecg_model_path)
    probs = model.predict(x, verbose=1)
    print(probs)

    return probs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_json", help="path to data json")
    parser.add_argument("model_path", help="path to model")
    args = parser.parse_args()
    probs = predict(args.data_json, args.model_path)

    print(probs)
