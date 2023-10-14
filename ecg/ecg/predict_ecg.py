import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

import load
import util
import analyze

# This is just an example. You need to replace this with your actual paths.
data_json = '/home/ubuntu/aimodel/ecg/dev-N.json'
model_path = '/home/ubuntu/aimodel/ecg/saved/cinc17/1696514528-820/0.406-0.867-020-0.264-0.907.h5'

def predict():
    preproc = util.load(os.path.dirname(model_path))
    dataset = load.load_dataset(data_json)
    x, y = preproc.process(*dataset)

    model = keras.models.load_model(model_path)
    probs = model.predict(x, verbose=1)
    results_df, most_probable_class = analyze.analyze_ecg_data(probs)

    print(results_df)
    print(f"The most probable class is: {most_probable_class}")


    return analyze.explain_heartbeat_data(results_df.to_json(), most_probable_class)
