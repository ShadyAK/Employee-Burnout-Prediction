import lightgbm
import pandas as pd  
import numpy as np
import pickle
def predict_burnout(df):
    try:
        add = open('models_and_pipelines\\burnout_rate\\saved_models/burnout','rb')
        burnout_model = pickle.load(add)
        add.close()
        return burnout_model.predict(df)
    except:
        raise Exception('Entries given to the model have some issue,preprocess using preprocess_data first')

def predict_fatigue(df):
    try:
        add = open('models_and_pipelines\\burnout_rate\\saved_models/fatigue','rb')
        fatigue_model = pickle.load(add)
        add.close()
        return fatigue_model.predict(df)
    except:
        raise Exception('Entries given to the model have some issue,try preprocessing using preprocess_data first')