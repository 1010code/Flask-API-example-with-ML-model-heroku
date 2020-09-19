import pickle
import gzip
import os

PROJECT_DIR=''

# 載入Model
with gzip.open(PROJECT_DIR+'model/xgboost-iris.pgz', 'rb') as f:
    xgboostModel = pickle.load(f)

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted